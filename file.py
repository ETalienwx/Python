__author__ = 'asus'
# f = open('d:test.txt','r')
# a=f.readlines()
# print(a)
# f.close()
#
# f=open("d:test.txt",'r')
# a=f.readline()
# print(a)
# f.close()
#
# f=open('d:test.txt','r')
# for a in f:
#     print(a)
# f.close()
#
# f=open('d:test.txt','w')
# f.write("hello world")
# f.close()

#统计文件中每个单词的个数
# f=open('d:test.txt','r')
# word_dict={}
# for word in f:
#     #word=word[0:-1]
#     word=word.strip()
#     if word in word_dict:
#         word_dict[word]+=1
#     else:
#         word_dict[word]=1
# print(word_dict)
# f.close()

#句柄（遥控器）
f=open('d:test.txt','r')
print(type(f))

#不及时关闭，可能会导致文件资源泄漏
f.close()

#关闭文件要特别小心
#1.返回的情况
def fun():
    x=0
    y=0
    if x==0:
        f.close()
        return
    if y==0:
        f.close()
        return
    f.close()
#2.列表访问越界情况
def fun():
    a=[1,2,3,4]
    a[100]
    f.close()

#所以python里提供了with语句
#with保证close可以被调用到
#with语句中as得到的对象称为“上下文管理器”
def fun():
    with open("d:test.txt","r") as f:
        #做各种文件操作
        x=0
        if x==0:
            return

#在解释器上查看内建函数
dir(__builtins__)

help(open)
#文件打开的几种方式
#r只读
#w清空文件写
#a文件不清空在后面写
#x有创建的功能
#b二进制方式打开
#t文本类型打开
#w+不清空在后面写

# #文件如果是中文的,以下代码会打印错误
# with open("d:test.txt","r") as f:
#     for line in f:
#         print(line,end='')
# #文件存储有一种编码方式（gbk 或者 utf8）
# #代码读取文件也有一种编码方式（unicode）
# #两种方法得对应上
# with open("d:test.txt","r",encoding="gbk") as f:
#     for line in f:
#         print(line,end='')


#把所有行读到列表中去,读到内存中去，适合读小文件
print(f.readlines())
#for循环读取,频繁的读取，会导致效率变慢,但是节省空间
for line in f:
    print(line)

#写文件
f.write()

#文件路径的操作
import os.path
my_path='d:aaa/bbb/ccc.txt'
print(os.path.basename(my_path))#ccc.txt
print(os.path.dirname(my_path))#d:aaa/bbb
print(os.psth.split(my_path))#('d:aaa/bbb','ccc.txt')返回一个元组
print(os.psth.splitext(my_path))#('d:aaa/bbb/ccc','.txt')返回一个元组

print(os.path.exists(my_path))#查看文件是否存在，不存在为False，存在为ture
print(os.path.islink(my_path))#判断文件是不是存在且是文件链接（快捷方式）
print(os.path.isdir(my_path))#判断文件是否存在且为一个目录
print(os.path.isfile(my_path))#判断文件是否存在且为一个文件

#操作系统相关操作
import os
my_path="d:/aaa"
print(os.listdir(my_path))#['bbb'](相当于ls命令）
#查看一个目录下的所有文件：可以采用递归调用，罗列中的这些文件看它是一个文件还是一个目录，如果是文件就停止返回，如果是目录就继续递归调用
print(os.rename(my_path,'testaaa'))#把aaa重命名为testaaa

#walk函数
my_path="d:/testaaa"
for item in os.walk(my_path):
    print(item)#里面是目录路径，目录列表，文件列表

#把目录下的所有文件的全路径打印出来
import os
my_path="d:/testaaa"
for base_path,_,file in os.walk(my_path):
    for f in file:
        print(os.join(base_path,f))



#还有一个包叫shutils更接近Linux指令，下来学习
