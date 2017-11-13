#coding:utf-8
import re
import urllib.request
import urllib.error
import threading

headers = ("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

class One(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,36,2):
            url = "http://www.qiushibaike.com/8hr/page/" + str(i)
            pagedata = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
            pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
            datalist = re.compile(pat, re.S).findall(pagedata)
            for j in range(0, len(datalist)):
                print("第" + str(i) + "页第" + str(j + 1) + "个段子的内容是")
                print(datalist[j])


class Two(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(2,36,2):
            url = "http://www.qiushibaike.com/8hr/page/" + str(i)
            pagedata = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
            pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
            datalist = re.compile(pat, re.S).findall(pagedata)
            for j in range(0, len(datalist)):
                print("第" + str(i) + "页第" + str(j + 1) + "个段子的内容是")
                print(datalist[j])

one = One()
one.start()

two = Two()
two.start()
