import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import pickle
import xgboost

## 合格
data_good_B = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/color_B/good_all.csv")
data_good_B.drop(columns=['file_name'], inplace=True)
data_good_B.columns = 'B_' + data_good_B.columns
data_good_G = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/color_G/good_all.csv")
data_good_G.drop(columns=['file_name'], inplace=True)
data_good_G.columns = 'G_' + data_good_G.columns
data_good_IR = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/IR940/good_all.csv")
data_good_IR.drop(columns=['file_name'], inplace=True)
data_good_IR.columns = 'IR_' + data_good_IR.columns
data_good = pd.concat([data_good_B, data_good_G, data_good_IR], axis=1)

## 不合格
data_bad_water_B = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/color_B/bad_water_all.csv")
data_bad_water_B.drop(columns=['file_name'], inplace=True)
data_bad_water_B.columns = 'B_' + data_bad_water_B.columns
data_bad_water_G = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/color_G/bad_water_all.csv")
data_bad_water_G.drop(columns=['file_name'], inplace=True)
data_bad_water_G.columns = 'G_' + data_bad_water_G.columns
data_bad_water_IR = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/IR940/bad_water_all.csv")
data_bad_water_IR.drop(columns=['file_name'], inplace=True)
data_bad_water_IR.columns = 'IR_' + data_bad_water_IR.columns
data_bad_water = pd.concat([data_bad_water_B, data_bad_water_G, data_bad_water_IR], axis=1)
data_bad_impur_B = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/color_B/bad_impur.csv")
data_bad_impur_B.drop(columns=['file_name'], inplace=True)
data_bad_impur_B.columns = 'B_' + data_bad_impur_B.columns
data_bad_impur_G = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/color_G/bad_impur.csv")
data_bad_impur_G.drop(columns=['file_name'], inplace=True)
data_bad_impur_G.columns = 'G_' + data_bad_impur_G.columns
data_bad_impur_IR = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/IR940/bad_impur.csv")
data_bad_impur_IR.drop(columns=['file_name'], inplace=True)
data_bad_impur_IR.columns = 'IR_' + data_bad_impur_IR.columns
data_bad_impur = pd.concat([data_bad_impur_B, data_bad_impur_G, data_bad_impur_IR], axis=1)
data_bad = pd.concat([data_bad_water, data_bad_impur], ignore_index=True)

## 非油品
data_non_B = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/color_B/non_all.csv")
data_non_B.drop(columns=['file_name'], inplace=True)
data_non_B.columns = 'B_' + data_non_B.columns
data_non_G = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/color_G/non_all.csv")
data_non_G.drop(columns=['file_name'], inplace=True)
data_non_G.columns = 'G_' + data_non_G.columns
data_non_IR = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/IR940/non_all.csv")
data_non_IR.drop(columns=['file_name'], inplace=True)
data_non_IR.columns = 'IR_' + data_non_IR.columns
data_non = pd.concat([data_non_B, data_non_G, data_non_IR], axis=1)

## 空抽
data_air_B = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/color_B/air.csv")
data_air_B.drop(columns=['file_name'], inplace=True)
data_air_B.columns = 'B_' + data_air_B.columns
data_air_G = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/color_G/air.csv")
data_air_G.drop(columns=['file_name'], inplace=True)
data_air_G.columns = 'G_' + data_air_G.columns
data_air_IR = pd.read_csv("/content/gdrive/My Drive/檢驗盒/模型訓練V3/模型3-2/IR940/air.csv")
data_air_IR.drop(columns=['file_name'], inplace=True)
data_air_IR.columns = 'IR_' + data_air_IR.columns
data_air = pd.concat([data_air_B, data_air_G, data_air_IR], axis=1)

data_good.insert(loc= len(data_good.columns), column='class', value=0)
data_bad.insert(loc= len(data_bad.columns), column='class', value=1)
data_non.insert(loc= len(data_non.columns), column='class', value=2)
data_air.insert(loc= len(data_air.columns), column='class', value=3)

dataframe = pd.concat([data_good, data_bad, data_non, data_air], ignore_index=True)
features = dataframe.iloc[:, :-1]
label = dataframe.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(features, label, test_size=0.25, random_state=20)
print("train data: ", x_train.shape)
print("test data: ", x_test.shape)
print("train label: ", y_train.shape)
print("test label: ", y_test.shape)

xgb = XGBClassifier(booster='gbtree', max_depth=3, learning_rate=0.1, n_estimators=100, random_state=40)
xgb.fit(x_train, y_train, eval_set=[(x_test, y_test)], verbose = 2)
train_accuracy = xgb.score(x_train, y_train)
test_accuracy = xgb.score(x_test, y_test)
print('train accuracy: ', train_accuracy)
print('test accuracy: ', test_accuracy)

train_pred = xgb.predict(x_train)
mse = metrics.mean_squared_error(y_train, train_pred)
print('訓練集 MSE: ', mse)

test_pred = xgb.predict(x_test)
mse = metrics.mean_squared_error(y_test, test_pred)
print('測試集 MSE: ', mse)

cm = confusion_matrix(y_test, test_pred)
print(cm)

xgboost.plot_importance(xgb, max_num_features=10)
plt.show()

pickle.dump(xgb, open("Model3_2_a.sav", "wb"))
