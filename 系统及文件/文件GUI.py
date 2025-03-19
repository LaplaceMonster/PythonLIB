'''
tkinter.filedialog 是 Tkinter 提供的 文件对话框 模块，可以用于打开、保存和选择文件/目录。
它是 GUI 应用中常用的功能，允许用户通过 文件浏览窗口 选择文件或目录。
函数	            作用
askopenfilename()	选择并返回文件路径（单个文件）
askopenfilenames()	选择多个文件，返回文件路径列表
askopenfile()	    选择单个文件，并以文件对象返回
asksaveasfilename()	选择保存文件的路径（不创建文件）
asksaveasfile()	    选择文件保存路径，并以文件对象返回
askdirectory()	    选择目录，返回目录路径
'''
import os
import tkinter
from tkinter import filedialog


filedialog.askdirectory(title="选择目录", initialdir="C:/") 
filedialog.askopenfilenames(title="选择需要处理的文件", filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])  
