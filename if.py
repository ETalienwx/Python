__author__ = 'asus'

num=1
if num==1:
    print("haha")
else:
    print("hehe")

num=1
while num<=10:
    print(num)
    num+=1

for num in range(1,11):
    print(num)

a=[9,5,2,7]
for num in a:
    print(num)

a='abcdef'
for num in a:
    print(num)

a={
    'ip':'127.0.0.1',
    'port':80
}
for key in a:
    print(a[key])

for num in range(1,100):
    if num%3==0:
        break
    print(num)

for num in range(1,100):
    if num%3==0:
        continue
    print(num)

a=10
if a==10:
    pass
else:
    print("hehe")

a=[1,2,3,4]
b=[]
for num in a:
    b.append(num**2)
print(b)

a=[1,2,3,4]
b=[x**2 for x in a]
print(b)

a=[1,2,3,4,5,6]
b=[x for x in a if x%2==0]
c=[x for x in a if x%2!=0]
print(b,c)