# Python学习日志

## Excel表格/`CSV`

`DataFrame` 是 Pandas 中用于存储**表格数据**的主要数据结构，它类似于一个二维数组，可以轻松地进行各种数据操作，如排序、筛选、汇总、填充缺失值等。

### `DataFrame`对象

#### DataFrame.apply(func, axis=0, raw=False, result_type=None, args=(), **kwds)

##### 参数说明：

- **`func`**：应用的函数，可以是内置函数或自定义函数。
- **`axis`**：指定沿哪个轴应用函数。
  - `axis=0` 表示按列（默认）应用函数。
  - `axis=1` 表示按行应用函数。
- **`raw`**：如果设置为 `True`，则传递给函数的每列或每行将是一个 `ndarray`，否则将是一个 `Series`。
- **`result_type`**：决定结果的类型，可以为 `None`（默认），`'expand'`，`'reduce'` 或 `'broadcast'`。
- **`args`**：传递给 `func` 的额外位置参数。
- **`**kwds`**：传递给 `func` 的额外关键字参数。

```
import pandas as pd
# 创建一个示例 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# 按列计算每列的平方
result = df.apply(lambda x: x ** 2)
print(result)
# 按行计算每行的和
result = df.apply(lambda x: x.sum(), axis=1)
print(result)
```

一般情况下直接调用`DataFrame.dropna()`会出现错误，因为某些值是非数字类型，所以一般我们清除空值之前可以先调用转为数字的函数

```
# 使用 apply 将列转换为数字，无法转换的将变为 NaN
data = data.apply(pd.to_numeric, errors='coerce')
然后再清除空值
data.dropna()
```



### **📌 常用 Pandas 函数总结**

| **操作/功能**      | **函数**                                        | **描述**                                              |
| ------------------ | ----------------------------------------------- | ----------------------------------------------------- |
| **读取数据**       | `pd.read_csv()`                                 | 读取 CSV 文件并返回 DataFrame                         |
|                    | `pd.read_excel()`                               | 读取 Excel 文件并返回 DataFrame                       |
|                    | `pd.read_sql()`                                 | 从 SQL 数据库读取数据                                 |
| **查看数据**       | `df.head()`                                     | 查看前 N 行数据（默认前 5 行）                        |
|                    | `df.tail()`                                     | 查看后 N 行数据（默认后 5 行）                        |
|                    | `df.info()`                                     | 显示 DataFrame 的简要信息（数据类型、缺失值等）       |
|                    | `df.describe()`                                 | 显示数值型列的统计信息（如均值、标准差等）            |
|                    | `df.shape`                                      | 返回 DataFrame 的形状（行数，列数）                   |
|                    | `df.columns`                                    | 获取所有列名                                          |
| **数据清洗**       | `df.isnull()`                                   | 判断每个元素是否为 NaN（缺失值）                      |
|                    | `df.notnull()`                                  | 判断每个元素是否不是 NaN                              |
|                    | `df.fillna()`                                   | 填充缺失值（可以指定填充值或用均值等）                |
|                    | `df.dropna()`                                   | 删除缺失值所在的行或列                                |
|                    | `df.drop_duplicates()`                          | 删除重复数据                                          |
| **数据选择**       | `df['column_name']`                             | 选择某列数据（返回 Series）                           |
|                    | `df[['col1', 'col2']]`                          | 选择多列数据（返回 DataFrame）                        |
|                    | `df.loc[]`                                      | 基于标签选择数据（行列都可以用标签）                  |
|                    | `df.iloc[]`                                     | 基于位置选择数据（行列都可以用索引）                  |
| **数据修改**       | `df['new_column'] = ...`                        | 创建或修改列数据                                      |
|                    | `df.rename(columns={'old_name': 'new_name'})`   | 重命名列名                                            |
|                    | `df['column_name'] = df['column_name'].apply()` | 对某列应用函数                                        |
| **排序与筛选**     | `df.sort_values(by='column_name')`              | 按某列排序（默认升序，可设置 `ascending=False` 降序） |
|                    | `df.query()`                                    | 根据条件筛选数据（类似 SQL 的 WHERE）                 |
|                    | `df[df['column_name'] > value]`                 | 筛选符合条件的行                                      |
| **数据合并与连接** | `pd.merge()`                                    | 按照某列或索引合并两个 DataFrame                      |
|                    | `df.append()`                                   | 在 DataFrame 末尾追加数据（行）                       |
|                    | `df.concat()`                                   | 合并多个 DataFrame（行或列方向）                      |
| **数据分组与聚合** | `df.groupby('column_name')`                     | 按某列分组                                            |
|                    | `df.groupby('column_name').agg()`               | 按组进行聚合操作（如求和、求均值等）                  |
|                    | `df.pivot_table()`                              | 创建数据透视表（类似 Excel 的 Pivot Table）           |
| **数据透视**       | `df.crosstab()`                                 | 计算列间交叉表                                        |
| **统计分析**       | `df.mean()`                                     | 计算各列的均值                                        |
|                    | `df.median()`                                   | 计算各列的中位数                                      |
|                    | `df.std()`                                      | 计算各列的标准差                                      |
|                    | `df.corr()`                                     | 计算列之间的相关性                                    |
| **日期时间处理**   | `pd.to_datetime()`                              | 将字符串转换为日期时间格式                            |
|                    | `df['date_column'].dt.year`                     | 提取日期时间列的年、月、日等部分                      |
|                    | `df['date_column'].dt.month`                    | 提取日期时间列的月份                                  |
| **保存数据**       | `df.to_csv()`                                   | 将 DataFrame 保存为 CSV 文件                          |
|                    | `df.to_excel()`                                 | 将 DataFrame 保存为 Excel 文件                        |
|                    | `df.to_sql()`                                   | 将 DataFrame 存储到 SQL 数据库                        |

### **📌 常用数据操作和技巧**

| **操作/功能**    | **函数**                                          | **描述**                                        |
| ---------------- | ------------------------------------------------- | ----------------------------------------------- |
| **添加新列**     | `df['new_column'] = ...`                          | 向 DataFrame 添加新列                           |
| **删除列**       | `df.drop(columns=['col1', 'col2'], inplace=True)` | 删除指定列                                      |
| **添加索引**     | `df.set_index('column_name')`                     | 设置 DataFrame 的索引列（可以使用现有的某一列） |
| **重设索引**     | `df.reset_index()`                                | 重设索引（将当前索引列恢复为普通列）            |
| **透视表与聚合** | `df.pivot()`                                      | 按指定列进行数据透视                            |
| **合并数据集**   | `pd.concat()`                                     | 合并多个 DataFrame（按行或按列）                |
| **数据去重**     | `df.drop_duplicates()`                            | 删除重复行                                      |
| **条件过滤**     | `df.loc[df['col'] > value]`                       | 根据条件过滤数据                                |
| **数据转置**     | `df.T`                                            | 转置 DataFrame（行列交换）                      |

## 绘制图像

### `2D`

```
'''
python绘制2D图像非常简单 只需要三步
1 X轴数据
2 Y轴数据（二者数据长度需要一致）
3 调用matplotlib.pyplot.plot()函数绘制图像
'''
# 生成数据
x = numpy.linspace(0, 10, 100)
y = numpy.sin(x)

# 创建图形
plt.plot(x, y, label="sin(x)", color="blue", linestyle="--", linewidth=2)

# 添加标题和标签
plt.title("正弦函数")
plt.xlabel("x 轴")
plt.ylabel("y 轴")

# 显示图例:在图中添加曲线的名称
plt.legend(loc='upper right')  # loc参数可以指定图例的位置，如'upper right', 'lower left'等
plt.grid(True)  # 添加网格线
# 显示图形
plt.show()
#plt.savefig("picture", dpi=300)  # 保存为 PNG 格式，300 dpi，确保清晰
```

**`Matplotlib`** 是 Python 中最常用的 **`2D` 绘图库** 之一，它可以用于创建各种图表，如折线图、散点图、柱状图、直方图等。

 ✅ **强大灵活**：支持多种类型的图表
 ✅ **与 `NumPy `兼容**：可以直接使用 NumPy 数组绘图
 ✅ **风格可定制**：可以调整颜色、线型、坐标轴等
 ✅ **适用于静态图像**：主要用于 2D 静态可视化

| **图表类型** | **函数**         | **说明**         |
| ------------ | ---------------- | ---------------- |
| 折线图       | `plt.plot()`     | 显示数据趋势     |
| 散点图       | `plt.scatter()`  | 观察数据分布     |
| 柱状图       | `plt.bar()`      | 对比不同类别数据 |
| 直方图       | `plt.hist()`     | 统计数据分布     |
| 饼图         | `plt.pie()`      | 显示比例关系     |
| 误差棒图     | `plt.errorbar()` | 显示误差范围     |
| 保存图片     | `plt.savefig()`  | 保存图片         |

### `3D`

**`Plotly`** 是 Python 中最常用的 **3D 绘图库** 之一，它不仅支持 3D 绘图，还提供了非常强大的交互功能。`Plotly `特别适合用来生成交互式图表，尤其在数据分析和可视化方面，广泛应用于报告、仪表板以及交互式应用中。

 ✅ **交互性强**：生成的图表可以缩放、旋转和悬停显示信息，非常适合探索性数据分析。
 ✅ **多样化图表**：支持2D、3D 图表、地理地图等多种类型。
 ✅ **高度自定义**：几乎每个元素都可以自定义，如颜色、大小、样式、布局等。
 ✅ **Web 集成**：可以将图表嵌入到网页或 Jupyter Notebook 中，方便展示和分享。
 ✅ **支持在线和离线绘图**：可以在浏览器中生成图表，也支持离线渲染。

## 人工智能

## 机器学习

### 监督学习

#### 回归：

- 预测**连续数值**，即输出是一个**实数值**。
- 适用于**温度预测、信号误差校正、股票价格预测**等任务。

 ✅ **线性回归（Linear Regression）**
 ✅ **岭回归（Ridge Regression）**
 ✅ **支持向量回归（SVR, Support Vector Regression）**
 ✅ **随机森林回归（Random Forest Regression）**
 ✅ **XGBoost 回归**
 ✅ **神经网络（MLP, CNN, LSTM）**（用于复杂时序或高维数据）

#### **分类：**

- 预测**离散类别**，即输出是一个**类别标签**。
- 适用于**垃圾邮件检测、情感分析、图像识别、信用风险评估**等任务。

 ✅ **逻辑回归（Logistic Regression）**（适用于二分类）
 ✅ **K 近邻（KNN, K-Nearest Neighbors）**（适用于小数据集）
 ✅ **支持向量机（SVM, Support Vector Machine）**（适用于高维数据）
 ✅ **决策树（Decision Tree）**（适用于可解释性任务）
 ✅ **随机森林（Random Forest）**（集成学习，提高泛化能力）
 ✅ **XGBoost / LightGBM / CatBoost**（适用于结构化数据）
 ✅ **朴素贝叶斯（Naïve Bayes）**（适用于文本分类）
 ✅ **卷积神经网络（CNN）**（适用于图像分类）
 ✅ **Transformer（BERT, GPT）**（适用于文本、语音分类）

### 无监督学习

### 强化学习