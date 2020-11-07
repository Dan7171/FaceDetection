import torch
from tqdm import tqdm
import const


class CustomTestTrainer(object):
    def __init__(self, model, criterion, optimizer, lr_scheduler, model_store, best_acc1:float = 0,
                 performance_tester=None, accuracy_threshold=0, num_epochs_to_test=None,
                 num_batches_per_epoch_limit=0, perf_logger=None):
        self.model = model
        self.__criterion = criterion
        self.__optimizer = optimizer
        self.__lr_scheduler = lr_scheduler
        self.__model_store = model_store
        self.__best_acc1 = best_acc1
        self.__performance_tester = performance_tester
        self.__performance_threshold = accuracy_threshold
        self.__num_epochs_to_test = num_epochs_to_test
        self.__num_batches_per_epoch_limit = num_batches_per_epoch_limit
        self.__performance_logger = perf_logger

    def train_model(self, start_epoch, end_epoch, data_loaders):
        for epoch in range(start_epoch, end_epoch):
            print(f'Epoch: {epoch}')

            print("lr before train: ", self.__lr_scheduler.get_last_lr())
            # modelling for one epoch
            phase_loss, phase_acc = self.__per_phase(epoch, const.TRAIN_PHASE, data_loaders)
            print(phase_loss, phase_acc)
            phase_loss, phase_acc = self.__per_phase(epoch, const.VAL_PHASE, data_loaders)
            print(phase_loss, phase_acc)

            print("lr after train: ", self.__lr_scheduler.get_last_lr())
            self.__lr_scheduler.step()
            print("lr after train and step: ", self.__lr_scheduler.get_last_lr())

            # remember best acc@1 and save checkpoint
            is_best = phase_acc > self.__best_acc1
            self.__best_acc1 = max(phase_acc, self.__best_acc1)

            self.__model_store.save_model(self.model, self.__optimizer, epoch, self.__best_acc1, is_best)

            if self.__should_test(epoch):
                perf = self.__test_performance(epoch)
                if perf is not None:
                    print (f'Done in {epoch} epochs')
                    print(perf)
                    return perf

    def __test_performance(self, epoch):
        performance_df = self.__performance_tester.test_performance(self.model)
        self.__performance_logger.log_performance(epoch, performance_df)
        for layer in performance_df.index:
            accuracy = performance_df.loc[layer]['acc@1']
            threshold = performance_df.loc[layer]['threshold']
            print ("layer: ", layer, " accuracy: ", accuracy, " threshold: ", threshold)
            if accuracy > self.__performance_threshold:
                return layer, accuracy, threshold

        return None

    def __should_test(self, epoch):
        # If we have a way to test our performance
        # And if we defined a valid performance threshold
        # And if we have a valid "epoch step" after which we wish to test our performance
        # And if we the epoch is a natural number of 'epoch steps'
        # Dayeynu
        return self.__performance_tester is not None\
               and self.__performance_threshold != 0 \
               and self.__num_epochs_to_test is not None \
               and epoch % self.__num_epochs_to_test == 0

    def __per_phase(self, epoch, phase, data_loaders):
        # batch_time, losses, top1, top5, data_time, progress = get_epoch_meters(self.train_loader, epoch)
        phase_loss = 0
        phase_acc = 0
        num_batches = len(data_loaders[phase])
        if 0 < self.__num_batches_per_epoch_limit < num_batches:
            num_batches = self.__num_batches_per_epoch_limit

        # switch to modelling mode
        self.model.train(phase == const.TRAIN_PHASE)
        with torch.set_grad_enabled(phase == const.TRAIN_PHASE):
            data_loader_iter = iter(data_loaders[phase])
            for i in tqdm(range(num_batches), desc=phase):
                (images, target) = next(data_loader_iter)

                batch_loss, batch_acc = self.__per_batch(images, target)
                # print(batch_loss, batch_acc.item())
                if batch_loss >= 10:
                    # I once got a batchloss = Inf so I added this print to give a heads up
                    print('batch_loss >= 10', batch_loss)
                phase_loss += batch_loss / num_batches
                phase_acc += batch_acc / num_batches

        return phase_loss, phase_acc

    def __per_batch(self, images, target):
        if torch.cuda.is_available():
            images = images.cuda(non_blocking=False)
            target = target.cuda(non_blocking=False)

        # compute output
        output = self.model(images)
        loss = self.__criterion(output, target)

        _, preds = torch.max(output, 1)
        # compute gradient and do optimizer step
        if self.model.training:
            self.__optimizer.zero_grad()
            loss.backward()
            self.__optimizer.step()

        return loss.data.item(), torch.sum(preds == target.data).item()/target.shape[0]