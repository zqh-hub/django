import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定自己机器的IP和端口
sk.bind(("192.168.0.105", 9000))
# 获取到一个元组(数据，(ip,port))
data, address = sk.recvfrom(1024)
print("从IP：{ip}，端口号：{port},获取到{data}".format(ip=address[0], port=address[1], data=data))

# 发送给101消息
sk.sendto("gun", ("192.168.0.101", 8000))
sk.close()
