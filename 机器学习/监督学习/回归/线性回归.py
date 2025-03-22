'''
线性回归：  y = ax+by+cz+d
本质上就是求解一个线性方程组
但是这个方程组的解不一定存在，所以需要用最小二乘法来求解
最小二乘法：
    1. 有一个线性方程组：y = ax+by+cz+d
    2. 有一组数据：(x1,y1,z1),(x2,y2,z2),(x3,y3,z3)...
    3. 求解出a,b,c,d
    4. 使得所有的数据点到这个平面的距离之和最小
    5. 通过最小二乘法可以求解出a,b,c,d
    6. 通过这个方程可以预测未来的数据
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
'''
scikit-learn 是一个第三方 Python 库，专门用于机器学习，
提供了各种经典的监督学习、无监督学习、数据预处理和模型评估工具。
'''
# 生成数据
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # 100个数据点
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3X + 噪声

# 创建线性回归模型
model = LinearRegression()
model.fit(X, y)  # 训练模型

# 预测
X_new = np.array([[0], [2]])  # 预测两个点
y_pred = model.predict(X_new)

# 绘图
plt.scatter(X, y, color="blue", label="Data")
plt.plot(X_new, y_pred, color="red", linewidth=2, label="Prediction")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

# 输出权重和截距
print(f"w (斜率): {model.coef_[0][0]:.2f}, b (截距): {model.intercept_[0]:.2f}")
