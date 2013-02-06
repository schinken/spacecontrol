#!/usr/bin/python2

import requests
import sys

if __name__ == '__main__':

    req = requests.get('http://status.bckspc.de/status.php?response=json')
    try:
        result = req.json()
    except:
        sys.exit('Invalid response')

    print "Members present:", result['members']
    print "Member devices:", result['member_devices']
    print "Unknown devices:", result['unknown_devices']

    if len(result['members_present']):

        nicknames = []
        for entry in result['members_present']:
            nicknames.append(entry['nickname'])

        print "Members:", ', '.join(nicknames)
