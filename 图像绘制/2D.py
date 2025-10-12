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

'''
python绘制2D图像非常简单 只需要三步
1 X轴数据
2 Y轴数据（二者数据长度需要一致）
3 调用matplotlib.pyplot.plot()函数绘制图像
'''
# 生成数据
x = numpy.linspace(0, 10, 100)
y1 = numpy.sin(x)
y2 = numpy.cos(x)
y3=numpy.tan(x)
# 创建图形
plt.plot(x, y1, label="sin(x)", color="blue", linestyle="--", linewidth=2)
plt.plot(x, y2, label="cos(x)", color="red", linestyle="-.", linewidth=2)
plt.plot(x, y3, label="tan(x)", color="green", linestyle="-", linewidth=2)# 可以在同一个图中绘制多条曲线
# 添加标题和标签
plt.title("正弦与余弦函数")
plt.xlabel("x 轴")
plt.ylabel("y 轴")

# 显示图例
plt.legend(loc='upper right')
plt.grid(True)

# 显示图形
plt.show()
#plt.savefig("picture", dpi=300)  # 保存为 PNG 格式，300 dpi，确保清晰

# 创建 1行2列 的子图
fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # figsize可调整整体大小
axes[0].plot(x, y1, label="sin(x)", color="blue", linestyle="--", linewidth=2)
axes[0].legend(loc='upper right')
axes[0].grid(True)
axes[0].set_title("正弦函数")
axes[0].set_xlabel("x 轴")
axes[0].set_ylabel("y 轴")
axes[1].plot(x, y2, label="cos(x)", color="red", linestyle="-.", linewidth=2)
axes[1].legend(loc='upper right')
axes[1].grid(True)
axes[1].set_title("余弦函数")
axes[1].set_xlabel("x 轴")
axes[1].set_ylabel("y 轴")
plt.show()