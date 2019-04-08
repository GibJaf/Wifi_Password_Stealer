# Made from scratch by Gibraan Jafar

# Is called when server by server.py before being terminated
# Removes duplicate passwords appended to Wordlist from accress
# clients

WORDLIST = '../victims/Wordlist'
PASSWORDS = list()


def main():
    try:
        open_wordlist()
        read_wordlist()
        remove_duplicate()
        arrange_asc()
        write_wordlist()
        close_wordlist()
    except:
        print("\n Work in progress !")


def open_wordlist():
    global WORDLIST
    WORDLIST = open(WORDLIST,'r+')


def read_wordlist():
    global PASSWORDS
    PASSWORDS = WORDLIST.read().strip('\n').split('\n')


def remove_duplicate():
    global PASSWORDS
    NEW_PASSWORDS = list()
    for password in PASSWORDS:
        if password not in NEW_PASSWORDS:
            NEW_PASSWORDS.append(password)
    """ For following statement , had to declare PASSWORDS
     as global , otherwise it trets PASSWORDS in below
     statement as a new local variable """
    PASSWORDS = NEW_PASSWORDS


def arrange_asc():
    PASSWORDS.sort()


def write_wordlist():
    passwords_string = '\n'.join(PASSWORDS)+'\n'
    WORDLIST.seek(0,0)
    WORDLIST.truncate()
    WORDLIST.write(passwords_string)


def close_wordlist():
    WORDLIST.close()


if __name__ == '__main__':
    main()
