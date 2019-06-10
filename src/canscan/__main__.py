#!/usr/bin/env python

# canScan - CANopen discovery/scanning tool
#
# https://github.com/dankamongmen/canscan

from __future__ import print_function
import canopen.node
import signal
import argparse

DEFAULT_NODEID = 0x64
CANOPEN_MAX_ID = 0x7f

def ExtractRangeList(s):
    """Extracts a comma-delimited list of hyphen-delimited ranges, or single
       integers, i.e. '2,0xA,0x40-96'. Returns a populated list."""
    ranges = list(s.split(","))
    newRange = []
    for r in ranges:
        if r=='':
            continue
        subRange = ([int(n, 0) for n in r.split('-')])
        if (len(subRange) > 1):
            newRange.extend(range(subRange[0], subRange[1] + 1))
        else:
            newRange.extend(subRange)
    newRange.sort()
    return newRange

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Probe and listen for CANopen')
    # The device changes depending on the backing python-can driver. For
    # socketcan, you want the network device name. For canalystii, USB devindex.
    parser.add_argument('bustype', help='specify bustype (see python-can)')
    parser.add_argument('device', help='can device identifier (per-bus semantics)')
    parser.add_argument('--id', help='our CANopen ID, 0..0x7f',
                        type=lambda x: int(x, 0), default=DEFAULT_NODEID)
    parser.add_argument('--ods', help='Object Dictionary indexes to scan',
                        type=ExtractRangeList, default=[])
    parser.add_argument('--scan', help='comma-delimited list of nodes to scan',
                        type=lambda x: x.split(','), default=[])
    parser.add_argument('--channel', help='channel, if appropriate', type=int)
    parser.add_argument('--passive', help='do not transmit any frames',
                        action='store_true', dest='passive')
    parser.add_argument('--oneshot', help='do an active scan, dump results, and exit',
                        action='store_true', dest='oneshot')
    args = parser.parse_args()
    if args.id < 0 or args.id > CANOPEN_MAX_ID:
        raise SystemExit('Invalid node ID: 0x%x' % args.id)
    CanID = args.id
    CanNode = node.Node(dev=args.device, bustype=args.bustype, channel=args.channel)
    scanNodes = []
    scanSet = set(scanNodes)
    if args.scan:
        for noderange in args.scan:
            try:
                node = int(noderange, 0)
                if node < 0 or node > 0x7f:
                    raise SystemExit('Invalid node ID: 0x%x' % node)
                scanSet.add(node)
            except ValueError:
                rlist = ([int(n, 0) for n in noderange.split('-')])
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
    if args.passive:
        if args.oneshot:
            raise SystemExit("--oneshot doesn't make sense with --passive, exiting")
        if len(scanNodes):
            raise SystemExit("--scan doesn't make sense with --passive, exiting")
    print('Bus:', args.bustype, 'NodeID:', hex(CanID), 'Node scan list:', scanNodes)
    CanNode.NetworkSDOSweep()
    if not args.passive:
        CanNode.Discover()
    if not args.oneshot:
        print('Waiting for signal/keyboard interrupt...')
        try:
            signal.pause()
        except KeyboardInterrupt:
            exit(0)
