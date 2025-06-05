import os
import sys
import time
import mmap
import socket
import multiprocessing
import ctypes
from multiprocessing import Process, Pipe, Queue, Value, Array, Lock, Manager

import win32pipe, win32file, pywintypes

PIPE_NAME = r'\\.\pipe\MyPipe'  # 与 Qt 中服务端一致的命名管道名称

def named_pipe_client():
    """
    Python命名管道客户端，连接Qt服务端命名管道并进行通信。
    """
    try:
        print("Connecting to pipe...")
        # 等待服务端创建好管道
        time.sleep(1)  # 可根据实际情况调整

        # 连接到命名管道（需要服务端已运行）
        handle = win32file.CreateFile(
            PIPE_NAME,
            win32file.GENERIC_READ | win32file.GENERIC_WRITE,
            0, None,
            win32file.OPEN_EXISTING,
            0, None
        )

        # 发送消息到Qt服务端
        message = b"Hello from Python pipe client"
        win32file.WriteFile(handle, message)
        print("Sent:", message.decode())

        # 读取Qt服务端返回的数据
        result, data = win32file.ReadFile(handle, 4096)
        print("Received:", data.decode())

        # 关闭连接
        win32file.CloseHandle(handle)

    except pywintypes.error as e:
        print("Pipe connection error:", e)

SHARED_MEM_FILE = "shared_mem.dat"
MEM_SIZE = 1024

def read_shared_memory():
    """
    读取 Qt 服务端写入的共享内存文件内容。
    """
    # 确保文件已由 Qt 服务端创建
    if not os.path.exists(SHARED_MEM_FILE):
        print("Shared memory file not found.")
        return

    with open(SHARED_MEM_FILE, "r+b") as f:
        # 映射整个共享内存区域
        mm = mmap.mmap(f.fileno(), MEM_SIZE, access=mmap.ACCESS_READ)

        # 读取数据
        mm.seek(0)
        raw = mm.read(MEM_SIZE)
        message = raw.split(b'\x00', 1)[0].decode(errors='ignore')
        print("Received from shared memory:", message)

        mm.close()

HOST = '127.0.0.1'  # Qt 服务端监听的地址
PORT = 12828       # Qt 服务端监听的端口

HOST = '127.0.0.1'   # 本机地址
PORT = 12828         # 目标端口

def socket_client():
    """
    TCP 客户端：连接本地 Qt TCP 服务端，交互式发送并接收数据。
    """
    try:
        time.sleep(1)  # 延时，确保服务端已启动

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"[INFO] Connecting to {HOST}:{PORT}...")
            s.connect((HOST, PORT))
            print("[INFO] Connected. Type your messages below (type 'exit' to quit):")

            while True:
                message = input(">>> ").strip()
                if message.lower() in {"exit", "quit"}:
                    print("[INFO] Exiting.")
                    break

                if not message:
                    continue

                s.sendall(message.encode())

                data = s.recv(1024)
                print("[RECV]", data.decode())

    except ConnectionRefusedError:
        print("[ERROR] Connection refused. Make sure Qt server is running.")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    socket_client()