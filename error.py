__author__ = 'asus'

#NameError
#prin('hehe')

#IndexError
# a=[1,2,3]
# a[100]

#FileNotFoundError
# open('d:aaaaa.txt','r')

#try...except...
#�ֶ���׽
try:
    a=[1,2,3]
    print(a[100])
except IndexError as e:#�±����
    print(e)#list index out of range
print('after except')#��ӡ��仰

#��python�������Ȳ�׽��
try:
    a=[1,2,3]
    prin(a[1])
except IndexError as e:#��׽�±���󣬵��Ƿ��������﷨��������쳣���������Ȳ�׽��
    print(e)
print('after except')#�����ӡ��仰

#�����쳣���Զ���
try:
    a=[1,2,3]
    prin(a[1])
except IndexError as e:
    print("IndexError:",e)
except NameError as e:
    print("NameError:",e)#name 'prin' is not defined
print('after except')#��ӡ��仰

#�����io��ȡ���������except�����ٴν��ж�д����Ϊ�п��ܾ������翨��һ�µ��µģ��ڶ�дһ�ο��ܾͶ���

#try��else����
try:
    a=[1,2,3]
    print(a[1])
except IndexError as e:
    print("IndexError:",e)
except NameError as e:
    print("NameError:",e)
else:
    print("û���쳣����")
print('�����Ƿ����쳣��������붼��ִ��')

#�����κ��쳣����һ�㲻������ôд
try:
    a=[1,2,3]
    print(a[1])
except:
    print("���쳣����")
else:
    print("û���쳣����")
print('�����Ƿ����쳣��������붼��ִ��')

try:
    a=[1,2,3]
    print(a[1])
except Exception as e:
    print("���쳣����",e)
else:
    print("û���쳣����")
print('�����Ƿ����쳣��������붼��ִ��')

#finally
try:
    f=open("d:test.txt","r")
    print(f.write("aaa"))
except Exception as e:
    print("���쳣",e)
else:
    print("û���쳣����")
finally:
    f.close()#�ر��ļ�
    print("�����Ƿ����쳣�����߳��������κ���������finall���붼��ִ��")


#with�����Ͼ���try except finally �ļ�д��
# with open("d:test.txt","r",encoding="gbk") as f:
#     for line in f:
#         print(line,end='')


#�׳��쳣

#����Ϊ0�����������������
def divide(x,y):
    if y==0:
        return 0,False
    return x/y,True

#���������쳣
def div(x,y):
    if y==0:
        raise Exception("divide zero except")#���ַ���������һ��Exception����
    return x/y
try:
    div(10,0)
except Exception as e:
    print(e)

#�к������õĻ���������
def div(x,y):
    if y==0:
        raise Exception("divide zero except")#���ַ���������һ��Exception����
    return x/y
def test():
    div(10,0)#�����׳��쳣����test������û�д������Ի������ף��׸�������
test()

#��������������text���沶��
def div(x,y):
    if y==0:
        raise Exception("divide zero except")
    return x/y
def test():
    try:
        div(10,0)
    except:
        print("�����쳣")
test()
#Ҳ�������������ڵ���test�ĵط�����
def div(x,y):
    if y==0:
        raise Exception("divide zero except")
    return x/y
def test():
    div(10,0)

try:
    test()
except:
    print("�����쳣")

#pylint���뾲̬��鹤�ߣ���֤���������Ĺ���
