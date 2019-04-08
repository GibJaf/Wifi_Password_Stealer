import socket
SERVER_IP = '3.88.38.38'
serversocket = ''

serversocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_address = (SERVER_IP , 12345)
serversocket.connect(server_address)
print(serversocket.recv(1024))
serversocket.close()
