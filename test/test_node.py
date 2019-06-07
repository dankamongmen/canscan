import unittest
import canscan.node

class TestNode(unittest.TestCase):

    def test_node_lifetime(self):
        node = canscan.node.Node()
