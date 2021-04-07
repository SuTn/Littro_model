# 修改文件名中的（） 不能使用的情况
import os
path= "G:/Desktopsnew/2021-03-08/xml"
fileList=os.listdir(path)
import re 
n=0
for i in fileList:
   
    
    #设置旧文件名（就是路径+文件名）
    oldname=path+ "/" + i   # os.sep添加系统分隔符
    print(oldname)

    j = i.replace(" ","").replace("(","_").replace(")","")
    print(j)
    
    #设置新文件名
    newname=path + "/" + j
    
    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    print(oldname,'======>',newname)
    
    # n+=1
