'''
list是Python内置的一种数据类型 ，他是一个有序的数据的集合
'''
classmates = ['Michael', 'Bob', 'Tracy']#list列表
print(classmates)
print(len(classmates))#使用len函数可以获取list的数据的个数
#list还可以使用下表索引元素，append方法追加元素等等

'''
python可以对集合数据进行1切片 2迭代 3列表生成式 4生成器 5迭代器
'''


def fun01(L):
    #取前三个元素 第一个参数表示第元素起始位置，第二个数表示元素的结束位置-1，第三个元素与表示取出元素的间隔
    print(L[0:10:2])
    #第一个数和最后一个数可以省略 默认从第一个元素开始间隔为1
    print(L[:3])

    #也可以倒数进行切片操作 且最后一个元素为-1 倒数第一个为-2依次类推
    print(L[-3:])
    '''
    tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
    字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：

    '''
    str='ABCDEFG'
    print(str[:3])
    return 


def fun02(L):
    '''
    可以方便的遍历整个list或者其他类型的数据
    '''
    for i in L:
        print(i)
    return

def fun03():
    '''
    生成式
    '''
    #可以直接初始化list
    print(list(range(1,11)))

    #也可以对生成的数据进行一些运算
    L=[x*x for x in range(1,11)]
    print(L)

    #1 for循环的后面还可以加上if语句是过滤数据
    #2 for循环的前面加上if-else语句是对数据的判断操作（并未过滤）
    L=[x*x for x in range(1,11) if x%2==0]
    print(L)

    L=[x if x%2==0 else 0 for x in range(1,11)]
    print(L)

    #也可以使用多层循环生成全排列
    str=[m+n for m in 'ABC' for n in 'abc']
    print(str)
    return

def fun04():
    #生成器是一种强大的数据类型他保存的是数据的表达式而不是数据，即只有在调用某个具体的元素时他才会返回具体数据
    #使用起来很简单只需要将列表生成式的括号改为()
    G=(range(1,100))#生成器内部只有数据的一种表达式因此生成器占用较少的内存
    for i in G:
        print(i)
    return

L=list(range(100))
fun01(L)
fun02(L)
fun03()
fun04()