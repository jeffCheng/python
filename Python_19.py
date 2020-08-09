import urllib.request as req
import bs4
import re
def getcode(url):
    request=req.Request(url,headers={
        "cookie":"over18=1",
        'User-Agent': 'Mozilla/5.0'
    })
    with req.urlopen(request) as response:
        code=response.read().decode("utf-8")
    return code
def getarticle(dom):
    soup=bs4.BeautifulSoup(dom,"html.parser")
    divs=soup.find_all("div",class_="r-ent")
    articles=[]
    for d in divs:
        if d.find("div",class_="nrec"):
            pushnum=d.find("div",class_="nrec").string
        if d.find("div",class_="author"):
            author=d.find("div",class_="author").string
        if d.find("div",class_="date"):
            date=d.find("div",class_="date").string
        if d.find("a"):
            title=d.find("a").string
            href=d.find("a")["href"]
            articles.append({
                "title":title,
                "pushnum":pushnum,
                "author":author,
                "date":date,
                "href":"http://www.ptt.cc"+href
            })
    nextlink="http://www.ptt.cc"+soup.find("a",string="‹ 上頁")["href"]
    return articles,nextlink
def getimg(dom):
    soup=bs4.BeautifulSoup(dom,"html.parser")
    links=soup.find(id="main-content").find_all("a")
    img=[]
    for link in links:
        if re.match(r'^https?://(i.)?(m.)?imgur.com',link["href"]):
            img.append(link["href"])
    return img
pageurl="https://www.ptt.cc/bbs/Beauty/index.html"
count=0
while count<5:
    code=getcode(pageurl)
    result=getarticle(code)
    pageurl=result[1]
    for i in result[0]:
        aurl=i["href"]
        codeimg=getcode(aurl)
        img=getimg(codeimg)
        print(img)
    count+=1