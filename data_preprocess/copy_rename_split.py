'''
	2024-06-04 複製+重新命名+影像切割
    四合一影像拆開並分類，資料前處理
'''

import os
import shutil
import cv2

# 命名規則、類別
img_name = 'output2'
#classname = 'good'

# 資料讀取路徑
path_data = r"C:\Users\User\Desktop\go"
files = os.listdir(path_data)

# 建立儲存路徑
path_save_ori = r"C:\Users\User\Desktop\goo\origin"
path_save_b = r"C:\Users\User\Desktop\goo\color_B"
path_save_g = r"C:\Users\User\Desktop\goo\color_G"
path_save_r = r"C:\Users\User\Desktop\goo\color_R"

# 建立資料夾
#os.mkdir(r"C:\Users\User\Desktop\rawdata0808" +"\\"+ str(img_name))
os.mkdir(path_save_ori)
os.mkdir(path_save_b)
os.mkdir(path_save_g)
os.mkdir(path_save_r)

# 原始影像的X、Y座標
ori_x1 = 0
ori_x2 = 480
ori_y1 = 0
ori_y2 = 640

for i in range(len(files)):
    
    name = files[i]
    img = cv2.imread(path_data+"\\"+name)
    
    img_ori = img[ori_y1:ori_y2, ori_x1:ori_x2]
    img_b = img[ori_y1:ori_y2, ori_x1+480:ori_x2+480]
    img_g = img[ori_y1+640:ori_y2+640, ori_x1:ori_x2]
    img_r = img[ori_y1+640:ori_y2+640, ori_x1+480:ori_x2+480]
    
    # 儲存影像到各類資料夾
    cv2.imwrite(path_save_ori+"\\"+"ori_"+img_name+"-"+name, img_ori)
    cv2.imwrite(path_save_b+"\\"+"b_"+img_name+"-"+name, img_b)
    cv2.imwrite(path_save_g+"\\"+"g_"+img_name+"-"+name, img_g)
    cv2.imwrite(path_save_r+"\\"+"r_"+img_name+"-"+name, img_r)
    
print('finish')
