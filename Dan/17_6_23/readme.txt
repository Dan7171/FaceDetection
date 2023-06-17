משימות:
1. לחכות לעידן שיסדר את השרת כי אני חוטף קונקשן ריפיוזד ארור
2. להריץ את הסקריפט של נועם /home/expertise/Git/FaceRecognitionSeminar/Dan/calc_mean_std.py.py
על שני הפאת'ים הבאים ולעדכן בקונפיגים:
train_img_root = "/home/ssd_storage/datasets/students/expertise/Dan/Experiment_2_datasets/year_1_20_faces_80_hands_train_val_100_classes/train/"
train_img_root = "/home/ssd_storage/datasets/students/expertise/Dan/Experiment_2_datasets/year_2_80_faces_20_hands_train_val_100_classes/train/"

3. אחרי ש1 ו3 קרו, לאמן על הקונפיג של השנה ה1 ואז של השנה השנייה. הם כבר מוכנים- מופיע למטה







**** commands:
# environment:
conda activate expertise_fixed 
# gpu status:
 nvidia-smi
 


*** UPDATED LOCATIONS ***


*** configs:

/home/expertise/Git/FaceRecognitionSeminar/Dan/17_6_23
*** Data setes

 
Data sets 100 classes per config (new- as same as noam's):

/home/ssd_storage/datasets/students/expertise/Experiment_2_fixed

*** Training


year 1:
Train first on 80 hands

nohup python /home/expertise/Git/FaceRecognitionSeminar/dir_experiments.py --config_path /home/expertise/Git/FaceRecognitionSeminar/Dan/17_6_23/20_faces_80_hands_year_1.cfg


yaer 2: (epoch starts from end of year 1)
Train first on 80 faces  

nohup python /home/expertise/Git/FaceRecognitionSeminar/dir_experiments.py --config_path /home/expertise/Git/FaceRecognitionSeminar/Dan/17_6_23/80_faces_20_hands_year_2.cfg


nohup python /home/expertise/Git/FaceRecognitionSeminar/dir_experiments.py --config_path /home/expertise/Git/FaceRecognitionSeminar/Dan/9_6_23/configs_9_6_23/20_faces_80_hands.cfg > /home/expertise/Git/FaceRecognitionSeminar/Dan/14_6_23/run_results/year_2.txt
