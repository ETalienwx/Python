#切片
a="abcdefg"
print(len(a))#7
print(max(a))#g
print(min(a))#a
print(a+a)#abcdefgabcdefg
print(a*3)#abcdefgabcdefgabcdefg
print(a[2:5])#cde
print(a.index("c"))#2
print(a[4])#e

print(a[-1:3:-1])#从倒数第一个开始，取到正数第三个（不包括这一位），倒着取一定要加负数的步长
print(a[-1:-4:-1])#从倒数第一个开始，取到倒数第四个（不包括这一位）


#con[start_index]
print(a[3])#d(取下标为3的元素)
#con[start_index:]
print(a[3:])#defg(从下标为3取到结尾，步长默认1)
#con[: end_index］
print(a[:3])#abc(默认起始位置为0，也就是从开始取到下标为3，不包括下标为3的元素)
#con[:]
print(a[:])#abcdefg(全缺省就是取开始到结尾的整个片段)
#con[start_index: end_index]
print(a[2:5])#cde(从下标为2，取到下标为5，但是不包括下标为5)
#con[start_index: end_index : step]
print(a[1::2])#bdf(从下标为1开始，取到结尾，步长为2)
#con[::step]
print(a[::2])#aceg(正序取，步长为2)

#错误代码
# list1=[1,2,3,4,5,6]
# print(len(list1))#list1的长度是6
# print(list1[len(list1)])#会报错，越界访问

#用切片逆置序列
a="abcdefg"
b=[1,2,3,4,5,6]
c=(11,22,33,44,55,66)

b.reverse()
print(b)

print(a[::-1])
print(b[::-1])
print(c[::-1])


