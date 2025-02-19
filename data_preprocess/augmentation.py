'''
    23-03-04
    資料擴增
    原始影像480x640
    取中心 x1=175,x2=303, y1=330,y2=458 一張128x128影像
    取平移 6 pixel 上、下、左、右、右上、右下、左上、左下 八張128x128影像
    取傾斜 5度 中心左傾斜、中心右傾斜 兩張128x128影像
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import shutil

photo_name =  "FY_112_0204-1-"
path_origin_data = r"C:\Users\User\Desktop\origin_data_FY\image\0204\1"
path_center = r"C:\Users\User\Desktop\go\center"
path_offset = r"C:\Users\User\Desktop\go\offset"
path_tilt = r"C:\Users\User\Desktop\go\tilt"

# 中心128x128影像座標
x1 = 175
x2 = 303
y1 = 330
y2 = 458

M1 = cv2.getRotationMatrix2D((240,320), 5, 1.0)  # 以中心點取逆時針微傾斜5度
M2 = cv2.getRotationMatrix2D((240,320), -5, 1.0)  # 以中心點取順時針微傾斜5度

imgs = os.listdir(path_origin_data)
for i in range(len(imgs)):
    name = imgs[i]
    os.chdir(path_origin_data)
    img = cv2.imread(name)
    img_m1 = cv2.warpAffine(img, M1, (480,640))
    img_m2 = cv2.warpAffine(img, M2, (480,640))
    
    cut1 = img[y1:y2, x1:x2]            # 中心
    cut2 = img[y1-6:y2-6, x1-6:x2-6]    # 左上
    cut3 = img[y1-6:y2-6, x1:x2]        # 上
    cut4 = img[y1-6:y2-6, x1+6:x2+6]    # 右上
    cut5 = img[y1:y2, x1-6:x2-6]        # 左
    cut6 = img[y1:y2, x1+6:x2+6]        # 右
    cut7 = img[y1+6:y2+6, x1-6:x2-6]    # 左下
    cut8 = img[y1+6:y2+6, x1:x2]        # 下
    cut9 = img[y1+6:y2+6, x1+6:x2+6]    # 右下
    
    cutL = img_m1[y1:y2, x1:x2] 
    cutR = img_m2[y1:y2, x1:x2] 
    
    os.chdir(path_center)
    cv2.imwrite(photo_name+name, cut1)
    
    os.chdir(path_offset)
    cv2.imwrite(photo_name+str(i)+"-6p-2"+".jpg", cut2)
    cv2.imwrite(photo_name+str(i)+"-6p-3"+".jpg", cut3)
    cv2.imwrite(photo_name+str(i)+"-6p-4"+".jpg", cut4)
    cv2.imwrite(photo_name+str(i)+"-6p-5"+".jpg", cut5)
    cv2.imwrite(photo_name+str(i)+"-6p-6"+".jpg", cut6)
    cv2.imwrite(photo_name+str(i)+"-6p-7"+".jpg", cut7)
    cv2.imwrite(photo_name+str(i)+"-6p-8"+".jpg", cut8)
    cv2.imwrite(photo_name+str(i)+"-6p-9"+".jpg", cut9)
    
    os.chdir(path_tilt)
    cv2.imwrite(photo_name+str(i)+"-L5"+".jpg", cutL)
    cv2.imwrite(photo_name+str(i)+"-R5"+".jpg", cutR)

print('finish')
