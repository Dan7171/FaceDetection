import os
import shutil
import random
import math

num_classes = 100
num_train_pics = 100
num_val_pics = 25

###make new datasets foe experiment 1
path_faces = "/home/ssd_storage/datasets/students/expertise/faces_only_300_189_classes"
path_hands = "/home/ssd_storage/datasets/students/Noam/Hands_upright_bg"
classes_faces = os.listdir(path_faces+"/train")
classes_hands = os.listdir(path_hands+"/train")
path_together = "/home/ssd_storage/datasets/students/expertise/Experiment_1/Hands_and_faces_100_together"
path_each = "/home/ssd_storage/datasets/students/expertise/Experiment_1/Hands_and_faces_100_each"
path_faces_exp = "/home/ssd_storage/datasets/students/expertise/Experiment_1/faces_only"
path_hands_exp = "/home/ssd_storage/datasets/students/expertise/Experiment_1/hands_only"
os.mkdir("/home/ssd_storage/datasets/students/expertise/Experiment_1")
os.mkdir(path_together)
os.mkdir(path_each)
os.mkdir(path_faces_exp)
os.mkdir(path_hands_exp)
for s in ["/train","/val"]:
    os.mkdir(path_together+s)
    os.mkdir(path_each+s)
    os.mkdir(path_faces_exp+s)
    os.mkdir(path_hands_exp+s)

i = 0

#faces
for class_dir in classes_faces:
    source_train = path_faces + "/train/" + class_dir
    dest_faces_exp_train = path_faces_exp + "/train/f" + class_dir
    dest_together_train = path_together + "/train/f" + class_dir
    dest_each_train = path_each + "/train/f" + class_dir
    pics_class_train = os.listdir(source_train)
    n = len(pics_class_train)
    pics_indexes_chosed = set()
    if i < num_classes:
        os.mkdir(dest_faces_exp_train)
        os.mkdir(dest_each_train)
    for choose in range(100):
        rand_pic_i = random.randint(0,n-1)
        while rand_pic_i in pics_indexes_chosed:
            rand_pic_i = random.randint(0,n-1)
        pics_indexes_chosed.add(rand_pic_i)
        pic_name = pics_class_train[rand_pic_i]
        source_train_pic = source_train + "/" + pic_name
        if i < num_classes:
            shutil.copy(source_train_pic, dest_faces_exp_train)
            shutil.copy(source_train_pic, dest_each_train)
        if i < math.floor(num_classes/2):
            if choose == 0:
                os.mkdir(dest_together_train)
            shutil.copy(source_train_pic, dest_together_train)
    source_val = path_faces + "/val/" + class_dir
    dest_faces_exp_val = path_faces_exp + "/val/f" + class_dir
    dest_together_val = path_together + "/val/f" + class_dir
    dest_each_val = path_each + "/val/f" + class_dir
    pics_class_val = os.listdir(source_val)
    n = len(pics_class_val)
    pics_indexes_chosed = set()
    if i < num_classes:
        os.mkdir(dest_faces_exp_val)
        os.mkdir(dest_each_val)
    for choose in range(25):
        rand_pic_i = random.randint(0,n-1)
        while rand_pic_i in pics_indexes_chosed:
            rand_pic_i = random.randint(0,n-1)
        pics_indexes_chosed.add(rand_pic_i)
        pic_name = pics_class_val[rand_pic_i]
        source_val_pic = source_val + "/" + pic_name
        if i < num_classes:
            shutil.copy(source_val_pic, dest_faces_exp_val)
            shutil.copy(source_val_pic, dest_each_val)
        if i < math.floor(num_classes/2):
            if choose == 0:
                os.mkdir(dest_together_val)
            shutil.copy(source_val_pic, dest_together_val)
    i+=1
    #hands have only 100 pictures for train and 25 for validation
print('copied faces')

i = 0
#hands
for class_dir in classes_hands:
    source_train = path_hands + "/train/" + class_dir
    dest_hands_exp_train = path_hands_exp + "/train/h" + class_dir
    dest_together_train = path_together + "/train/h" + class_dir
    dest_each_train = path_each + "/train/h" + class_dir
    source_val = path_hands + "/val/" + class_dir
    dest_hands_exp_val = path_hands_exp + "/val/h" + class_dir
    dest_together_val = path_together + "/val/h" + class_dir
    dest_each_val = path_each + "/val/h" + class_dir
    if i < num_classes:
        shutil.copytree(source_train, dest_hands_exp_train)
        shutil.copytree(source_val, dest_hands_exp_val)
        shutil.copytree(source_train, dest_each_train)
        shutil.copytree(source_val, dest_each_val)
    if i < math.ceil(num_classes/2):
        shutil.copytree(source_train, dest_together_train)
        shutil.copytree(source_val, dest_together_val)
    i+=1
print('copied hands')


parent_dir = "/home/ssd_storage/datasets/students/expertise/Experiment_1"
for exp in os.listdir(parent_dir):
    for s in ["train", "val"]:
        for c in os.listdir(parent_dir +"/" + exp + "/" + s):
            pics = 0
            for pic in os.listdir(parent_dir +"/" + exp + "/" + s + "/" + c):
                pics += 1
            if (pics != 100) & (pics != 25):
                print(pics, " pictures in ", parent_dir +"/" + exp + "/" + s + "/" + c)
                
'''
### delete from faces, keep 189 classes ###
i=0
path = r'/home/ssd_storage/datasets/students/expertise/faces_only_300_189_classes/train'
dirs = os.listdir(path)

for class_dir in dirs:
    if i < num_classes:
        #print("didn`t delete ", path+"/"+class_dir)
        i+=1
        continue
    else:
        #print("deleted ", path+"/"+class_dir)
        shutil.rmtree(path+"/"+class_dir, ignore_errors=False)

path2 = r'/home/ssd_storage/datasets/students/expertise/faces_only_300_189_classes/val'
for class_dir in os.listdir(path2):
    if class_dir in dirs:
        #print("didn`t delete ", path2+"/"+class_dir)
        continue
    else:
        #print("deleted ", path2+"/"+class_dir)
        shutil.rmtree(path2+"/"+class_dir, ignore_errors=False) 
'''