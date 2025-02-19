'''
    2024.08.29
    將可見光影像切割成9片
    取其中5片區域，計算統計數值
'''
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
from scipy import stats
import pandas as pd
import csv
import copy

def get_values(img):
    data_array=[]
    b, g, r = cv2.split(img)
    #hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #h, s, v = cv2.split(hsv)
    
    ###[y1:y2, x1:x2]
    cut_1 = img[0:70, 0:50]   # ROI左上50x70
    cut_2 = img[70:120, 0:50]   # ROI左50x50
    cut_3 = img[70:120, 50:180]   # ROI中間130x50
    cut_4 = img[70:120, 180:220]   # ROI右40x50
    cut_5 = img[0:70, 180:220]   # ROI右上40x70
    
    img_list = [cut_1, cut_2, cut_3, cut_4, cut_5]
    for i in range(len(img_list)):
        image = img_list[i]
        
        mean_ = np.mean(image)
        mean_ = math.trunc(mean_) #取整數
        array_ = image.flatten('C')
        mode_ = stats.mode(array_)[0]
        mode_ = int(mode_) # 陣列轉數字
        median_ = np.median(image)
        range_ = np.max(image) - np.min(image)
        q1_ = np.percentile(image,25)
        q3_ = np.percentile(image,75)
        quantile_ = np.percentile(image,75)-np.percentile(image,25)
        std_ = np.std(image)
        std_ = round(std_, 2) # 取到小數點後兩位
        skewness_ = np.mean(abs(image - image.mean())**3)
        thirdMoment_ = skewness_**(1./3)
        thirdMoment_ = round(thirdMoment_, 2)
    
        data_array.extend([ mean_,mode_,median_,range_,q1_,q3_,quantile_,std_,thirdMoment_])
    
    return data_array


imgs_path = r"C:\Users\User\Desktop\goo\color_G"
f = open(r'C:\Users\User\Desktop\goo\G.csv', 'w', newline='')
imgs = os.listdir(imgs_path)

array = []
for i in range(len(imgs)):
    filename = imgs[i]
    img = cv2.imread(imgs_path + '\\'+ filename)
    data = get_values(img)
    data.insert(0, filename)
    array.append(data)
    
# 匯出 csv檔
with f:
    writer = csv.writer(f)
    writer.writerow(['file_name',
        'c1_mean','c1_mode','c1_median','c1_range','c1_q1','c1_q3','c1_quantile','c1_std','c1_skewness',
        'c2_mean','c2_mode','c2_median','c2_range','c2_q1','c2_q3','c2_quantile','c2_std','c2_skewness',
        'c3_mean','c3_mode','c3_median','c3_range','c3_q1','c3_q3','c3_quantile','c3_std','c3_skewness',
        'c4_mean','c4_mode','c4_median','c4_range','c4_q1','c4_q3','c4_quantile','c4_std','c4_skewness',
        'c5_mean','c5_mode','c5_median','c5_range','c5_q1','c5_q3','c5_quantile','c5_std','c5_skewness'])
    writer.writerows(array)
