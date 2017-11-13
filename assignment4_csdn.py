# coding:utf-8
# 需求：爬取CSDN博客http://blog.csdn.net/ 首页显示的所有文章，每个文章内容单独生成一个本地网页存到本地中

import urllib.request
import re

url = "http://blog.csdn.net/"
# 浏览器伪装
headers = ("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
# 爬取首页所有文章的url，存入到allurl 列表中
data = opener.open(url).read()
data2 = data.decode("utf-8","ignore")

pat = 'href="(http://blog.csdn.net/.*?/article/details/.*?)"  target="_blank">'
allurl = re.compile(pat).findall(data2)

# 循环爬取所有文章的url到本地
for i in range(0,len(allurl)):
    try:
        print ("第"+str(i)+"次爬取")
        thisurl = allurl[i]  #current url
        file = "csdnblogs/"+str(i)+".html"
        blog = opener.open(thisurl).read()
        fh = open(file,"wb")
        fh.write(blog)
        fh.close()
        print ("-----成功爬取-----")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
