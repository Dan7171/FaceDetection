import os
import shutil

src_val = "/home/ssd_storage/datasets/students/expertise/Dan/Experiment_2_80_20_20_80/Dan/Experiment_2/Experiment_2_datasets/val/mixed_hands_faces"
dst_val_80_faces = "/home/ssd_storage/datasets/students/expertise/Dan/Experiment_2_80_20_20_80/Dan/Experiment_2/Experiment_2_datasets/part_1_80_faces_20_hands_train_val/val"
dst_val_80_hands = "/home/ssd_storage/datasets/students/expertise/Dan/Experiment_2_80_20_20_80/Dan/Experiment_2/Experiment_2_datasets/part_2_20_faces_80_hands_train_val/val"
train_val_80_faces = "/home/ssd_storage/datasets/students/expertise/Dan/Experiment_2_80_20_20_80/Dan/Experiment_2/Experiment_2_datasets/part_1_80_faces_20_hands_train_val/train"
train_val_80_hands = "/home/ssd_storage/datasets/students/expertise/Dan/Experiment_2_80_20_20_80/Dan/Experiment_2/Experiment_2_datasets/part_2_20_faces_80_hands_train_val/train"

for dirname in os.listdir(train_val_80_faces):
    shutil.copytree(os.path.join(train_val_80_faces,dirname), os.path.join(dst_val_80_faces,dirname))
for dirname in os.listdir(train_val_80_hands):
    shutil.copytree(os.path.join(train_val_80_hands,dirname), os.path.join(dst_val_80_hands,dirname))
