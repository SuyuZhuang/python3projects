# coding:utf8
# 第一次作业,逆向输出乘法口诀
for i in range(9,0,-1):
    for j in range (i,0,-1):
        print (str(i)+"*"+str(j)+"="+str(i*j)+" ",end="")
    print()
