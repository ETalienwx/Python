import types
__author__ = 'asus'
#swap
x=10
y=20
x,y=y,x
print(x,y)

for num in range(0,10):
    x=1
    pass
print(num,x)

# def fun():
#     x=1
#     return x
# print(x)

a=10
print(type(a))

a=10
b=type(a)
print(b)
print(type(b))

def fun():
    a=10
    print(a)
x=fun()
print(x)#None

if None:
    print("haha")
else:
    print("hehe")

if 0.0:
    print("haha")
else:
    print("hehe")

if [0]:
    print("haha")
else:
    print("hehe")

if (0,):
    print("haha")
else:
    print("hehe")

a="abcd"
b="abcd"
if a==b:
    print("haha")
else:
    print("hehe")

a="abcd"
b="abcd"
if id(a)==id(b):
    print("haha")
else:
    print("hehe")

a="abcd"
b=a
if id(a)==id(b):
    print("haha")
else:
    print("hehe")

a="abcd"
b=a
if a is b:
    print("haha")
else:
    print("hehe")

a=100
print(type(a)==type(100))

a=100
print(type(a)==types.IntType)

a=100
print(isinstance(a,type(100)))
a=[]
print(isinstance(a,list))

a=[]
b=list()
print(a,b)

a=[1,2,3,4]
b=tuple(a)
print(b)
print(type(b))

a=-10
print(abs(a))

a,b=divmod(10,3)
print(a,b)

a=10
b=str(a)
print(b,type(b))

#round
import math
print(math.pi)

for num in range(0,10):
    print(round(math.pi,num))

import random
print(random.randint(1,10))
help(random)

x=6
y=4
smaller=x if x<y else y
print(smaller)

#while else
def find(input_list,x):
    for num in range(0,len(input_list)):
        if input_list[num]==x:
            return num
    else:
        return None
a=[1,2,3,4,5,6]
print(find(a,5))

def ShowMaxFactor(x):
    count=x/2
    while count>1:
        if x%count==0:
            print 'largest factor of %d is %d'%(x,count)
            break
        count-=1
    else:
        print x,"is prime"

for i in range(10,20):
    print(ShowMaxFactor(i))


def outer():
    def inner():
        print("hehe")
    inner()
outer()

def outer():
    def inner():
        print("hehe")
    return inner
a=outer()
a()

def add(x,y):
    return x+y
print(add(10,20))
print(add("haha","hehe"))
print(add([1,2],[3,4]))
print(add((1,2),(3,4)))


def hello(x=100):
    return x
print(hello())
print(hello(1))

def get_point(x=0,y=0,z=0):
    print(x,y,z)
get_point(x=100,z=100)

#print(10,20,end=' ',sep=';')

a=[9,5,2,7]
b=sorted(a)
print(a,b)

# a=[9,5,2,7]
# b=sorted(a,reverse=Ture)
# print(a,b)

# def Cmp(x,y):
#     return x<y
# a=[9,5,2,7]
# b=sorted(a,cmp=Cmp)
# print(a,b)

# def Cmp(x,y):
#     if abs(x)<abs(y):
#         return -1
#     elif abs(x)>abs(y):
#         return 1
#     else:
#         return 0
# a=[9,-5,2,7]
# b=sorted(a,cmp=Cmp)
# print(a,b)

a=['aaaa','bbb','cc','d']
print(sorted(a,key=len))

def log(*data):
    for num in data:
        print(num)
log(10,20,30)
log(10,20,30,40)


def add(*data):
    ret=0
    for i in data:
        ret+=i
    print(ret)
add(1,2,3,4,5,6,7,8,9,10)
add(1,2,3,4)

def log(**data):
    for key in data:
        print(key,data[key])
log(x=1,y=2,z=3)





