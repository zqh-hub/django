import socket

# 基于tcp协议的socket连接
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP端口
sk.bind(("192.168.0.103", 9090))
# 128代表能够处理的数量
sk.listen(128)
# 接收到客户端的请求，返回一个元组（客户端的socket,客户端ip）
client_socket, client_address = sk.accept()
# 客户端发送过来的具体数据：hello，每次读1024个字节
res = client_socket.recv(1024)
print(res)
