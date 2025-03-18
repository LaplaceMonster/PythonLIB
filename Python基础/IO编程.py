'''
文件读写：
'''
# 读文件
try:
    f = open('d:/Code/GitHub/PythonLIB/README.md', 'r')
    print(f.read())
finally:
    if f:
        f.close()
#使用with语句来自动帮我们调用close()方法：
'''
with语句适用于自动清理资源的场景
文件操作：open()
数据库连接：sqlite3.connect()
网络请求：requests.get()
线程锁：threading.Lock()
临时文件：tempfile.TemporaryFile()
as 语句会将前面的对象赋值给后面的变量
因此我们使用的f就是open()函数返回的文件对象
'''
with open('d:/Code/GitHub/PythonLIB/README.md', 'r',encoding='utf-8') as f:
    print(f.read())


# 写文件
with open('d:/Code/GitHub/PythonLIB/Python基础/README.txt', 'a') as f:
    f.write('Hello, world!')

'''
StringIO和BytesIO使用场景：
StringIO顾名思义就是在内存中读写str。
BytesIO顾名思义就是在内存中读写二进制数据。
适用哪些临时文件，而不是直接写入文件，直接写入内存
比文件效率更高
'''
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())


'''
操作文件和目录：
'''
import os
#获取操作系统类型
print(os.name)
#获取环境变量
print(os.environ)
#获取某个环境变量的值
print(os.environ.get('PATH'))
#查看当前目录的绝对路径
print(os.path.abspath('.'))
