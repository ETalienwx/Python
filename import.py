__author__ = 'asus'
import os#����ϵͳ
print(id(os),type(os))
print(os.__doc__)

import sys#ϵͳ
for path in sys.path:
    print(path)

#�����Ҫ����Ŀⲻ�ڵ�ǰĿ¼�����ҿ��������������path·����Ϣ
import sys
sys.path.append(r"E:\CODEGitHub\Python")#ת����ԭʼ�ַ�������path����Ӹ�·��
import calc#Ȼ�����ģ��Ϳ���ʹ����
print(calc.add(10,20))

#һ���Դ��
import sys,os

#�����ȵ����׼�⣬�ڵ���������⣬�ڵ����Զ���ģ��
#ģ��Ҳ��һ������
#ģ�����������λ�õ��룬ֻ�е����˲ſ���ʹ��
def fun():
    import os.oath
    print(os.path.exists("d:hhh.txt"))
fun()
os.path.exists("d:hhh.txt")#������䲻��ִ�У���Ϊos.path�൱��һ������������������ֻ��fun���������ڲ�


import os.path as op #������op����os.path
import sys
s=sys #������s����sys
s.path #Ҳ����sys.path


#���ھ۵����
#import�ǵ�������ģ��
#from ������import�����ǵ���ģ���е�ָ������
from os.path import exists#����os.path�е�exists��#ģ���ĵ����
def fun():
    print(exists("d:hhh.txt"))#�������ֱ��ʹ��
fun()

from os.path import *#������os.path�е��������ݣ��������ֱ��ʹ�ã����ǻ���������ͻ�����⣬���Բ�����ʹ��


import os.path#������ģ�飬�������Ҫдos.path.

#���ֵ��뷽ʽ
import os.path
import os.path as op
from os.path import exists

#��importһ��ģ��ʱ
#��ʵ����ִ����һ�¶�Ӧ�����ģ��
#import����ʱ��ֻ�ᵼ��һ��
#����ɹ�֮�����һ��__pycache__������ǵ���ģ��ĺۼ��������Ƿ����Ķ�����


#python2����һ�ֲ������ȵ���һ��ģ�飬�ڳ��������а�ģ���޸��ˣ������µ���
#����ʹ��reload��ģ��������ʵ�֣�����python3�аѸú���ɾ����





#__main__�ǳ�������
#print(__name__)------���������ļ��Ļ���ô�ͻ��ӡ��__main__
#����ǿ��ļ��Ļ���ô�ͻ��ӡ������
#˭������ļ�˭��__name__�ʹ�ӡ��__main__





