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

[Python 網路連線程式、公開資料串接](https://www.youtube.com/watch?v=sUzR3QVBKIo&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=15)
- Python_14.py

```
＊網路連線＊
<載入模組>
import urllib.request

<下載特定網址資料>
import urllib.request as request
with request.urlopen(網址) as response:
  data = response.read()
print(data)

公開資料：
適合的資料來源：台北市政府公開資料

確認資料格式：  JSON, CSV, 或其他格式
解讀JSON格式： 使用內建的json模組

# 網路連線
import urllib.request as request
src = "https://www.ntu.edu.tw"
with request.urlopen(src) as response:
  # 取得台灣大學網站的原始碼
  # .decode("utf-8") => 顯示中文，不然本來是亂碼
  data = response.read().decode("utf-8")
print(data)
>>> 跑出NTU的html


# 串接、擷取公開資料
# data.taipei
import urllib.request as request
import json
src = "資料網址請複製貼上"
with request.urlopen(src) as response:
  data = json.load(response) # 利用 json 模組處理 json 資料格式
print(data)
>>> 一堆
# 將公司名稱列表出來
clist = data["result"]["results"]
for company in clist:
  print(company["公司名稱"])

# 檔案寫入公司名稱+\n換行符號
clist = data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:
  for company in clist:
    file.write(company["公司名稱"]+"\n")
```

[Python 類別的定義與使用 - Class Attributes](https://www.youtube.com/watch?v=uPKgQ3FoVtY&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=16)
- Python_15.py

[Python 實體物件的建立與使用 - 上篇 - 實體屬性 Instance Attributes ](https://www.youtube.com/watch?v=Lr5N2r1rmtM&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=17)
- Python_16.py

 [Python 實體物件的建立與使用 - 下篇 - 實體方法 - Instance Methods ](https://www.youtube.com/watch?v=MZtTClJ74NU&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=18)
 - Python_17.py

 [Python 網路爬蟲 Web Crawler 基本教學](https://www.youtube.com/watch?v=MZtTClJ74NU&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=18)
 - Python_18.py

 ```
 # 步驟一：抓取 PTT 電影版的網頁原始碼（HTML）。

# 因為是 mac 電腦 ，所以先執行下列兩行程式碼才有辦法抓到網路上資料。

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Step1. 先 import urllib.request 這個內建的封包，以執行接下來的動作，並且取名為 req ，以方便之後操作。

import urllib.request as req
src = "https://www.ptt.cc/bbs/movie/index.html"

# 建立一個 request 物件，附加 Request Headers 的資訊——為了讓我們看起來更像一個真正的使用者。（不然 PTT 不會讓我們抓資料。）

request = req.Request(src, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36"
})

# Step2. 使用 with request.urlopen(網址) 連上網路，並將其重新取名為 response ，最後使用 read() 函數，將網頁結果放入 data 中。

with req.urlopen(request) as response: # 原本 req.urlopen 的括號內會放網址而已，但為了讓我們更像一般使用者，這邊放入剛剛建立的物件。
    data = response.read().decode("utf-8") # 取的網頁的原始碼。並用decode("uyf-8")來翻譯成中文（解碼）。
print(data) # 取得 PTT 電影版ㄉ網頁原始碼。

# 步驟二：解析原始碼，取得每篇文章的標題。

# 使用第三方套件： beautifulsoup4/直接在終端機打 pip install beautifulsoup4
# debug: 因為是用 macbook ，下載 BS4 相對麻煩些：
# Step1. 將 "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.pysudo python get-pip.py" 貼上終端機。
# Step2. 將 "sudo python get-pip.py" 貼上終端機。 此處將會要求輸入電腦密碼。
# Step3. 下載 pip ，將 "sudo easy_install pip" 貼上終端機。
# Step4. 下載 BS4 ，將 "pip install beautifulsoup4" 貼上終端機。
# Step5. 再次下載 BS4 ，將 "pip3 install beautifulsoup4" 貼上終端機。

# 載入 bs4 套件。

import bs4 

# 利用上方載入套件做解析：變數 data 是剛在網路上抓到的資料，丟給 Beautifulsoup，他會幫我們用 html 解析。 並用 root 代表整份網頁。

root = bs4.BeautifulSoup(data, "html.parser") # 利用上方載入套件做解析：變數 data 是剛在網路上抓到的資料，丟給 beautifulsoup4，他會幫我們用 html 解析。 

# 印出網頁，並解透過 "." 來操作要抓取的東西：

print(root.title) # .title ：抓取網頁標題。<title> 以及 </titl3> 分別代表開始與結束。
print(root.title.string) # .title.string ：抓取標籤內的文字。(不會再顯示印出上方時句首句末會出現的 <title> 以及 </titl3>)

# 接下來觀察原始碼，看看我們要找的資料有無特別之處：
# 舉例：在 PTT 電影版中，我廟找的每一則文章的標題，在原始碼中都會先被 <a> 夾住 ，再被 <div> 包住。這就是特色！ 
# 使用 BS4 中強大的套件：
# 下方因為class 是 python 的保留字，程式中不能使用。所以 BeautifulSoup 就選擇使用 class_ 來篩選標籤中的 class 屬性。

# 使用 ".find" 可以幫助我們找到符合一個以下條件的東西：

titles = root.find("div", class_="title") # 尋找 class = "title" 的 div 標籤。
print(titles) # 印出剛剛上面找到的標籤。這裏 titles 代表上面找到的 div 標籤。
print(titles.a.string) # 加上 ".a" 代表我們剛剛找到的那個 div 標籤底下的 <a> 裡面的東西； ".string" 則是抓取前面 "titles.a" 抓到的東西的文字。

# 使用 ".find_all" 可以幫助我們找到「全部」符合以下條件的東西：

titles = root.find_all("div", class_="title") # 尋找所有 class = "title" 的 div 標籤。
print(titles) # 印出剛剛上面找到的標籤。這裏 titles 代表上面找到的 div 標籤。

# 做完上面動作之後，會發現印出來的資料是一個列表的形式，所以我們嘗試使用 for 迴圈將標題資料抓出來：

for title in titles:
    if title.a != None: # 因為可能會有內文被刪除的狀況，如果發生則 div 下就不會有 <a> 標籤。所以先用這個判斷式來判斷此狀況是否發生。
        print(title.a.string) # 如果「不是None」這件事發生，則印出標題（"titles.a" 抓到的東西的文字）。
```

```
pip3 install beautifulsoup4
```

[Python 網路爬蟲 Web Crawler 教學 - Cookie 操作實務](https://www.youtube.com/watch?v=BEA7F9ExiPY&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=20)
 - Python_19.py

