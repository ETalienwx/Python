__author__ = 'asus'

num=10
#python 里的float就是double
pi=3.14
name="wangxuan"
#python是动态强类型的编程语言
name=100
count=num+1
print(type(num))

#字符串格式化
s='num={}'.format(num)
s='num=%d'% num
#s=f'num={num}'

str='abcdef'
str[1:3]

#bool
#True是1，False是0
value=True
print(value+1)#2

#输入input输出print
s=input("请输入一段内容")#input的返回值是字符串
print("s:",s)

s=input("请输入一个数字")
print("num+1=",int(num)+1)

#/是除 //是整除
a=1
b=2
a/b#0.5
a//b#0

#**是乘方
a=100
b=100
a**b#100的100次方

a=1
b=2
c=3
print(a<b<c)
#c++里面该表达式永远为ture，因为a<b这个表达式要不是0要不是1,0和1与3相比永远小，所以表达式为真
#python里面就是数学的含义a<b and b<c

#python里逻辑与 and
#逻辑或 or
#逻辑非 not
2<4 and 2==4 #false
2>4 or 2<4 #true
not 6.2<6 #true

#字符串比较
a="haha"
b="hehe"
a==b#false

#python里没有++操作--操作
num=10
num+=1

#列表
a=[]#空列表
a=[9,5,2,7]
a[-1]#7
a[0]=100#把第一个元素改成100

a=[9,'hehe',5,2]
a=[9,'hehe',[1,2],7]

#元组(tuple)
a=(9,5,2,7)
a[2]#5
#a[0]=100 #这里会报错

#列表是可变对象，元组是不可变对象，元组的对象不可以改

#字典(键值对)底层是哈希表
a={
    'ip':'127.0.0.1',
    'port':80
}
print(a)

#json出自于JavaScript表示对象
#{
#    "hero_name":"曹操"
#    "skill1":"剑气"
#    "skill2":"三段跳"
#    "skill3":"吸血"
#}

print(a['port'])#80

#哈希表的底层是一棵树，可以把key映射到数组下标上，数组取下标是O(1)的操作
#哈希冲突：不同的key映射到相同的下标
#解决方法：开散列和闭散列
#unordered_map用挂链表解决

#理解引用
a='hehe'
b=a
#C++创建a定义为hehe，然后创建b，把a的值赋值给b（深拷贝）
#java 有一块内存是hehe，a里面试hehe的地址，b里面也是hehe的地址（浅拷贝）
#python中也是浅拷贝，可以把变量名想象成标签，如果a='haha'，就是把a标签拿过来贴到haha上
print(id(a))
print(id(b))#id可以查看对象的唯一标识（不是地址）


