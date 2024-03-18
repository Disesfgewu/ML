## 基本 Python 影像處理模組

###### 在本專案中會使用到的所有在以往社課中沒教過的 Python 模組與函式公式

### Python 開檔關檔

#### 讀取文字檔案

- file = open( "文件路徑" , 使用模式 )
  - 模式：
    - 1. 'r'：純讀
    - 2. 'w'：寫入

#### 寫入文字

- file.write( "要寫入的內容" )

#### 檔案關閉

- file.close()

### Pillow 影像圖片處理模組

- 為 Python 的圖片處理模組

- from PIL import Image

#### 開啟

- 圖片變數 = Image.open( "圖片路徑" )

#### 儲存

- 圖片變數.save( "檔案路徑`\\`名稱" ) # 可以以與原圖不同之格式儲存檔案

#### 更改圖片大小

- 圖片變數.resize( ( 圖片寬度 , 圖片高度 ) , 品質旗標 )
- 品質旗標： Image.ANTIALIAS （正常品質）

#### 圖片灰階處理

- 圖片變數.convert( 'L' )

### glob 查找匹配檔案

- import glob

#### 讀取在資料夾中所有某個檔案格式的資料

- 資料 ( List 型態 ) = glob.glob( "path/*.檔案格式")

### os 系統模組

- import os

#### 資料夾建立

- os.mkdir( "資料夾名稱" )

#### 判斷資料夾是否存在

- os.path.isdir( "資料夾名稱" )
  - 若無 return False
  - 反之 return True
  
#### 刪除檔案

- os.remove( "檔名" )

#### 得出基底檔案名

- 檔案名 = os.path.basename( "檔案路徑" )

### shutil 模組

- import shutil

#### 刪除檔案夾與其資料

- shutil.rmtree( "資料夾名稱" )

### sleep 函式

- from time import sleep

#### 暫停程式 n 毫秒

- sleep( n )

### OpenCV 影像偵測與處理模組

- pip install opencv-python

- import cv2

#### 輸入影像

- 圖形變數 = cv2.imread( 檔案路徑 )

#### 導入 Haar 特徵模型

- 模型變數 = cv2.CascadeClassifier( 模型路徑 )

#### 偵測物件

- 偵測變數 = 模型變數.detectMultiScale( 圖片 , minSize = ( 寬 , 高 ) , scaleFactor = 放大比例 , minNeighbors = 最小相鄰數 )
  - 參數說明：
  - 1. minSize : 檢測最小矩形大小，通常為偵測物件的長及寬
  - 2. scaleFactor : 矩形放大比例，當找不到物件時會將矩形放大再次尋找，通常為 1.1 ~ 1.5
  - 3. minNeighbors : 通常相鄰的檢測物件都會符合物件偵測的模型，為防止框選物件太多，可將此值提高通常為 4 ~ 10 

- 偵測變數為二維串列，包括每個框選資料的左上角 x , y 座標及寬度與高度
  - detector = [ [x , y , 寬度 , 高度] ..... ]

#### 建立視窗顯示影像

- cv2.namedWindow( 視窗名稱[ , 視窗旗標 ] ) # 建立視窗
- cv2.destroyWindow( 視窗名稱 ) # 關閉
- cv2.destroyAllWindows() # 關閉全部
- 影像變數 = cv2.imread( 影像檔案路徑[ , 讀取旗標 ] ) 
  - 讀取旗標：
    - 0  = 灰階
    - 1  = 彩色（預設）
    - -1 = 原始模式
- cv2.imshow( 視窗名稱 , 影像變數 ) # 顯示影像
- cv2.waitKey(n) # 等待 n 毫秒

#### 儲存影像

- cv2.imwrite( 存檔路徑 , 影像變數[ , [ int( 存檔旗標 ) , 值 ] ] )
  - 例：cv2.imwrite( "img.jpg" , img , [ int( cv2.IMWRITE_JPEG_QUALITY ) , 70 ] )

#### 繪圖

##### 顏色

- BGR 非 RGB

##### Line

- cv2.line( 畫布 , 起始點 , 結束點 , 顏色 , 寬度 )

##### Rectangle

- cv2.rectangle( 畫布 , 起始點 , 結束點 , 顏色 , 寬度 )

##### Circle

- cv2.circle( 畫布 , 圓心 , 半徑 , 顏色 , 寬度 )

##### Polylines

- cv2.polylines( 畫布 , 點座標串列 , 封閉 , 顏色 , 寬度 )
    - 點座標串列： numpy 物件 
    - numpy.array( [ [ 第一個點 ] , [ 第二個點 ] ... ] , numpy.int32 )
    - 封閉：True 為 封閉 False 為 開口

##### Text

-  cv2.putText( 畫布 , 文字 , 位置 , 字體 , 字體尺寸 , 顏色 , 文字粗細 )