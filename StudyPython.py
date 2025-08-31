import cmd
import os
import glob
import sys
print("Current working directory:", os.getcwd())
glob_files = glob.glob('*.py')
print("Python files in current directory:", glob_files)

if __name__ == "__main__":

    print('exit/end 退出程序')
    cmd=input('请输入命令:')
    while cmd != 'exit' and cmd != 'end':
        print(cmd)
        cmd=input('请输入命令:')
    print('程序退出')

