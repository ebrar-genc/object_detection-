import os

os.system("python yolov5-master/detect.py --weights best.pt --img 640 --conf 0.25 --source 0 --save-crop --name exp")