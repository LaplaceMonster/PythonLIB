import math

'''
使用*args参数来接收任意数量的参数 func01
**kwargs参数可以接收任意数量的关键字参数 func02

也可以使用*args和**kwargs来接收任意数量的参数
并对这些参数进行处理
'''

def func01(*args):
    '''
    使用*args参数来接收任意数量的参数
    对这些参数进行求和处理

    args是一个元组，包含所有传入的参数
    '''
    sum = 0
    for i in args:
        if not isinstance(i, int):
            raise TypeError("All arguments must be integers")
        sum += i
    return sum

print(func01(1, 2, 3, 4, 5))  # Output: 15
print(func01(100, 200, 300))  # Output: 600

def func02(**kwargs):
    '''
    使用**kwargs参数来接收任意数量的关键字参数
    对这些参数进行求和处理
    kwargs是一个字典，包含所有传入的关键字参数
    '''
    sum = 0
    for key, value in kwargs.items():
        if not isinstance(value, int):
            raise TypeError("All arguments must be integers")
        sum += value
    return sum
print(func02(a=1, b=2, c=3))  # Output: 6
print(func02(x=10, y=20, z=30))  # Output: