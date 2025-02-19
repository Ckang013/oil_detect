'''
    2023/10/31 圖片縮放成 0.5倍
'''

import os
import cv2
import numpy as np

path_1 = r"C:\Users\User\Desktop\box_dev\develop-RPi_normal_cam_180ang\ModelTrainV3\model3-1_4c\dataset\water\origin"
path_2 = r"C:\Users\User\Desktop\box_dev\develop-RPi_normal_cam_180ang\ModelTrainV3\model3-2_4c\dataset\water\origin"

imgs = os.listdir(path_1)
for i in range(len(imgs)):
    name = imgs[i]
    os.chdir(path_1)
    img = cv2.imread(name)
    
    re_img = cv2.resize(img, (240,320), interpolation=cv2.INTER_AREA) # 縮小圖片使用INTER_AREA效果較好
    
    os.chdir(path_2)
    cv2.imwrite(name, re_img)

print('finish')
