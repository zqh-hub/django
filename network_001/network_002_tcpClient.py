import socket

# 基于tcp协议的socket连接
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 发送数据之前，先和服务器建立连接
sk.connect(("127.0.0.1", 9090))
# 发送内容 tcp：使用send;udp使用：sendto
sk.send("hello".encode("utf-8"))
sk.close()
