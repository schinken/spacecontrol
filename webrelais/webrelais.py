#!/usr/bin/python2

import argparse
from relais_client import RelaisClient

server = 'webrelais.core.bckspc.de'

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Switch WebRelais')

    parser.add_argument('--relais', '-r', dest='relais', type=int, required=True, choices=range(8), help='Relais you want to switch')
    parser.add_argument('--on',  '-on', dest='on', default=False, action='store_true', help='Switch on')
    parser.add_argument('--off', '-off', dest='off', default=False, action='store_true', help='Switch off')

    args = parser.parse_args()

    if not (args.on or args.off):
        parser.error('No action requested, add --on or --off')

    webrelais = RelaisClient(server, 443)

    if args.on:
        webrelais.setPort(args.relais)
        print "Relais %d switched on" % (args.relais,)

    if args.off:
        webrelais.resetPort(args.relais)
        print "Relais %d switched off" % (args.relais,)
