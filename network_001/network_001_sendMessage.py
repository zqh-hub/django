import socket

# 1、创建socket
# AF_INET:表示这个socket是用来进行网络连接的
# SOCK_STREAM：表示连接是一个udp的
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2、绑定自己的端口
sk.bind(("192.168.0.101", 8000))
# 3、连接并发送数据
# address:发送给谁的IP\Port
sk.sendto("hello world".encode("utf-8"), ("192.168.0.105", 9000))
# 4、接收105发过来的消息
data, address = sk.recvfrom(1024)
sk.close()
