""" It takes all passwords from all 0x* files and stores
    them in Wordlist """

# list files in victim directory  			<= Done
# open Wordlist in append mode	  			<= Done
# take second column of each file and write in Wordlist <= Done
# arrange in ascending mode				<= Done
# remove duplicates					<= Done


import re
import os
import subprocess
import fnmatch

LOCATION = ''
FILES = ''
WORDLIST = ''


def main():
	list_files()
	open_wordlist()
	open_files()
	close_wordlist()
	filter()


def list_files():
	# puts list of victim files in FILES
	global LOCATION,FILES
	os.chdir('../victims')
	LOCATION = os.getcwd()
	FILES = os.listdir(LOCATION)


def open_wordlist():
	global WORDLIST
	WORDLIST = open(LOCATION+"/Wordlist",'w+')


def open_files():
	for files in FILES:
		if fnmatch.fnmatch(files,'0x*'): #fnmatch() ensures only 0x files are accessed and not the Wordlist
			file = open(LOCATION+'/'+files,'r')
			stuff = file.read()
			append_passwords(stuff)

def append_passwords(stuff):
	content = stuff.strip('\n').split('\n') #strip() required cuz for some reason 2 \n were being added
	for pair in content:
		password = pair.split(',')[1]
		WORDLIST.write(password+'\n')



def close_wordlist():
	WORDLIST.close()


def filter():
	WORDLIST = open(LOCATION+"/Wordlist",'r')
	CONTENT = WORDLIST.read().strip('\n').split('\n')
	CONTENT.sort()
	NEW_CONTENT = remove_duplicates(CONTENT)
	WORDLIST.close()
	WORDLIST = open(LOCATION+"/Wordlist",'w')
	WORDLIST.write(NEW_CONTENT)
	WORDLIST.close()

def remove_duplicates(CONTENT):
	NEW_CONTENT = []
	for password in CONTENT:
		if password not in NEW_CONTENT:
			NEW_CONTENT.append(password)
	NEW_CONTENT = '\n'.join(NEW_CONTENT)+'\n'
	return NEW_CONTENT


if __name__ == '__main__':
	main()
