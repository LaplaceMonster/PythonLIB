import matplotlib.pyplot as plt
import numpy 
'''
Matplotlib 是 Python 中最常用的 2D 绘图库之一。
能够创建高质量的图形，如折线图、柱状图、散点图、直方图、饼图等。
它为数据可视化提供了强大的功能，适用于科研、数据分析和工程应用。
Matplotlib 主要由 pyplot 模块组成，它提供了一组类似 MATLAB 的绘图函数。
基本绘图通常包含以下核心概念：
Figure（画布）：整个图形的背景容器。
Axes（坐标轴）：具体的绘图区域，可以包含多个子图。
Axis（轴）：x 轴和 y 轴。
Ticks（刻度）：轴上的刻度标记。
Line2D、Patch、Text（元素）：构成图形的基本组件，如线条、散点、文字等。
'''
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 生成数据
x = numpy.linspace(0, 10, 100)
y = numpy.sin(x)

# 创建图形
plt.plot(x, y, label="sin(x)", color="blue", linestyle="--", linewidth=2)

# 添加标题和标签
plt.title("正弦函数")
plt.xlabel("x 轴")
plt.ylabel("y 轴")

# 显示图例
plt.legend()

# 显示图形
plt.show()
