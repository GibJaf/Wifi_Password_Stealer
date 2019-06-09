#!/usr/bin/python3

import argparse
import sys

EMAIL = ''
PASSWORD = ''
args = ''

def get_arguments():
    global EMAIL , PASSWORD
    parser = argparse.ArgumentParser()
    parser.add_argument("-e","--email",dest="email",help="Email to send wifi passwords to")
    parser.add_argument("-p","--password",dest="password",help="Password for email address given in -e argument")
    args = parser.parse_args()

    if args.email == None or  args.password == None:
        if args.email == None:
            print(" Email missing")

        if args.password == None:
            print(" Password missing")

        print("Usage : python3 mail_password.py -e <email_address> -p <password_of_email>")
        sys.exit()

    else:
        EMAIL = args.email
        PASSWORD = args.password


def generate_agent():
    seg = " is password for "
    f = open('agent.py','w')
    f.write(EMAIL)
    f.write(seg)
    f.write(PASSWORD)
    f.close()

def main():
    global args
    args = get_arguments()
    generate_agent()


if __name__ == "__main__":
    main()
