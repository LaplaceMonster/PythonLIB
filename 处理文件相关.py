import os #os模块提供了一种使用操作系统依赖功能的方法
from tkinter import Tk #Tkinter是Python的标准GUI库 TK是其中的一个类可以初始化一个主窗口
from tkinter import filedialog #filedialog是一个子模块，提供了一个对话框，用于选择文件或目录


def select_directory():
    '''
    这是一个可以弹出窗口并可以让用户选择文件夹的函数
    '''
    root = Tk()
    root.withdraw()  # 隐藏主窗口
    directory = filedialog.askdirectory()  # 弹出选择文件夹对话框
    return directory #返回的是一个字符串

def select_file():
    '''
    这是一个可以弹出窗口并可以让用户选择文件的函数
    '''
    root = Tk()
    root.withdraw()  # 隐藏主窗口
    file = filedialog.askopenfilename()  # 弹出选择文件对话框
    return file #返回的是一个字符串

def get_files_with_extension(directory, extension):
    """
    获取指定文件夹下所有指定后缀名的文件列表
    :param directory: 文件夹路径
    :param extension: 文件后缀名（例如 '.txt'）
    :return: 指定后缀名的文件列表
    """
    if not os.path.isdir(directory):
        raise ValueError(f"指定的路径不是一个有效的文件夹: {directory}")

    files_with_extension = [] #用一个list来存放文件名
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                files_with_extension.append(os.path.join(root, file))

    return files_with_extension


current_directory = os.getcwd()#获取当前工作目录
print(current_directory)
directory_contents = os.listdir(current_directory)#列出当前目录下的所有文件和目录
print(directory_contents)
#os.mkdir('/path/to/new_directory')#创建新目录

#os.remove('/path/to/file')#删除文件

#os.rmdir('/path/to/directory')#删除目录

#os.rename('/path/to/file', '/path/to/new_file')#重命名文件或者目录
file = 'D:/Python/StudyPython.py'
absolute_path = os.path.abspath(file)#获取文件的绝对路径
print(absolute_path)
file_name = os.path.basename(file)#获取文件名
print(file_name)
directory_name = os.path.dirname(file)#获取文件所在目录
print(directory_name)

exists = os.path.exists(file_name)#检查文件或目录是否存在
print(exists)

is_file = os.path.isfile(file_name)#检查是否是文件
print(is_file)

is_directory = os.path.isdir(file)#检查是否是目录
print(is_directory)

path = os.getenv('PATH')#获取环境变量
print(path)