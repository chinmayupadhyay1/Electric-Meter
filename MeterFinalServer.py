import socket
var=0
host="192.168.1.42"
port=5002
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((host,port))
while True:
    var=sock.recvfrom(1024)
    print(var[0])
