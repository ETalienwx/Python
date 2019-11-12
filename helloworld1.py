msg="hello world"
print(msg)

#元组
a=(1,2,3,4)
print(a)
#报错（元组不可以改变）
# a[0]=10
# print(a)

#列表
b=[5,"msg",[7,6,5,4],8]
print(b)
b[0]=10 #支持下标访问
print(b)

#切片
c='asdfghjkl'
print(c[::-1])
print(c[::-2])
print(c[::2])
print(c[1:4])

#通过key值查询value值
dic1={1:"dictionary",2:"kid",3:"key"}
print(dic1[2])
dic2={"书":"book","脸":"face"}
print(dic2["书"])

#int可以无限大，只要内存存的下
num=1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000
print(num)

num1=10
num2=3.14
print(type(num1))
print(type(num2))
print(len("abc"))

#理解引用的概念
str1="haha"#str1是haha的标签
str2="hehe"#str2是hehe的标签
print(id(str1))
print(id(str2))
str1="hehe"#str1也变成了hehe的标签
print(id(str1))
print(id(str2))

print("my name is 'ET'")

a=True
print(type(a))
#true运算的时候被当成了1
b=a+1
print(b)#输出2

#输入
# name=input("输入名字：")
# print(name)

a,b=1,2
c=a/b
print(c)
print(type(c))

d=a//b
print(d)
print(type(d))

print(2>4)#false
print(2<4)#true
print(2==4)#false
print(2!=4)#true
print(2<4 and a==4)#false
print(2>4 or 2!=4)#true
print(not 2>4)#true

a,b=10,20
if a>b:
    print(a)
else:
    print(b)


# a=20
# b=10
# if a==10:
#     print(a)
# elif b<a:
#     print(b)
# else:
#     pass





