__author__ = 'asus'

#NameError
#prin('hehe')

#IndexError
# a=[1,2,3]
# a[100]

#FileNotFoundError
# open('d:aaaaa.txt','r')

#try...except...
#手动捕捉
try:
    a=[1,2,3]
    print(a[100])
except IndexError as e:#下标错误
    print(e)#list index out of range
print('after except')#打印这句话

#被python解释器先捕捉了
try:
    a=[1,2,3]
    prin(a[1])
except IndexError as e:#捕捉下标错误，但是发生的是语法错误，因此异常被解释器先捕捉了
    print(e)
print('after except')#不会打印这句话

#捕获异常可以多种
try:
    a=[1,2,3]
    prin(a[1])
except IndexError as e:
    print("IndexError:",e)
except NameError as e:
    print("NameError:",e)#name 'prin' is not defined
print('after except')#打印这句话

#如果是io读取错误可以在except里面再次进行读写，因为有可能就是网络卡顿一下导致的，在读写一次可能就对了

#try和else连用
try:
    a=[1,2,3]
    print(a[1])
except IndexError as e:
    print("IndexError:",e)
except NameError as e:
    print("NameError:",e)
else:
    print("没有异常发生")
print('无论是否有异常，这个代码都会执行')

#捕获任何异常，但一般不建议这么写
try:
    a=[1,2,3]
    print(a[1])
except:
    print("有异常出现")
else:
    print("没有异常发生")
print('无论是否有异常，这个代码都会执行')

try:
    a=[1,2,3]
    print(a[1])
except Exception as e:
    print("有异常出现",e)
else:
    print("没有异常发生")
print('无论是否有异常，这个代码都会执行')

#finally
try:
    f=open("d:test.txt","r")
    print(f.write("aaa"))
except Exception as e:
    print("有异常",e)
else:
    print("没有异常发生")
finally:
    f.close()#关闭文件
    print("无论是否发生异常，或者出现其他任何情况，这个finall代码都会执行")


#with本质上就是try except finally 的简化写法
# with open("d:test.txt","r",encoding="gbk") as f:
#     for line in f:
#         print(line,end='')


#抛出异常

#除数为0的情况可以这样处理
def divide(x,y):
    if y==0:
        return 0,False
    return x/y,True

#还可以抛异常
def div(x,y):
    if y==0:
        raise Exception("divide zero except")#用字符串构造了一个Exception对象
    return x/y
try:
    div(10,0)
except Exception as e:
    print(e)

#有函数调用的话会往上抛
def div(x,y):
    if y==0:
        raise Exception("divide zero except")#用字符串构造了一个Exception对象
    return x/y
def test():
    div(10,0)#这里抛出异常但是test函数里没有处理，所以会往上抛，抛给解释器
test()

#可以这样处理：在text里面捕获
def div(x,y):
    if y==0:
        raise Exception("divide zero except")
    return x/y
def test():
    try:
        div(10,0)
    except:
        print("捕获异常")
test()
#也可以这样处理：在调用test的地方捕获
def div(x,y):
    if y==0:
        raise Exception("divide zero except")
    return x/y
def test():
    div(10,0)

try:
    test()
except:
    print("捕获异常")

#pylint代码静态检查工具，保证代码质量的工具
