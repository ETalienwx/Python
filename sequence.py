__author__ = 'asus'
#is sequence
a=[1,2,3]
b=[3,2,1]
print(a==b)#False

#not sequence
a={'ip':'127.0.0.1','port':80}
b={'port':80,'ip':'127.0.0.1'}
print(a==b)#Ture

a=[1,2,3,4]
print(1 in a)#Ture
print(10 in a)#False

b=[4,3,2,1]
print(a<b)#Ture

a="hello world"
print("world" in a)#Ture

a=[1,2]
b=[3,4]
print(a+b)
a.extend(b)
print(a)

a=['aaa','bbb','ccc']
ret=''
for str in a:
    ret+=str
print(ret)

a=['aaa','bbb','ccc']
ret=''.join(a)
print(ret)


a=['aaa','bbb','ccc']
ret=';'.join(a)
print(ret)

a=['aaa','bbb','ccc']
ret='-'.join(a)
print(ret)

a=[1,2,3,4]
print(a*2)

a="123456"
print(a[:])
print(a[0])
print(a[0:5])
print(a[3:5])
print(a[2:])
print(a[:3])
print(a[0:6:2])
print(a[::-1])
print(a[::-2])
print(a[1::2])

a=[1,2,3,4,5,6]
print(len(a))#6
print(max(a))#6
print(min(a))#1

a=[9,5,2,7]
a.sort()
print(a)

a=[9,5,2,7]
b=sorted(a)
print(b)

a="sdiuwebcins"
print(''.join(sorted(a)))

a=[1,-5,2,-4]
print(sorted(a,key=abs))
print(sorted(a))
print(sum(a))

a=[1,2,3,4]
def find1(input_list,x):
    for num in range(0,len(input_list)):
        if input_list[num]==x:
            return num
    else:
        return None
#enumerate--->i,value
def find2(input_list,x):
    for i,value in enumerate(input_list):
        if value==x:
            return i
    else:
        return None


a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
for i in zip(a,b,c):
    print(i)
# (1, 4, 7)
# (2, 5, 8)
# (3, 6, 9)

#str,list,tuple---->sequence

