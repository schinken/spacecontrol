#!/usr/bin/python2

import argparse
import requests

ledapi_url = 'http://api.ledboard.bckspc.de'

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Control LED Board')

    mutex = parser.add_mutually_exclusive_group(required=True)
    mutex.add_argument('--text',  '-t', dest='text', nargs='+', default=False, help='Display text on ledboard')

    args = parser.parse_args()

    if args.text:
        message = ' '.join(args.text)
        if len(message) > 256:
            print "Text is too long"
        else:
            req = requests.get(ledapi_url+'/send_text', params={'message': message})
            if req.status_code == 200:
                print "Thank you! Your message will be displayed"
            else:
                print "Error posting message"
