__author__ = 'asus'

#change string
a="abcd"
a="1"+a[1:]
print(a)

#int/float/bool/str/tuple... cannot be change
#list/dict can be change

a=10
print(id(a))
a+=1
print(id(a))

# a=10
# s=f'a={a}'
# print(s)

a="hello\n world"
print(a)

a=r"hello\n world"
print(a)

a="hello"
print('['+ a.center(50) +']')

a='hello'
print(a.count('l'))

a=[1,1,2,3]
print(a.count(1))

a=['aaa','bbb','ccc']
print(''.join(a))

a="hello"
print('['+ a.center(50) +']')
print('['+ a.ljust(50) +']')
print('['+ a.rjust(50) +']')

a='HELLO WORLD'
print(a.lower())
print(a.replace('WORLD','world'))
a='abc'
print(a.islower())
print(a.isalpha())
print(a.upper())
a='123'
print(a.isdigit())

a="hello world;aaa bbb"
print(a.split(';'))#is a list

a = '   hello world    '
print(a.strip())

a="hello world"
print(a.find('world'))
print(a.find('e'))

