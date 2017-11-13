# coding:utf-8
# 第三次作业，从豆瓣网站https://read.douban.com/provider/all中，使用正则表达式将所有出版社的名字提取出来，存入文件

import urllib.request
import re

# 观察页面代码，得知出版社名字所在的模式<div class="name">博集天卷</div>
pat='<div class="name">(.*?)</div>'
data=urllib.request.urlopen("https://read.douban.com/provider/all").read().decode('utf-8')
result = re.compile(pat).findall(str(data))

# 将结果写入文件, 由于直接一个list输出太长，改为每排输出8个出版社名
f = open('DBproviders.txt','w')
i = 0
for name in result:
    if (i<8):
        f.write(name)
        f.write(", ")
        i+=1
    else:
        i=1
        f.write('\n')
        f.write(name)
        f.write(", ")
f.close
