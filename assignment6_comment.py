# coding:utf-8
import re
import urllib.request

headers = ("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)


comid = '6202897004748157654'
url = 'http://coral.qq.com/article/1485749985/comment?commentid='+comid+'&reqnum=20&tag=&callback=jQuery1120045970003580648344_1478897723865&_=1478897723870'

for i in range(0,2):
    data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
    patnext = '"last":"(.*?)"'
    nextid = re.compile(patnext).findall(data)[0] #使用［0］将列表转为字符串
    patcom = '"content":"(.*?)",'
    comdata = re.compile(patcom).findall(data)
    for j in range(0,len(comdata)):
        print("---第"+str(i+1)+"页"+str(j+1)+"条评论内容是：")
        print(eval('u"'+comdata[j]+'"'))
        print('\n')
    url = 'http://coral.qq.com/article/1485749985/comment?commentid=' + nextid + '&reqnum=20&tag=&callback=jQuery1120045970003580648344_1478897723865&_=1478897723870'


