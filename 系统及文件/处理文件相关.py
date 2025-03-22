import os #os模块提供了一种使用操作系统依赖功能的方法
import chardet #字符编码检测库
''''
os模块的path属性提供了一些关于文件路径的方法
'''
def FileInfo(file):
    print(os.path.dirname(file)) #打印文件路径

    filename_suffix=os.path.basename(file) #获取带后缀文件名
    fileName=os.path.splitext(filename_suffix)[0] #获取文件名
    fileSuffix=os.path.splitext(filename_suffix)[1] #获取文件后缀#输出文件
    #第一个参数目录路径，第二个参数文件名
    outFile=os.path.join(os.path.dirname(file), fileName+'+process'+fileSuffix) 

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

