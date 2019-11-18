__author__ = 'asus'
def add(x,y):
    return x+y
ret=add(10,20)
print(ret)

#unpack
def get_point():
    x=10
    y=20
    return x,y
x,y=get_point()
print(x,y)

def get_point():
    x=10
    y=20
    return x,y
tmp=get_point()
print(type(tmp))

def get_point():
    x=10
    y=20
    return x,y
_,y=get_point()
print(y)

print(type(get_point))

