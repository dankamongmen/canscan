#!/usr/bin/env python

# canScan - CANopen discovery/scanning tool
#
# https://github.com/dankamongmen/canscan

from __future__ import print_function
import node
import signal
import argparse

DEFAULT_NODEID = 0x64
CANOPEN_MAX_ID = 0x7f

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Probe and listen for CANopen')
    parser.add_argument('device', help='link/can network device')
    parser.add_argument('--id', help='our CANopen ID, 0..0x7f',
                        type=lambda x: int(x, 0), default=DEFAULT_NODEID)
    parser.add_argument('--scansdo', help='comma-delimited list of nodes to scan',
                        type=lambda x: x.split(','), default=[])
    parser.add_argument('--oneshot', help='do an active scan, dump results, and exit',
                        action='store_true', dest='oneshot')
    args = parser.parse_args()
    if args.id < 0 or args.id > CANOPEN_MAX_ID:
        raise SystemExit('Invalid node ID: 0x%x' % args.id)
    CanID = args.id
    CanNode = node.Node(args.device)
    scanNodes = []
    scanSet = set(scanNodes)
    if args.scansdo:
        for noderange in args.scansdo:
            try:
                node = int(noderange)
                if node < 0 or node > 0x7f:
                    raise SystemExit('Invalid node ID: 0x%x' % node)
                scanSet.add(node)
            except ValueError:
                rlist = ([int(n) for n in noderange.split('-')])
                if len(rlist) != 2:
                    raise SystemExit('Invalid node ID range: %s' % noderange)
                if rlist[0] < 0 or rlist[1] < 0:
                    raise SystemExit('Invalid node ID range: %s' % noderange)
                if rlist[0] > 0x7f or rlist[1] > 0x7f:
                    raise SystemExit('Invalid node ID range: %s' % noderange)
                if rlist[0] > rlist[1]:
                    raise SystemExit('Invalid node ID range: %s' % noderange)
                r = set(range(rlist[0], rlist[1] + 1))
                scanSet.update(r)
        scanNodes = list(scanSet)
    print('Node scan list:', scanNodes, 'NodeID:', hex(CanID))
    CanNode.NetworkSDOSweep()
    CanNode.Discover()
    if not args.oneshot:
        print('Waiting for signal/keyboard interrupt...')
        signal.pause()
