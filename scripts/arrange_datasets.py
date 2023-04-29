import os
import shutil

### delete classes out of train and val in "hands_upright" ###
handspath = r'/home/ssd_storage/datasets/students/expertise/Hands_upright'
for filename in os.listdir(handspath):
    if filename != "train" and filename != "val":
        print("deleted ", handspath+"/"+filename)
        shutil.rmtree(handspath+"/"+filename, ignore_errors=False)
'''
### delete from faces, keep 189 classes ###
i=0
path = r'/home/ssd_storage/datasets/students/expertise/faces_only_300_189_classes/train'
dirs = os.listdir(path)
for filename in dirs:
    if i < 189:
        print("didn`t delete ", path+"/"+filename)
        i+=1
        continue
    else:
        print("deleted ", path+"/"+filename)
        shutil.rmtree(path+"/"+filename, ignore_errors=False)

path2 = r'/home/ssd_storage/datasets/students/expertise/faces_only_300_189_classes/val'
for filename in os.listdir(path2):
    if filename in dirs:
        print("didn`t delete ", path2+"/"+filename)
        continue
    else:
        print("deleted ", path2+"/"+filename)
        shutil.rmtree(path2+"/"+filename, ignore_errors=False) 
'''