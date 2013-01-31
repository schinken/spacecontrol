#!/usr/bin/python2.7
import getpass
import argparse
import requests

verify_url = 'https://door.bckspc.de/verify'

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Open or Close the Backspace Door')

    mutex = parser.add_mutually_exclusive_group(required=True)
    mutex.add_argument('--open',  '-o', dest='mode', action='store_const', const='Open', help='Close the door')
    mutex.add_argument('--close', '-c', dest='mode', action='store_const', const='Close', help='Open the door')

    args = parser.parse_args()

    passwd = getpass.getpass("Door password: ")

    req = requests.post(verify_url, data={'password': passwd, 'type': args.mode})

    try:
        result = req.json()
    except:
        sys.exit('Invalid response')

    if result['response']:
        print "Your request is being processed"
    else:
        print "One does not simply walk into backspace"


