import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect(("192.168.0.103", 9090))
file_name = input("请输入要接收的文件名：")
# 发送给服务端文件名
socket_client.send(file_name.encode("utf-8"))
# 客户端接收文件
with open(file_name, "wb") as f:
    while True:
        data = socket_client.recv(1024)
        if not data:
            break
        f.write(data)
