#遍历字符串中的每一个字符
for letter in "python":
    print("当前字母：",letter)

#打印列表
list1=[1,2,"hhh",4,[2,3,4,5],6,7,8,9]
for num in list1:
    print(num)

#通过序列索引迭代
#用range打印
fruits=["banana","apple","mango"]
for index in range(len(fruits)):
    print("当前水果:",fruits[index])

#偶数全部变为二倍
list2=[1,2,3,4,5,6,7,8,9]
for index in range(len(list2)):
    if(list2[index]%2==0):
        list2[index]*=2
    else:
        pass
print(list2)

#找质数（for...else...）
for num in range(10,20):#循环1：取10到20之间的数
    for i in range(2,num):#循环2：取2到num之间的数，作为除数
        if(num%i==0):#确定第一个因子
            j=num/i#确定第二个因子
            print("%d 等于 %d * %d   "%(num,i,j))
            break
    else:
        print("%d 是一个质数"% num)
        
#求50到100之间的质数
#1.正确代码
for i in range(50,100):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)

#2.if与else对齐时，有问题了
# for i in range(50,101):
#     for j in range(2,i):
#         if(i%j==0):#当i不可以整除j时，else就会打印该数，并且循环打印，直到找到一个整除自己等于0的数
#             break
#         else:
#             print(i)

#遍历字典中的key和value
dic={"apple":"苹果","banana":"香蕉","mango":"芒果"}
for i in dic:
    print(i,dic[i])
for i in dic:
    print("key:",i)
    print("value:",dic[i])

#for循环打印三次
for i in range(0,3):
    print("hhh:%d" % i)#0,1,2

#for循环加步长
for i in range(0,100,2):#取0到100中所有的偶数
    print(i)

#打印0-100中所有的3的倍数
for i in range(0,100):
    if(i%3!=0):#不是3的倍数就继续
        continue
    print(i)#是3的倍数就打印

    
#查找1-100中第一个被3整除的数字
for i in range(1,100):
    if(i%3==0):
        print(i)
        break

# #整数序列求和。用户输入一个正整数N，计算从1到N（包含1和N）相加之后的结果
# num=input("请输入一个数字：")
# sum1=0
# for n in range(0,int(num)+1):
#         sum1+=n
# print(sum1)

#九九乘法表输出
for i in range(1,10):
    for j in range(1,i+1):
        print(("{}*{}={}   ").format(j,i,i*j),end='')
    print("\n")

#阶乘计算。计算1+2！+3！+……10！的结果
# sum2=0
# temp=1
# for i in range(0,11):
#         temp*=i
#         sum2+=temp
# print("运算结果是:{}".format(sum2))

n = int(input())
jie = 1
sum = 0
i = 1
while n >= i:
    jie = jie * i
    sum = sum + jie
    i = i + 1
print(sum)
    
# def jie(n):
#     if n == 1:
#         return 1
#     else:
#         return n*jie(n-1)
# n = int(input())
# sum = 0
# if n < 1 or n > 40:
#     print("请重新输入数据")
# else:
#     for i in range(1,n+1):
#         sum = sum + jie(i)
#     print(sum)