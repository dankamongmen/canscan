import canopen

OD_IDENTITY = 0x1018
OD_IDENTITY_VENDORID = 0x1

class Node(object):
    """CANopen node bound to some device"""

    def __init__(self, dev):
        self.network = canopen.Network()
        self.network.connect(bustype='socketcan', channel=dev)

    def __del__(self):
        print("Disconnecting from CAN...")
        self.network.disconnect()

    def CheckNodeSDO(self, nodeid):
        """Hit some node (7-bit Node ID) with a quick Vendor Identity SDO."""
        node = canopen.RemoteNode(6)
        vendor_id = node.sdo[OD_IDENTITY][OD_IDENTITY_VENDORID].raw

    def NetworkSDOSweep(self):
        """Use python-canopen's inflexible SDO search."""
        self.network.scanner.search()

    def Discover(self):
        """Listen for traffic identifying CANopen nodes. FIXME"""
