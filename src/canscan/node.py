import canopen

OD_IDENTITY = 0x1018
OD_IDENTITY_VENDORID = 0x1

class Node(object):
    """CANopen node bound to some device"""

    def __init__(self, dev):
        network = canopen.Network()
        network.connect(bustype='socketcan', channel=dev)

    def CheckNodeSDO(self, nodeid):
        """Hit some node (7-bit Node ID) with a quick Vendor Identity SDO."""
        node = canopen.RemoteNode(6)
        vendor_id = node.sdo[OD_IDENTITY][OD_IDENTITY_VENDORID].raw
