import canopen

class Node(object):
    """CANopen node bound to some device"""

    def __init__(self, dev):
        network = canopen.Network()
        network.connect(bustype='socketcan', channel=dev)
