__author__ = 'asus'

num=10
#python ���float����double
pi=3.14
name="wangxuan"
#python�Ƕ�̬ǿ���͵ı������
name=100
count=num+1
print(type(num))

#�ַ�����ʽ��
s='num={}'.format(num)
s='num=%d'% num
#s=f'num={num}'

str='abcdef'
str[1:3]

#bool
#True��1��False��0
value=True
print(value+1)#2

#����input���print
s=input("������һ������")#input�ķ���ֵ���ַ���
print("s:",s)

s=input("������һ������")
print("num+1=",int(num)+1)

#/�ǳ� //������
a=1
b=2
a/b#0.5
a//b#0

#**�ǳ˷�
a=100
b=100
a**b#100��100�η�

a=1
b=2
c=3
print(a<b<c)
#c++����ñ��ʽ��ԶΪture����Ϊa<b������ʽҪ����0Ҫ����1,0��1��3�����ԶС�����Ա��ʽΪ��
#python���������ѧ�ĺ���a<b and b<c

#python���߼��� and
#�߼��� or
#�߼��� not
2<4 and 2==4 #false
2>4 or 2<4 #true
not 6.2<6 #true

#�ַ����Ƚ�
a="haha"
b="hehe"
a==b#false

#python��û��++����--����
num=10
num+=1

#�б�
a=[]#���б�
a=[9,5,2,7]
a[-1]#7
a[0]=100#�ѵ�һ��Ԫ�ظĳ�100

a=[9,'hehe',5,2]
a=[9,'hehe',[1,2],7]

#Ԫ��(tuple)
a=(9,5,2,7)
a[2]#5
#a[0]=100 #����ᱨ��

#�б��ǿɱ����Ԫ���ǲ��ɱ����Ԫ��Ķ��󲻿��Ը�

#�ֵ�(��ֵ��)�ײ��ǹ�ϣ��
a={
    'ip':'127.0.0.1',
    'port':80
}
print(a)

#json������JavaScript��ʾ����
#{
#    "hero_name":"�ܲ�"
#    "skill1":"����"
#    "skill2":"������"
#    "skill3":"��Ѫ"
#}

print(a['port'])#80

#��ϣ��ĵײ���һ���������԰�keyӳ�䵽�����±��ϣ�����ȡ�±���O(1)�Ĳ���
#��ϣ��ͻ����ͬ��keyӳ�䵽��ͬ���±�
#�����������ɢ�кͱ�ɢ��
#unordered_map�ù�������

#�������
a='hehe'
b=a
#C++����a����Ϊhehe��Ȼ�󴴽�b����a��ֵ��ֵ��b�������
#java ��һ���ڴ���hehe��a������hehe�ĵ�ַ��b����Ҳ��hehe�ĵ�ַ��ǳ������
#python��Ҳ��ǳ���������԰ѱ���������ɱ�ǩ�����a='haha'�����ǰ�a��ǩ�ù�������haha��
print(id(a))
print(id(b))#id���Բ鿴�����Ψһ��ʶ�����ǵ�ַ��


