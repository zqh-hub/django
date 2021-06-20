import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind(("129.168.0.103", 9009))
socket_server.listen(128)
client_socket, client_address = socket_server.accept()
# 接收到客户端要的文件名,并发送给客户端
file_name = client_socket.recv(1024)
with open(file_name, "rb") as f:
    data = f.read()
    socket_server.send(data)
