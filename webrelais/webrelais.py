#!/usr/bin/python2

import argparse
from relais_client import RelaisClient

server = 'webrelais.core.bckspc.de'

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Switch WebRelais')

    mutex = parser.add_mutually_exclusive_group(required=True)
    mutex.add_argument('--on',  '-on', dest='mode', action='store_const', const='on', help='Switch on')
    mutex.add_argument('--off', '-off', dest='mode', action='store_const', const='off', help='Switch off')
    mutex.add_argument('--status', '-s', dest='mode', action='store_const', const='status', help='Status of Relais')
    mutex.add_argument('--list',  '-l', dest='mode', action='store_const', const='list', help='List relais aliases')

    parser.add_argument('relais', nargs='?', type=int, choices=range(8), help="Relais you want to switch")

    args = parser.parse_args()

    webrelais = RelaisClient(server, 443)

    if args.mode == 'on':
        webrelais.setPort(args.relais)
        print "Relais %d switched on" % (args.relais,)
    elif args.mode == 'off':
        webrelais.resetPort(args.relais)
        print "Relais %d switched off" % (args.relais,)
    elif args.mode == 'status':
        for relais, status in enumerate(webrelais.getPorts()):
            print "Relais %d is %s" % (relais, ('on' if status else 'off'))
    elif args.mode == 'list':
        
        relais = ['door open', 'door close', 'door buzzer', 'exit light white',
                  'exit light red', 'alarm light', 'heater', 'relais 7']

        for index, name in enumerate(relais):
            print "%d: %s" % (index,name)
