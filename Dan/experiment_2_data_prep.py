
import os
import shutil

#also in "Dan/Hands_upright_bg_train" # same as noam's 

class Dataset:

 
    def get_subject_to_pictures(self,verbose):
        picture_formants = ['jpg','png']

        subject_to_pictures = {}
        for root,dirnames,filenames in os.walk(self.raw_path):
            for dir in dirnames:
                subject_dir_path = os.path.join(root,dir)
                for file in os.listdir(subject_dir_path):
                    for format in picture_formants:
                        if file.endswith(format):
                            if dir not in subject_to_pictures.keys():
                                subject_to_pictures[dir] = []
                            subject_to_pictures[dir].append(file)
                # subject_to_pictures[dir] = pictures_cnt
        

        if verbose:
            print(self.name)
            for k,v in subject_to_pictures.items():
                print(f"subject id: {k}, num of pictures: {len(v)}")
            print(f"total num of subjects (individuals, classes): {len(subject_to_pictures.keys())}")
            print(f"total num of pictures : {sum([len(l) for l in subject_to_pictures.values()])}")
            print(f"smallest class (lowest num of pictures in a class) : {min(len(l) for l in subject_to_pictures.values())}")
            print(f"largest class (highest num of pictures in a class) : {max(len(l) for l in subject_to_pictures.values())}")
        
        return subject_to_pictures
    
    def __init__(self,name,raw_path):
        self.raw_path = raw_path
        self.name = name
        self.subject_to_pictures = self.get_subject_to_pictures(verbose= True)

    def get_picture_cnt(self):
        """
        return the total number of pictures of dataset"""
        sum([len(l) for l in self.subject_to_pictures.values()])
    
    def get_class_cnt(self):
        """
        return the total number of classes in dataset"""
        return len(self.subject_to_pictures.keys())
    
    def get_min_class_size(self):
        """
        return the size (items count) of the smallest class of dataset
        """
        return min(len(l) for l in self.subject_to_pictures.values()) 

    def get_min_class_size(self):
        """
        return the size (items count) of the largest class of dataset
        """
        return max(len(l) for l in self.subject_to_pictures.values()) 


hands_path = "/home/ssd_storage/datasets/students/Noam/Hands_upright_bg/train" 
faces_path = "/home/ssd_storage/datasets/expertise/260_cls/faces/train" 

def make_experiment_2_dataset(hands_path,faces_path, dst_dir):    
    hands = Dataset('hands',hands_path)
    faces = Dataset('faces',faces_path)

    # set the size of each class (num of pictures) in final dataset 
    final_dataset_class_size= min(hands.get_min_class_size(),faces.get_min_class_size())
    
    # set the number of classes in final dataset 
    # which will be contributed from each of original datasets
    # for example if faces had 200 classes, and hands had 185,
    # then final class count will be 185 (185 classes from faces, 185 from hands.In total 370)
    final_dataset_class_cnt = min(hands.get_class_cnt(),faces.get_class_cnt())
    
    # create output dirs
    faces_dir_name = "faces"
    hands_dir_name = "hands"
    majority_faces_dirname =  "80%_"+faces_dir_name+"_20%_"+hands_dir_name # 80% faces 20% hands
    majority_hands_dirname = "20%_"+faces_dir_name+"_80%_"+hands_dir_name # 20% faces 80% hands

    majority_faces_dir_path = os.path.join(dst_dir,majority_faces_dirname)
    majority_hands_dir_path = os.path.join(dst_dir,majority_hands_dirname)
    hands_in_majority_hands_dirpath = os.path.join(majority_hands_dir_path,hands_dir_name) # "hands" dir in "20% faces 80% hands" dir
    faces_in_majority_hands_dirpath = os.path.join(majority_hands_dir_path,faces_dir_name) # "faces" dir in "20% faces 80% hands" dir
    hands_in_majority_faces_dirpath = os.path.join(majority_faces_dir_path,hands_dir_name) # "hands" dir in "80% faces 20% hands" dir
    faces_in_majority_faces_dirpath = os.path.join(majority_faces_dir_path,faces_dir_name) # "faces" dir in "20% faces 80% hands" dir
    dirs_to_make = [hands_in_majority_hands_dirpath,hands_in_majority_faces_dirpath, faces_in_majority_hands_dirpath,faces_in_majority_faces_dirpath]
    for dir in dirs_to_make:
        os.makedirs(dir)
    
    # copy data to destination dir until you reach the limit you set (of classes num and size)
    for path in [hands_path, faces_path]:
        for i, subject in enumerate(os.listdir(path)):
            if i == final_dataset_class_cnt: 
                break # reached number of classes limit
            
            if path == hands_path:
                if i < final_dataset_class_cnt//5: 
                    dst_dir_path = hands_in_majority_faces_dirpath # minority - send to 80% faces
                else:
                    dst_dir_path = hands_in_majority_hands_dirpath # majority - send to 80% hands
            
            elif path == faces_path:
                if i < final_dataset_class_cnt//5: 
                    dst_dir_path = faces_in_majority_hands_dirpath # minority - send to 80% hands
                else:
                    dst_dir_path = faces_in_majority_faces_dirpath # majority - send to 80% faces

            subject_src_dir_path = os.path.join(path,subject)
            subject_dst_dir_path = os.path.join(dst_dir_path,subject)
            os.makedirs(subject_dst_dir_path)

            for j,picture in enumerate(os.listdir(subject_src_dir_path)):
                if j == final_dataset_class_size:
                    break # reached number of items in each class limit
                if path == hands_path:
                    picture_format = 'png'
                elif path == faces_path:
                    picture_format = 'jpg'
                if str(picture).endswith(picture_format):
                    shutil.copyfile(os.path.join(subject_src_dir_path,picture), os.path.join(subject_dst_dir_path,picture))
    
    majority_faces = Dataset("mixed", majority_faces_dir_path) 
    majority_hands = Dataset("mixed", majority_hands_dir_path)
dst_dir = os.path.join(os.getcwd(),"Dan/output_dataset")
make_experiment_2_dataset(hands_path,faces_path,dst_dir)
    

# python dir_experiments.py --config_path /home/expertise/Git/FaceRecognitionSeminar/configs/yonatan_and_dan/handsonly.cfg

