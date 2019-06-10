import unittest
import canscan.__main__

class TestExtractRangeList(unittest.TestCase):

    def test_empty_arg(self):
        nodes = canscan.__main__.ExtractRangeList('')
        self.assertEqual(nodes, [])

    def test_trivial_dec_arg(self):
        nodes = canscan.__main__.ExtractRangeList('1')
        self.assertEqual(nodes, [1])

    def test_trivial_hex_arg(self):
        nodes = canscan.__main__.ExtractRangeList('0xffff')
        self.assertEqual(nodes, [0xffff])

    def test_complete_list(self):
        nodes = canscan.__main__.ExtractRangeList('0x0-0xffff')
        self.assertEqual(nodes, list(range(0x10000)))

    def test_complete_list_union(self):
        nodes = canscan.__main__.ExtractRangeList('0x0-0x7fff,0x8000-0xffff')
        self.assertEqual(nodes, list(range(0x10000)))

    def test_cut_list(self):
        nodes = canscan.__main__.ExtractRangeList('0x0-0x7fff,0x8001-0xffff')
        self.assertEqual(nodes, [n for n in range(0, 0x10000) if n != 0x8000])

    def test_sparse_list(self):
        nodes = canscan.__main__.ExtractRangeList('0x1000,0x8000,0xf000')
        self.assertEqual(nodes, [0x1000, 0x8000, 0xf000])
