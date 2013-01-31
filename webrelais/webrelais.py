#!/usr/bin/python2

import argparse
from relais_client import RelaisClient

server = 'webrelais.core.bckspc.de'

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Switch WebRelais')

    parser.add_argument('--relais', '-r', dest='relais', type=int, required=True, choices=range(8), help='Relais you want to switch')

    mutex = parser.add_mutually_exclusive_group(required=True)
    mutex.add_argument('--on',  '-on', dest='mode', action='store_const', const=True, help='Switch on')
    mutex.add_argument('--off', '-off', dest='mode', action='store_const', const=False, help='Switch off')

    args = parser.parse_args()

    webrelais = RelaisClient(server, 443)

    if args.mode:
        webrelais.setPort(args.relais)
        print "Relais %d switched on" % (args.relais,)
    else:
        webrelais.resetPort(args.relais)
        print "Relais %d switched off" % (args.relais,)
