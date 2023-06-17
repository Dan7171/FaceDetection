import os
import shutil

yonatans_100_100 = "/home/ssd_storage/datasets/students/expertise/Experiment_1/Hands_and_faces_100_each"
src_train_path = os.path.join(yonatans_100_100,'train')
src_val_path = os.path.join(yonatans_100_100,'val')
all_class_names = os.listdir(yonatans_100_100)
for name in all_class_names:
    assert(name.startswith('f') or name.startswith('h'))
dst_year_1 = "/home/ssd_storage/datasets/students/expertise/Experiment_2_fixed/year_1_80_hands"
dst_year_2 = "/home/ssd_storage/datasets/students/expertise/Experiment_2_fixed/year_2_80_faces"

# year 1

year_1_classes = set()
for i in range(len(all_class_names)):
    if size(year_1_classes) == 80:
        break
    if all_class_names[i].startswith('h'):

    # pick hands dir (starts with h) 
    # copy its trin and val dirs to year 1
    # add class name to year 1 set

while(year_1_classes.size() < 100)
    # pick faces dir (starts with f) 
    # copy its trin and val dirs to year 1
    # add class name to year 1 set

# 
year_2_classes = [cl for cl in  ]
for dir


