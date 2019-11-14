#while执行语句
a=1
while a<10:
    print(a)
    a+=2

#分开奇数和偶数
num=[23,32,45,54,65,99,12,2,1,6,8]
a=[]
b=[]
while len(num)>0:
    n=num.pop()
    if(n%2==0):
        a.append(n)
    else:
        b.append(n)
print(a)
print(b)

#打印数字
count=0
while(count<9):
    print("this count is:",count)
    count=count+1

#打印偶数
i=1
while(i<10):
    i+=1
    if(i%2!=0):
        continue#到while
    print(i)

#while...else...
count=0
while(count<5):
    print("%d is less than 5" % count)
    count+=1
else:#else就是while语句不成立时执行的语句
    print("%d is not less than 5" % count)


count=5
while(count>0):
    print(count)
    count-=1
else:
    print("LAST:",count)

#while基础格式示例，定义url，并逐行从开头处减少一个字符显示
url="www.baidu.com"
while(url):
    print(url)
    url=url[1:]#从下标为1的数开始取，取到结尾，每次把下标为0的数跳过

#while基础格式示例，自定义url，并逐行从结尾处减少一个字符显示
url="www.qq.com"
while(url):
    print(url)
    url=url[:-1]

url="www.qq.com"
print(len(url))#10
while(url):
    print(url)#第一次直接打印完整的url
    url=url[:len(url)-1]#从下标为0的数开始取，取到len(url)-1

#while基础格式示例，逐行打印“x= 0”到“x = 9”
x=0
while(x<10):
    print("x=%d" % x)
    x+=1

#while-else格式示例，自定义url，并逐行从结尾处减少一个字符显示，且当循环执行结束后打印提示信息“Game over !”
url="www.qq.com"
while(url):
    print(url)
    url=url[:-1]
else:#while执行完会执行else
    print("game over!")


#break用法示例：自定义url，逐行从结尾处减少一个字符显示，自定义if条件，当减少5个字符时结束打印。
url="www.qq.com"
x=0
while(url):
    print(url)
    url=url[:-1]
    x+=1
    if(x==5):
        break
else:#break会直接跳出最内层的循环，所以else不会执行
    print("hhhhhh")

#continue用法示例：自定义url，逐行从结尾处减少一个字符显示，自定义if条件，当减少5个字符时结束打印，并提示信息“Reduce 5 chars,game over!”
url="www.qq.com"
x=0
while(url):
    print(url)
    url=url[:-1]
    x+=1
    if(x<5):
        continue
    else:
        print("Reduce 5 chars,game over!")#大于5的时候就break中止
        break
        
# #while True语句用法示例
# l=[]
# while True:
#     print('PleaseInput An Char:')
#     x=input()
#     if(x=="q" or x=="quit"):#如果是q或者quit就停止接收char
#         break
#     else:
#         l.append(x)#不是q或者quit就插入到l里
# print(l)


#逐一显示指定列表中的所有元素
l=[1,2,3,4,5]
count=0
while(count<len(l)):
    print(l[count])
    count+=1


for x in l:
    print(x)

#求100以内所有偶数之和
sum=0
x=0
while(x<100):
    if(x%2==0):
        sum=sum+x
    x+=1    
print(sum)

sum=0
x=0
while(x<100):
    sum=sum+x
    x+=2
print(sum)

sum=0
for x in range(0,100):
    if(x%2==0):
        sum+=x
print(sum)

#并逐一显示指定字典的所有键；于显示结束后说明总键数
d = {'x':11,'y':22,'z':33,'k':44}
x=0
for key in d:#依次取d里的key
    print(key)
    x+=1
else:
    print("总键数:%d"%x)

#打印key和value
d = {'x':11,'y':22,'z':33,'k':44}
for key in d:
    print(key," is ",d[key])

#创建一个包含了100以内所有奇数的列表
l=[]
x=0
while(x<100):
    x+=1
    if(x%2!=0):
        l.append(x) 
else:
    print(l)
      

