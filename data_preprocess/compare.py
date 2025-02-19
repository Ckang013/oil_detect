'''
    2024-01-17 兩張資料比對
'''

import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread(r"C:\Users\User\Desktop\goo\25.jpg")
img2 = cv2.imread(r"C:\Users\User\Desktop\go\25.jpg")

# 比較方式一
'''
array_1 = np.array(img1)
array_2 = np.array(img2)

difference_1 = np.setdiff1d(array_1, array_2)
difference_2 = np.setdiff1d(array_2, array_1)

list_difference = np.concatenate((difference_1, difference_2))
print(list(list_difference))
'''
# --------------------------------

# 比較方式二
'''
difference_1 = set(img1.tolist()).difference(set(img2.tolist()))
difference_2 = set(img2.tolist()).difference(set(img1.tolist()))

list_difference = list(difference_1.union(difference_2))
print(list_difference)
'''

print(img1[100][112])
print(img2[100][112])


print("end")
