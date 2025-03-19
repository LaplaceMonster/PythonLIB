import os
from datetime import datetime
from tkinter import filedialog
import pandas
import chardet #字符编码检测库

def getFileEncodeFromat(file):
    '''
    chardet.detect(data)会返回一个字典，其中包含了字符编码的信息
    {'encoding': 'GB2312', 'confidence': 0.99, 'language': 'Chinese'}
    '''
    codeFormat =''
    with open(file, 'rb') as f:
        data = f.read()
        codeFormat = chardet.detect(data)['encoding']
    return codeFormat

def processExcel(file):
    print(os.path.basename(file)) #打印文件路径
    data=pandas.read_excel(file) #读取文件进行处理
    data['液位差']=data['液位'].diff() #计算液位差
    col_index = data.columns.get_loc("液位")  # 获取 "液位" 的列索引
    data.insert(col_index + 1, "液位差", data.pop("液位差"))  # 插入到其右侧
    data=data[(data['液位'] < 50) & (data['液位差'] >= 0)]  #筛选出液位小于50的数据

    filename_suffix=os.path.basename(file) #获取带后缀文件名
    fileName=os.path.splitext(filename_suffix)[0] #获取文件名
    fileSuffix=os.path.splitext(filename_suffix)[1] #获取文件后缀
    outFile=os.path.join(os.path.dirname(file), fileName+'+筛选'+fileSuffix) #输出文件

    data.to_excel(outFile, index=False, sheet_name="Sheet1")  # 不保存行索引，指定工作表名
    print(outFile + "处理完成")

def processCSV(file):
    print(os.path.basename(file)) #打印文件路径
    
    data=pandas.read_csv(file,encoding=getFileEncodeFromat(file)) #按字符格式读取文件

    data['液位差']=data['液位'].diff() #计算液位差
    col_index = data.columns.get_loc("液位")  # 获取 "液位" 的列索引
    data.insert(col_index + 1, "液位差", data.pop("液位差"))  # 插入到其右侧
    data=data[(data['液位'] < 50) & (data['液位差'] >= 0)]  #筛选出液位小于50的数据

    filename_suffix=os.path.basename(file) #获取带后缀文件名
    fileName=os.path.splitext(filename_suffix)[0] #获取文件名
    fileSuffix=os.path.splitext(filename_suffix)[1] #获取文件后缀
    outFile=os.path.join(os.path.dirname(file), fileName+'+筛选'+fileSuffix) #输出文件

    data.to_csv(outFile, index=False)  # 不保存行索引，指定工作表名
    print(outFile + "处理完成")

files=filedialog.askopenfilenames(title="选择需要处理的文件", filetypes=[("Excel表格", "*.xlsx"), ("CSV文件", "*.CSV*")]) 

for file in files:
    if os.path.splitext(file)[1] == ".xlsx":
        processExcel(file)
    else:
        processCSV(file)
