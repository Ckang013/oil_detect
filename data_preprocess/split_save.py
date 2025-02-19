'''
    2024.07.16
    資料前處理(切割) -->取出ROI
    路徑下的多個資料夾同時處理，需注意要修改切割位置(IR，Pi兩個camera不同)
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import shutil

#切割的資料路徑
path_1 = r"C:\Users\User\Desktop\split\IR_940\bad_water_2"

files = os.listdir(path_1)
for i in range(len(files)):
    file = files[i]
    img_path = path_1+"\\"+str(files[i])
    
    imgs = os.listdir(img_path)
    os.chdir(img_path)
    for j in range(len(imgs)):
        name = imgs[j]
        img = cv2.imread(name)
    
        #cut = img[300:580, 140:350]     # 從 480x640 去切 210x280，ModelV3的pi_cam資料切割
        cut = img[400:560, 130:310]     # 從 480x640 去切 180x160，ModelV3的CM_cam資料切割
    
        cv2.imwrite(name, cut)

print('finish')
