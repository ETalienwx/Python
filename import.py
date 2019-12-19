__author__ = 'asus'
import os#操作系统
print(id(os),type(os))
print(os.__doc__)

import sys#系统
for path in sys.path:
    print(path)

#如果我要导入的库不在当前目录，那我可以这样做，添加path路径信息
import sys
sys.path.append(r"E:\CODEGitHub\Python")#转换成原始字符串，给path里添加该路径
import calc#然后这个模块就可以使用了
print(calc.add(10,20))

#一次性打包
import sys,os

#导入先导入标准库，在导入第三方库，在导入自定义模块
#模块也是一个对象
#模块可以在其他位置导入，只有导入了才可以使用
def fun():
    import os.oath
    print(os.path.exists("d:hhh.txt"))
fun()
os.path.exists("d:hhh.txt")#这条语句不能执行，因为os.path相当于一个变量，它的作用域只在fun（）函数内部


import os.path as op #可以用op代替os.path
import sys
s=sys #可以用s代替sys
s.path #也就是sys.path


#高内聚低耦合
#import是导入整个模块
#from 。。。import。。是导入模块中的指定名字
from os.path import exists#导入os.path中的exists，#模块间的低耦合
def fun():
    print(exists("d:hhh.txt"))#这里可以直接使用
fun()

from os.path import *#导入了os.path中的所有内容，后序可以直接使用，但是会有命名冲突的问题，所以不建议使用


import os.path#导入了模块，后序调用要写os.path.

#三种导入方式
import os.path
import os.path as op
from os.path import exists

#当import一个模块时
#其实就是执行了一下对应导入的模块
#import两次时，只会导入一遍
#导入成功之后会有一个__pycache__，这就是导入模块的痕迹，里面是翻译后的二进制


#python2里有一种操作，先导入一个模块，在程序运行中把模块修改了，想重新导入
#可以使用reload（模块名）来实现，但是python3中把该函数删除了





#__main__是程序的入口
#print(__name__)------如果是入口文件的话那么就会打印出__main__
#如果是库文件的话那么就会打印出库名
#谁是入口文件谁的__name__就打印出__main__





