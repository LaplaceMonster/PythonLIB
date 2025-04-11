import numpy as np
import matplotlib.pyplot as plt
'''
将原始数据拟合为多项式曲线

'''

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

x=[-4.1,0, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60]

y1=[81.29567636, 82.24643398, 81.81998597, 81.0418206, 79.99343699, 78.69254204, 77.19320534, 75.67490646, 74.17839069, 72.62833718, 69.5395849, 66.46274852]

y2=[0.301236367,0.253157261,0.213531964,0.181946399,0.154210254,0.133832408,0.118730938,0.104366218,0.093180302,0.084781027,0.068914587,0.057828285]
degree = 2  # 设置多项式阶数
coeffs = np.polyfit(x, y1, degree)  # 拟合
poly_eq = np.poly1d(coeffs)        # 得到拟合方程

print(f"拟合的多项式方程为：\n{poly_eq}")
y_fit = poly_eq(x)  # 用拟合函数计算预测值

plt.scatter(x, y1, label='原始数据', color='blue', s=10)
plt.plot(x, y_fit, label=f'{degree}阶拟合曲线', color='red')
plt.legend()
plt.title('多项式拟合示例')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()