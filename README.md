# oil_detect
油品檢測裝置，檢測流過玻璃管的液體是合格油品、不合格油品、非油品哪一個，再根據結果讓機台做出應對的動作

硬體設備:
1. 樹莓派
2. Pi camera
3. IR camera
4. sensor (led、ir led)

模型訓練:
1. CNN + MobileNet
2. Transfer Learning + XGBoost

## 資料蒐集
### 光譜數據 Spectral data
起初的做法是用 Arduino 結合具有 I2C 功能的光譜感測器和顏色感測器，光譜感測器給出的數據是波長介於380~940之間共6個channel的數據，而顏色感測器則是RGB三個數據，將這些設備組合起來，做成一個檢測與資料蒐集裝置。
資料蒐集是模型訓練中最花時間也最要求的部分，當一個模型餵進去訓練的資料是錯誤或有異常的，產出的結果就會很糟沒有參考性，也不能部署上線，而液體資料的蒐集又更難，相較於固體的資料，液體有變質的問題，因此同一筆樣本是沒有辦法做到二次蒐集的。

![螢幕擷取畫面 2025-02-19 164110](https://github.com/user-attachments/assets/dee1b468-4dec-4804-b52f-cbac47410f18)

### 影像資料 Image data
因為發現光譜數據要做到偵測效果不是很好，能力有限，因此改為使用 Raspberry Pi 結合 camera 的方式，透過影像資料來去做偵測，就開始搭配各種光源，針對各種不同的液體做資料蒐集

![圖片1](https://github.com/user-attachments/assets/5b42dedd-7a47-4169-843f-914ddcaccd78)
![圖片2](https://github.com/user-attachments/assets/1d3ac22a-2411-4ca2-86ab-81bfe6e62a54)

## 資料前處理
蒐集完的資料與數據，都會需要一一檢查與清洗，在蒐集的過程中可能會有設備突然異常、led異常、資料失真...等等的情況發生，所以需要去丟掉這些不能用的資料，影像資料有使用了兩種不同的模型去實作，一個是卷積神經網路(CNN)，另一個是遷移學習(Transfer Learning)
### 取出ROI
因為有了影像資料量太大，辨識太花時間這個經驗，所以就想出了將影像作切割和轉換，只取出某一小部分的ROI，來做訓練。
### 影像轉數據
取出的影像資料要轉換成什麼資料，我剛好在網路上看到了一篇 Color Moment 的文章，因此才有了想法

## 數據分析
有針對所有蒐集到的資料，不論是光譜數據還是影像所轉出來的數據，做一些統計分析
### 光譜數據分析

### 影像資料分析

## 模型訓練
### 捲積神經網路(CNN)
一開始選擇這個方式，是因為蒐集到的資料是影像的形式，然後也有一定的量，就決定試試這個方式，也因為做辨識的資料是影像，資料量太大造成每次辨識的時間太長，所以有額外加上google的AI運算棒來加速，辨識速度從一張影像100ms 提高到10ms，但最後辨識結果不盡人意。
現在回想起來當初這個階段的時候，所規劃的光源配置沒有很好，因此資料間彼此的差異性沒有很突出，辨識上靠的主要還是液體之間顏色的差異性，而捲積神經網路比較沒辦法處理這個，捲積神經網路強的部份是找出影像之間彼此形狀上的特徵差異，所以後來棄用了這個方式。
### 遷移學習(Transfer Learning)
當具有足夠的資料量時，可以用既有的模型來微調，既有的模型的好處就是已經經過了很大量的資料訓練，因此模型的權重是很好的，如果調用過來再針對自己的資料去做微調，會有不錯的成果，因此我這裡使用 XGBooost模型來微調這些蒐集到的資料

## 模型驗證與部署
