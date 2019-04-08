# Made from scratch by Gibraan Jafar

# list all files from victims folder except Wordlist
# Accept SSID name from user
# Go through all files and retieve all passwords
#	corresponding to that SSID


import os
import fnmatch


VICTIMS = list()
SSID = ''
PSK = list()


def main():
    list_victims()
    accept_ssid()
    search_psk()
    filter_results()
    display_result()



def list_victims():
    global VICTIMS
    os.chdir('../victims')
    VICTIMS = os.listdir(os.getcwd())


def accept_ssid():
    global SSID
    SSID = input(" Enter SSID : ")


def search_psk():
    for victim in VICTIMS:
        if fnmatch.fnmatch(victim,'0x*'):
            search_in(victim)


def search_in(file):
    """ searches for SSID in file passed to it """
    FILE_DESC = open(file,'r')
    content = FILE_DESC.read().strip('\n').split('\n')
    for pair in content:
        ssid = pair.split(',')[0]
        if ssid == SSID:
            PSK.append(pair.split(',')[1])
    FILE_DESC.close()



def filter_results():
    """ removes duplicates from PSK list """
    global PSK
    PSK.sort()
    new_psk = list()
    for psk in PSK:
        if psk not in new_psk:
            new_psk.append(psk)
    PSK = new_psk

def display_result():
    print("\n SEARCH RESULTS :")
    print(len(PSK)," results found ")
    for i in PSK:
        print(i)


if __name__ == '__main__':
	main()
