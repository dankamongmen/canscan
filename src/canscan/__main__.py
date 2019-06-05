#!/usr/bin/env python

# canScan - CANopen discovery/scanning tool
#
# https://github.com/dankamongmen/canscan

import node
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Probe and listen for CANopen')
    parser.add_argument('device', help='link/can network device')
    args = parser.parse_args()
    node.Node(args.device)
