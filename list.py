__author__ = 'asus'
a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

a=[1,2,3,4]
a.append(5)
print(a)
a.append([6,7])
print(a)
a.extend([8,9,10])
print(a)
print(len(a))
#del
del(a[5])
print(a)
#remove
a.remove(8)
print(a)
#in
print(2 in a)
print(15 in a)

a=[1,2,3]
b=[1,3,2]
print(a==b)

a=[1,2,3,3,3,3,3]
print(a.count(3))

a=[1,2,3,4]
print(a.index(3))
print(a.insert(1,5))
print(a.pop())
print(a.pop(0))

a=[5,4,7,8,2,5]
print(a.reverse())
print(a.sort())

a=[1,3,2]
print(sorted(a))#123
print(a)#132

a=[1,3,2]
print(a.sort())#None
print(a)#123

#stack
a=[1,2,3]
a.append(4)
print(a)
a.pop()
print(a)

#quene
a=[1,2,3]
a.append(4)
print(a)
a.pop(0)
print(a)

#deepcopy
a=[1,2,3]
b=a
a[0]=100
print(b)

import copy
a=[1,2,3]
b=copy.deepcopy(a)
a[0]=100
print(b)

a=(1,2,3)
b=(4,5,6)
print(a+b)
print(a.count(2))
print(a.index(2))

print(a+(4,))

(a,b)=(10,20)
def fun():
    return 10,20
print(type(fun()))

#tuple id can not change
a=([1,2],[3,4])
a[0][0]=100
print(a)


def fun(a):
    a[0]=100
a=[1,2,3,4]
fun(a)
print(a)

# def fun(a):
#     a[0]=100
# a=(1,2,3,4)
# fun(a)
# print(a)

a=()
b={a:10}
print(b)

