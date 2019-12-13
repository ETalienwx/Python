__author__ = 'asus'
a=set([1,2,3])
b=set([3,2,1])
print(a==b)

a=set([1,2,2,3])
print(a)

#bingji,jiaoji,chaji
a=set([1,2,3])
b=set([3,5,6])
print(a&b)#jiaoji
print(a|b)#bingji
print(a-b)#a you b meiyou
print(a^b)#buji(duichenchaji)

a=[1,2,2,3,3,4]
b=list(set(a))
print(b)

