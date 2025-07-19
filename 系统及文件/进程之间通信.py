import socket
import sys
import os
import json
from multiprocessing import Process
'''
进程间通信示例
使用 socket 实现简单的客户端和服务器通信
客户端发送 JSON 数据，服务器接收并解析
'''

def server(name,port):
    print(f"函数:{server.__name__}---- {name} --->启动")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET表示使用 IPv4，SOCK_STREAM 表示使用 TCP 协议
    server_socket.bind(('localhost', port)) # 绑定到本地地址和端口
    server_socket.listen(1)
    print("服务器已启动，等待连接...")

    conn, addr = server_socket.accept()
    print(f"客户端连接来自: {addr}")

    data = conn.recv(1024).decode('utf-8')
    print(f"接收到数据: {data}")

    try:
        json_data = json.loads(data)
        print(f"解析后的数据: {json_data}")
    except json.JSONDecodeError as e:
        print(f"JSON 解析错误: {e}")

    conn.close()
    server_socket.close()
def client(name,port):
    print(f"函数:{server.__name__}---- {name} --->启动")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', port))

    data = {
        "name": "Alice",
        "age": 25,
        "hobbies": ["reading", "traveling"]
    }
    json_data = json.dumps(data)
    
    client_socket.sendall(json_data.encode('utf-8'))
    print(f"发送数据: {json_data}")

    client_socket.close()







if __name__=='__main__':
    master_process = Process(target=server, args=(name:="主进程",port:=12828))
    master_process.start()
    slave_process = Process(target=client, args=(name:="子进程", port:=12828))
    slave_process.start()
