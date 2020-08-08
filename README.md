# Python Basic

## Idea
- 實作環境建置：Jupyter Notebook
- 入門程式語法：基礎語言、物件導向、數學計算
- 函式庫應用、例外處理、多執行緒、資料庫串接

## Video 
[Python 簡介、安裝、與快速開始](https://www.youtube.com/watch?v=wqRlKVRUV_k&t=6s)
- Visual Studio Code
- Python3
- Terminal
- `alias python=/usr/local/bin/python3 `

[Python 變數與資料型態](https://www.youtube.com/watch?v=FMruNSjHOzQ&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=2)
- Python_01.py

[Python 數字、字串的基本運算](https://www.youtube.com/watch?v=bLRa4TZ99aY&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=3)
- Python_02.py

[Python 有序列表的基本運算 - List、Tuple](https://www.youtube.com/watch?v=JLU5oc4_VtA&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=4)
- Python_03.py

[Python 集合、字典的基本運算 - Set、Dictionary](https://www.youtube.com/watch?v=L3-KuGYhw78&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=5)
- Python_04.py

[ Python 流程控制：if 判斷式](https://www.youtube.com/watch?v=A93BsHB-lWo&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=6)
- Python_05.py

[Python 流程控制：迴圈基礎，while 迴圈、for 迴圈 ](https://www.youtube.com/watch?v=szaAeLt_49U&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=7)
- Python_06.py

[Python 流程控制：迴圈進階控制，break、continue、else 命令](https://www.youtube.com/watch?v=yBXlwOmLqZ4&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=8)
- Python_07.py

[Python 函式基礎：定義並呼叫函式](https://www.youtube.com/watch?v=7qKFvUVpQXg)
- Python_08.py

[Python 函式參數詳解：參數預設值、名稱對應、任意長度參數](https://www.youtube.com/watch?v=OOJmhezLd4o&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=10)
- Python_09.py

[Python Module 模組的載入與使用](https://www.youtube.com/watch?v=Et0DjY2cGiE&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=11)
- Python_10.py

[Python Package 封包的設計與使用](https://www.youtube.com/watch?v=GGp-7VHgsKk&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=12)
- Python_11.py

```
<包含模組的資料夾>
用來整理、分類模組程式

＊封包＊
<專案檔案配置>
- 專案檔案夾
  - 主程式.py
  - 封包資料夾
    - __init__.py # 有這個程式的資料夾才會被當成封包資料夾
    - 模組一.py
    - 模組二.py

<專案檔案配置範例>
- 專案檔案夾
  - main.py
  - geometry
    - __init__.py 
    - point.py
    - line.py


＊使用封包＊
<基本語法>
import 封包名稱.模組名稱
import 封包名稱.模組名稱 as 模組別名
```
[Python 文字檔案的讀取和儲存](https://www.youtube.com/watch?v=C4OkV6DrVRs&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=13)
- Python_12.py

```
# 檔案操作流程:1.開啟檔案 2.讀取或寫入 3.關閉檔案
# 第一步開啟檔案:
# 開啟檔案基本語法:
# 檔案物件=open(檔案路徑,mode=開啟模式)
# 開啟模式有三種:讀取模式:r,寫入模式:w,讀寫模式:r+

# 第二步讀取或寫入:
# 讀取全部文字語法:
# 檔案名稱.read()

# 第三步關閉檔案:
# 基本語法:檔案物件.close()


# 範例一:如何開啟中文檔案，並關閉檔案
# 開啟後會在專案資料夾裡產生一個檔案
# 如果想打中文，沒有多打這一行 encoding="utf-8"，會出現下列錯誤資訊:
# UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-2: character maps to <undefined>
file=open("data.txt",mode="w",encoding="utf-8")
file.write("Hello File\nSecond line")
file.write("好棒棒")
file.close()

# 範例二:最佳實務
# with open(檔案路徑,mode=開啟模式) as 檔案物件:
# 以上區塊會自動安全的關閉檔案
with open("data1.txt",mode="w",encoding="utf-8") as file1:
     file1.write("測試中文")
with open("data1.txt", mode="r", encoding="utf-8") as file1:
          data=file1.read()
print(data)

# 範例三:把檔案中的的數字資料，一行一行的讀取出來，並計算總合
# 如果要一次讀取一行，可以用 for 迴圈:
# for 變數 in 檔案物件:
# 從檔案依序讀取每行文字到變數中
with open("data2.txt",mode="w") as file2:
     file2.write("5\n3")
sum=0
with open("data2.txt",mode="r") as file2:
     for line in file2:
          sum+=int(line)
print(sum)

# 範例四: 如何讀取json檔案，並列印json檔案字典裡的資料
# 讀取JSON格式:
# import json
# 讀取到的資料=json.load(檔案物件)
# 寫入JSON格式:
# import json
# json.dump(要寫入的資料,檔案物件)
import json
with open ("config.json",mode="r") as file3:
    data=json.load(file3) #data是一個字典資料
print("name:",data["name"])
print("version:",data["version"])

# 範例五: (承上)如何修改json檔案內的資料: 1.先修改2.再複寫
# 從檔案中讀取 json 資料，放入變數 data 裡面
data["name"]="New Name1"  #修改變數中資料
with open("config.json","w") as file4:
    json.dump(data,file4) #最後，把最新的資料複寫回檔案中
```

[Python 亂數與統計模組](https://www.youtube.com/watch?v=-xwCu6PN1jU&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=14)
- Python_13.py

