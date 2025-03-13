import math
'''
1 函数定义
2 函数的参数
'''

#*******************函数定义*******************
# Python中函数可以返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
#调用的时候可以直接声明两个变量来接受值
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
#tuple：元组，一种有序列表，一旦初始化就不能修改
t=("tuple",1,2,3,'s')
print(t)
#实际上返回的是一个tuple所以我们可以使用一个tuple来接受返回值
r = move(100, 100, 60, math.pi / 6)
print(r)
#*******************函数定义*******************



#*******************函数的参数*******************
#python中函数的参数可以有默认值，调用的时候可以不传递
def power(x,n=2):
#     默认计算x的平方
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(5))
#也可以传递参数
print(power(5,3))

#Python传入参数的个数可以是可变的，可以是0个，1个，2个到任意个
#可变参数的定义在参数前面加上*号
#在函数内部，参数numbers接收到的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict
#关键字参数的定义在参数前面加上**号
#在函数内部，参数kw接收到的是一个dict
#dict:字典，一种无序的键值对集合
d={'a':1,'b':2,'c':3}
print(d)
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Bob', 35, city='Beijing', job='Engineer')

#上述的参数可以混合使用
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
f1(1, 2)
f1(1, 2,3)
#*******************函数的参数*******************