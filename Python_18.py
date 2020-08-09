import urllib.request as req

src = 'https://www.ptt.cc/bbs/movie/index.html'
request = req.Request(src, headers={'User-Agent': 'Mozilla/5.0'})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

#print(data)

import bs4 

root = bs4.BeautifulSoup(data, "html.parser") 
print(root.title)
print(root.title.string) 

titles = root.find("div", class_="title") 
print(titles) 
print(titles.a.string)

titles = root.find_all("div", class_="title")
#print(titles) 

for title in titles:
    if title.a != None: 
        print(title.a.string)