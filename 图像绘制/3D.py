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
import os
from tkinter import filedialog
from datetime import datetime, timedelta
import pandas

'''
['日期', '井号', '设备编号', '日产液量', '日产油量', '日产水量',
'日含水率', '日产气量', '日气油比','生产时间']
'''
fileName=filedialog.askopenfilename(title="选择需要处理的文件", filetypes=[("Excel文件", "*.xlsx"), ("所有文件", "*.*")])  
print(f"正在处理文件{os.path.basename(fileName)}")
data=pandas.read_excel(fileName)

data['日期'] = pandas.to_datetime(data['日期']) #读取日期列

data = data.sort_values(by='日期', ascending=True)#按时间排序升序（早的排在前面）


# 创建 3D 散点图
fig = go.Figure(data=[go.Scatter3d(
    x=data['日期'],  # X 轴：日期
    y=data['日产液量'],  # Y 轴：日产液量
    z=data['日含水率'],  # Z 轴：日含水率
    mode='markers',  # 只显示点
    marker=dict(size=5, color=data['日含水率'], colorscale='Viridis', opacity=0.8)
)])

# 设置布局
fig.update_layout(
    title="日产液量 vs 日含水率 (3D 散点图)",
    scene=dict(
        xaxis_title='日期',
        yaxis_title='日产液量 (m³)',
        zaxis_title='日含水率'
    )
)

fig.show()  # 显示图形