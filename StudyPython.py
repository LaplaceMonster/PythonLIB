import os


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