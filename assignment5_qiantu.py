
import re
import urllib.request

headers = ("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

pat = 'src.="(.*?).jpg!qt226'
for i in range(0,1):
    url = "http://www.58pic.com/haibao/0/id-"+str(i+1)+".html"
    data = urllib.request.urlopen(url).read().decode("gbk",'ignore')
    print(str(i+1),' ',len(data))
    imagelist = re.compile(pat).findall(data)
    print (imagelist)
    for j in range(0,len(imagelist)):
        thisimg = imagelist[j]
        thisimgurl = thisimg+'_1024.jpg'
        file = "data/imgP" + str(i) + "T" + str(j) + ".jpg"
        urllib.request.urlretrieve(thisimgurl,file)
