import socket
import json

HOST = '127.0.0.1'  # 本地回环地址
PORT = 12345        # 与客户端通信的端口

def start_test_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[INFO] Test server started at {HOST}:{PORT}, waiting for client...")

    conn, addr = server.accept()
    print(f"[INFO] Client connected from {addr}")

    try:
        # 模拟发送 JSON 格式的数据
        test_data = {
            "temp": 26.5,
            "MAG": 1.56,
            "PHS": 1.74
        }
        json_str = json.dumps(test_data)
        conn.sendall(json_str.encode())
        print(f"[SEND] {json_str}")

        # 接收客户端返回的预测结果
        result = conn.recv(1024).decode()
        print(f"[RECV] Predicted result from client: {result}")

    finally:
        conn.close()
        server.close()
        print("[INFO] Test server closed.")

if __name__ == "__main__":
    start_test_server()
