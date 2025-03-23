import numpy
'''
NumPy 是 Python 中科学计算的核心库，提供了大量的数学函数和矩阵运算功能，
可以用于线性代数、傅里叶变换、随机数生成等多种应用。
NumPy 的核心数据结构是多维数组 ndarray，它支持大量的维度数组和矩阵运算。
'''
# 生成数据
x = numpy.linspace(0, 10, 100) # 起点0 终点10 生成100个数据
x2 = numpy.arange(0, 10, 0.1) # 起点0 终点10 步长0.1
x_random = numpy.random.rand(100) # 生成 0-1 之间的 100 个随机数

y_sin = numpy.sin(x) # 计算正弦值
y_cos = numpy.cos(x) # 计算余弦值
y_tan = numpy.tan(x) # 计算正切值
y_exp = numpy.exp(x) # 计算指数值
y_log = numpy.log(x) # 计算对数值
y_sqrt = numpy.sqrt(x) # 计算平方根
# 也可以利用 numpy 提供的函数基本函数来计算更复杂的函数
