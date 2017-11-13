# coding:utf-8
import re
import urllib.request

keyname = "连衣裙"
key = urllib.request.quote(keyname)

headers = ("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

for i in range(0,2):
    url='https://s.taobao.com/list?q='+str(key)+'&cat=16&style=grid&seller_type=taobao&spm=a219r.lm874.1000187.1&bcoffset=12&s='+str(i*60)
    data = urllib.request.urlopen(url).read().decode("utf-8",'ignore')
    print(len(data))
    pat = '"picUrl":"//(.*?)"'
    imagelist = re.compile(pat).findall(data)
    for j in range(0,len(imagelist)):
        thisimg = imagelist[j]
        thisimgurl = "http://" + thisimg
        file = "data/imgP"+ str(i)+"T"+str(j)+".jpg"
        urllib.request.urlretrieve(thisimgurl,file)


