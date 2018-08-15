from socket import *
# 1.创建套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)
# 2.准备接收方的ip地址及端口号
sendAddr = ("169.254.189.52",8080)
# 3.发送数据到指定地址
udpSocket.sendto("你好？！".encode("gb2312"),sendAddr)
# 4.关闭套接字
udpSocket.close()
