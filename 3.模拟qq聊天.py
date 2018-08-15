from threading import Thread
from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)
destIp = ""
destPort = 0
# 1.收数据，然后打印
def recvData():
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print(">>%s:%s"%(str(recvInfo[1]),recvInfo[0].decode("gb2312")))

# 2.检测键盘，发数据
def sendData():
    while True:
        sendInfo = input("<<")
        # udpSocket.sendto(发送信息，（目的ip，目的端口）)
        udpSocket.sendto(sendInfo.encode("gb2312"),(destIp,destPort))
def main():
    global udpSocket
    global destIp
    global destPort
    destIp = input("对方的ip：")
    destPort = int(input("对方的Port:"))
    udpSocket = socket(AF_INET,SOCK_DGRAM)
    udpSocket.bind(("",7788)) #7768，7788
    tr = Thread(target=recvData)
    ts = Thread(target=sendData)
    tr.start()
    ts.start()
    tr.join()
    ts.join()
if __name__ == '__main__':
    main()
