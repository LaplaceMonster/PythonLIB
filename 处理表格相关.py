import pandas
''' pandas是一个用于数据处理和分析的强大Python库。
    Series：一维数组，类似于Python的列表或NumPy的数组。
    DataFrame：二维表格数据结构，类似于电子表格或SQL表格。
    支持读取和写入多种文件格式，如CSV、Excel、SQL数据库、JSON等。
    数据清洗：处理缺失值、重复数据等。
    数据转换：数据类型转换、数据重塑等。
    数据合并：连接、合并和拼接数据集。
    统计分析：描述性统计、分组操作、聚合等。
    时间序列分析：处理时间序列数据，支持日期范围生成、频率转换等。
'''

#df = pandas.read_excel("file.xlsx")#读取Excel文件
#df = pandas.read_csv('data.csv')#读取CSV文件
'''
DataFrame 是 pandas 库中最重要的数据结构之一，
它是一个二维的表格数据结构，类似于电子表格或SQL表格。
可以使用多种方法来创建dataframe，如从列表、字典、Series、Numpy数组等。
'''
#最常用的列表list创建DataFrame
data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]
df = pandas.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)

print(df.head())  # 查看前5行
print(df.tail())  # 查看后5行
print(df.shape)   # 查看DataFrame的形状（行数, 列数）
print(df.columns) # 查看列名
print(df.info())  # 查看DataFrame的基本信息
print(df.describe())  # 查看数据的统计信息


print(df['Name'])  # 选择单列



print(df[['Name', 'Age']])  # 选择多列  可以这样来提取某一列或者多列

print(df.iloc[0])  # 按行号选择
print(df.loc[0])   # 按索引选择

df = df.dropna()  # 删除包含缺失值的行
df = df.fillna(0)  # 用0填充缺失值
df = df.drop_duplicates()  # 删除重复行

df['Age'] = df['Age'].astype(float)  # 转换数据类型
df['Name'] = df['Name'].str.upper()  # 转换字符串为大写


#print(df.groupby('City').mean())  # 按城市分组并计算平均值
#print(df['Age'].mean())  # 计算年龄的平均值
print(df['Age'].sum())   # 计算年龄的总和