import calc
#相当于调用calc里面的函数
#可以理解为是命名空间
#calc.py这个文件必须放在当前目录中，或者系统目录中
print(calc.add(10,20))
print(calc.divide(10,20))
print(calc.mul(10,20))
print(calc.sub(10,20))