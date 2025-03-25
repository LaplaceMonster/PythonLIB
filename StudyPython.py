import os
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def generate_picture(fileName):
    filename_suffix = os.path.basename(fileName)  # 获取带后缀文件名
    sheetName = os.path.splitext(filename_suffix)[0]  # 获取文件名
    print(f"正在处理文件--->{sheetName}")
    # 读取数据
    data = pd.read_excel(fileName, sheet_name=sheetName)

    ## **1️⃣ 选出数值列，不影响文本列**
    num_cols = ['日产液量', '日产油量', '日产水量', '日含水率', '日产气量', '生产时间']  # 只转换这些列
    data[num_cols] = data[num_cols].apply(pd.to_numeric, errors='coerce')

    # **2️⃣ 只删除数值列中有 NaN 的行**
    data = data.dropna(subset=num_cols)

    # **3️⃣ 确保数据不为空**
    if data.empty:
        raise ValueError("❌ 数据清洗后为空，请检查 Excel 文件格式！")

    # 处理日期列
    data['日期'] = pd.to_datetime(data['日期'])
    data = data.sort_values(by='日期', ascending=True)  # 按时间升序排列

    # 提取数据
    x = data['日期']
    y1 = data['日产液量']
    y2 = data['日产油量']
    y3 = data['日产水量']
    y5 = data['日产气量']

    # 创建一个画布，包含 1 行 2 列的 2 个子图
    fig, axes = plt.subplots(1, 2, figsize=(16, 8.94))

    # **子图1：日产液量、日产油量、日产水量**
    axes[0].plot(x, y1, label="日产液量", color="blue", linestyle="-", linewidth=2)
    axes[0].plot(x, y2, label="日产油量", color="red", linestyle="-", linewidth=2)
    axes[0].plot(x, y3, label="日产水量", color="green", linestyle="-", linewidth=2)
    axes[0].set_title(r"产液量/m$^3$ 产油量/t 产水量/m$^3$", fontsize=15)
    axes[0].set_xlabel("日期", fontsize=13)
    axes[0].set_ylabel("产量", fontsize=13)
    axes[0].grid(True, linestyle="--", linewidth=0.5, alpha=0.7)
    axes[0].legend()

    # **子图2：日产气量**
    axes[1].plot(x, y5, label="产气量", color="orange", linestyle="-", linewidth=2)
    axes[1].set_title(r"产气量/Nm$^3$", fontsize=15)
    axes[1].set_xlabel("日期", fontsize=13)
    axes[1].set_ylabel("气量/Nm$^3$", fontsize=13)
    axes[1].grid(True, linestyle="--", linewidth=0.5, alpha=0.7)
    axes[1].legend()

    # 自动调整子图间距，避免重叠
    plt.tight_layout()

    # 设置总标题并调整字体大小
    fig.suptitle(sheetName + "设备计量情况", fontsize=20, fontweight='bold')

    # 预留空间，避免总标题被覆盖
    plt.tight_layout(rect=[0, 0, 1, 0.96])  

    # 保存图像到文件
    fileDir=os.path.dirname(fileName)  # 获取文件路径
    picturName = fileDir+"/"+sheetName+'.png'  # 保存路径及文件名
    plt.savefig(picturName, dpi=300)  # 保存为 PNG 格式，300 dpi，确保清晰

    # 显示图形
    plt.show()

    print(f"图像已保存为：{picturName}")
# 选择文件
files= filedialog.askopenfilenames(title="选择需要处理的文件", filetypes=[("Excel文件", "*.xlsx"), ("所有文件", "*.*")])
for file in files:
    generate_picture(file)
