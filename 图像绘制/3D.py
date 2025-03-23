'''
Matplotlib是Python中最常用的2D绘图库之一。
但是也可以绘制一些简单的3D图形。但缺点是3D图形的绘制比较复杂，
而且Matplotlib的3D绘图功能相对较弱且不支持交互。

Plotly  是一个开源的数据可视化库，
支持交互式绘图，提供了丰富的图表类型和样式，
适用于数据分析、科学研究和工程应用。
Plotly 的绘图功能强大且易于使用，支持在线绘图和离线绘图，
可以生成高质量的图形，如折线图、散点图、柱状图、饼图、热力图等。
'''
import plotly.graph_objects as go
import numpy
# 生成随机数据
x = numpy.random.rand(100)
y = numpy.random.rand(100)
z = numpy.random.rand(100)

# 创建 3D 散点图
fig = go.Figure(data=[go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(size=5, color=z, colorscale='Viridis')  # 颜色映射
)])

fig.update_layout(title="3D 散点图")

fig.show()