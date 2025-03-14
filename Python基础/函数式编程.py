import datetime

#函数可以向C语言一样可以让一个变量指向一个函数，
#然后这个变量可以像调用函数一样调用这个函数
def abs(x):
    if x>=0:
        return x
    else:
        return -x 
fun01=abs
print(fun01(-1))
#这样的话就有了向C语言的回调函数的概念，即函数可以作为参数传递
def add(x,y,abs):
    return abs(x)+abs(y)
print(add(-1,2,abs))
#可以引出内置的两个函数map和reduce
#map函数接受两个参数，一个是函数，一个是Iterable
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x,y):
    return x*10+y
r=reduce(add,[1,3,5,7,9])
print(r)
'''
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
def is_odd(n):
    return n%2==1
r=filter(is_odd,[1,2,3,4,5,6,7,8,9])
print(list(r))
'''
Python内置的sorted()函数就可以对list进行排序
sorted()函数也是一个高阶函数，
它还可以接收一个key函数来实现排序的规则是降序还是升序等等
'''
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

'''
函数除了可以作为参数传递外，还可以作为返回值返回
'''
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())#只有调用时才会真正计算
#在这个例子中我们定义了一个函数lazy_sum，它返回了一个函数sum
#在这个函数中我们定义了一个局部变量ax，这个变量在sum函数中使用
#在这个函数中我们使用了外部函数的参数args
#这种称为闭包的函数在Python中是支持的


'''
匿名函数
Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数
'''
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#关键字lambda表示匿名函数，冒号前面的x表示函数参数
#匿名函数有个限制，就是只能有一个表达式，不用写return，
#返回值就是该表达式的结果




'''
装饰器
现在，假设我们要增强now()函数的功能，
比如，在函数调用前后自动打印日志，
但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个返回函数的高阶函数。
所以，我们要定义一个能打印日志的decorator，可以定义如下：
'''
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log#把@log放到now()函数的定义处，相当于执行了语句now = log(now)
def now():
    print(datetime.datetime.now())
now()