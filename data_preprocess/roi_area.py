'''
    21.10.08
    畫出玻璃管影像中間正方形的ROI
'''
import cv2
import os

img = cv2.imread(r"C:\Users\User\Desktop\Valid\model3-2-b\out1\0906p\5\20.jpg")
#save_dir = r"C:\Users\User\Desktop"
font = cv2.FONT_HERSHEY_SIMPLEX

# 影像水平翻轉
#img = cv2.flip(img, 1)

x1 = 610    # 空管led位置 中心食人魚230，右側燈條330，紅外光230
x2 = 830    # 空管led位置 中心食人魚250，右側燈條350，紅外光250
y1 = 300    # 空管led位置 中心食人魚380，右側燈條160，紅外光420
y2 = 520    # 空管led位置 中心食人魚400，右側燈條180，紅外光440

img_cp = img.copy()
area = img_cp[y1:y2, x1:x2]

cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)
#cv2.putText(img, 'x1='+str(x1), (220,50), font, 1, (255,255,0), 2)
#cv2.putText(img, 'y1='+str(y1), (220,80), font, 1, (255,255,0), 2)
#cv2.putText(img, 'x2='+str(x2), (320,440), font, 1, (255,255,0), 2)
#cv2.putText(img, 'y2='+str(y2), (320,470), font, 1, (255,255,0), 2)

cv2.imshow('img', img)
cv2.imshow('area', area)

#os.chdir(save_dir)
#cv2.imwrite('k.jpg', img)

#print(area)

cv2.waitKey(0)
