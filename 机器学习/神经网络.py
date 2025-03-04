import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# 模拟数据：假设你有幅度、相位和对应的含水率数据
# 生成一些模拟数据
np.random.seed(42)

# 生成模拟的幅度数据（幅度随着含水率减小）
amplitude = [0.8646,0.8599,0.8589,0.6211,0.5388,0.456,0.397,0.3415,0.2819,0.089]  # 幅度从1到0
# 生成周期性相位数据（随着含水率周期变化）
phase =[1.7125,1.6913,1.2917,0.6788,1.6311,0.212,1.256,1.5318,0.746,0.8677,1.627]  # 相位数据呈周期性
# 假设含水率与幅度和相位的关系（幅度与含水率成反比，相位为周期函数）
moisture_content = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]  # 含水率的关系是线性与周期性结合

# 将数据进行标准化（为了提高神经网络训练效果）
scaler = MinMaxScaler()
X = np.column_stack((amplitude, phase))
y = moisture_content
X_scaled = scaler.fit_transform(X)

# 数据集分割
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 构建神经网络模型
model = Sequential()

# 输入层和第一个隐藏层
model.add(Dense(64, input_dim=2, activation='relu'))
model.add(Dense(32, activation='relu'))

# 输出层：预测含水率
model.add(Dense(1, activation='linear'))

# 编译模型
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mae'])

# 训练模型
history = model.fit(X_train, y_train, epochs=200, batch_size=32, validation_data=(X_test, y_test))

# 评估模型
loss, mae = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss}, Test MAE: {mae}')

# 使用模型进行预测
y_pred = model.predict(X_test)

# 绘制结果对比图
plt.figure(figsize=(10, 6))
plt.plot(y_test, label="True Moisture Content")
plt.plot(y_pred, label="Predicted Moisture Content")
plt.legend()
plt.xlabel("Samples")
plt.ylabel("Moisture Content")
plt.title("True vs Predicted Moisture Content")
plt.show()
