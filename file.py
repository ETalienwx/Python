__author__ = 'asus'
# f = open('d:test.txt','r')
# a=f.readlines()
# print(a)
# f.close()
#
# f=open("d:test.txt",'r')
# a=f.readline()
# print(a)
# f.close()
#
# f=open('d:test.txt','r')
# for a in f:
#     print(a)
# f.close()
#
# f=open('d:test.txt','w')
# f.write("hello world")
# f.close()

#ͳ���ļ���ÿ�����ʵĸ���
# f=open('d:test.txt','r')
# word_dict={}
# for word in f:
#     #word=word[0:-1]
#     word=word.strip()
#     if word in word_dict:
#         word_dict[word]+=1
#     else:
#         word_dict[word]=1
# print(word_dict)
# f.close()

#�����ң������
f=open('d:test.txt','r')
print(type(f))

#����ʱ�رգ����ܻᵼ���ļ���Դй©
f.close()

#�ر��ļ�Ҫ�ر�С��
#1.���ص����
def fun():
    x=0
    y=0
    if x==0:
        f.close()
        return
    if y==0:
        f.close()
        return
    f.close()
#2.�б����Խ�����
def fun():
    a=[1,2,3,4]
    a[100]
    f.close()

#����python���ṩ��with���
#with��֤close���Ա����õ�
#with�����as�õ��Ķ����Ϊ�������Ĺ�������
def fun():
    with open("d:test.txt","r") as f:
        #�������ļ�����
        x=0
        if x==0:
            return

#�ڽ������ϲ鿴�ڽ�����
dir(__builtins__)

help(open)
#�ļ��򿪵ļ��ַ�ʽ
#rֻ��
#w����ļ�д
#a�ļ�������ں���д
#x�д����Ĺ���
#b�����Ʒ�ʽ��
#t�ı����ʹ�
#w+������ں���д

# #�ļ���������ĵ�,���´�����ӡ����
# with open("d:test.txt","r") as f:
#     for line in f:
#         print(line,end='')
# #�ļ��洢��һ�ֱ��뷽ʽ��gbk ���� utf8��
# #�����ȡ�ļ�Ҳ��һ�ֱ��뷽ʽ��unicode��
# #���ַ����ö�Ӧ��
# with open("d:test.txt","r",encoding="gbk") as f:
#     for line in f:
#         print(line,end='')


#�������ж����б���ȥ,�����ڴ���ȥ���ʺ϶�С�ļ�
print(f.readlines())
#forѭ����ȡ,Ƶ���Ķ�ȡ���ᵼ��Ч�ʱ���,���ǽ�ʡ�ռ�
for line in f:
    print(line)

#д�ļ�
f.write()

#�ļ�·���Ĳ���
import os.path
my_path='d:aaa/bbb/ccc.txt'
print(os.path.basename(my_path))#ccc.txt
print(os.path.dirname(my_path))#d:aaa/bbb
print(os.psth.split(my_path))#('d:aaa/bbb','ccc.txt')����һ��Ԫ��
print(os.psth.splitext(my_path))#('d:aaa/bbb/ccc','.txt')����һ��Ԫ��

print(os.path.exists(my_path))#�鿴�ļ��Ƿ���ڣ�������ΪFalse������Ϊture
print(os.path.islink(my_path))#�ж��ļ��ǲ��Ǵ��������ļ����ӣ���ݷ�ʽ��
print(os.path.isdir(my_path))#�ж��ļ��Ƿ������Ϊһ��Ŀ¼
print(os.path.isfile(my_path))#�ж��ļ��Ƿ������Ϊһ���ļ�

#����ϵͳ��ز���
import os
my_path="d:/aaa"
print(os.listdir(my_path))#['bbb'](�൱��ls���
#�鿴һ��Ŀ¼�µ������ļ������Բ��õݹ���ã������е���Щ�ļ�������һ���ļ�����һ��Ŀ¼��������ļ���ֹͣ���أ������Ŀ¼�ͼ����ݹ����
print(os.rename(my_path,'testaaa'))#��aaa������Ϊtestaaa

#walk����
my_path="d:/testaaa"
for item in os.walk(my_path):
    print(item)#������Ŀ¼·����Ŀ¼�б��ļ��б�

#��Ŀ¼�µ������ļ���ȫ·����ӡ����
import os
my_path="d:/testaaa"
for base_path,_,file in os.walk(my_path):
    for f in file:
        print(os.join(base_path,f))



#����һ������shutils���ӽ�Linuxָ�����ѧϰ
