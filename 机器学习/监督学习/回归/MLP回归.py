import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 1. 生成模拟数据（1000条）
np.random.seed(42)
n_samples = 1000

# 模拟幅度（随含水率单调下降）
water_content = np.random.uniform(0, 1, n_samples)
amplitude = 1 - 0.6 * water_content + np.random.normal(0, 0.02, n_samples)

# 相位（随含水率周期性变化）
phase = np.sin(4 * np.pi * water_content) + np.random.normal(0, 0.1, n_samples)

# 温度（随机 10~40°C）
temperature = np.random.uniform(10, 40, n_samples)

# 加入温度对幅度和相位的影响（模拟干扰）
amplitude -= 0.003 * (temperature - 25)
phase += 0.01 * (temperature - 25)

# 2. 构造特征矩阵和目标
X = np.column_stack((amplitude, phase, temperature))
y = water_content  # 含水率

# 3. 划分训练集/测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. 建立 MLP 回归模型
model = MLPRegressor(hidden_layer_sizes=(32, 16),
                     activation='relu',
                     solver='adam',
                     max_iter=1000,
                     random_state=42)

# 5. 训练模型
model.fit(X_train, y_train)

# 6. 预测和评估
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"均方误差 (MSE): {mse:.4f}")
print(f"R²得分: {r2:.4f}")

# 7. 可视化预测效果
plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([0, 1], [0, 1], 'r--')
plt.xlabel("真实含水率")
plt.ylabel("预测含水率")
plt.title("MLP 含水率预测效果")
plt.grid(True)
plt.show()
