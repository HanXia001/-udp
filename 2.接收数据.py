import socket
def socKet():
    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpSocket.bind(("",7788))
    # udpSocket.sendto(b"hehe",("169.254.189.52",8080))
    receiveData,desInfo = udpSocket.recvfrom(1024)
    print(receiveData.decode("gb2312"))
socKet()
