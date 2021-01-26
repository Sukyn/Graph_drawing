import sys
sys.path.append('../')# allows us to fetch files from the project root
import unittest
from modules.open_digraph import *


class InitTest(unittest.TestCase):
    def test_init_node(self):
        n0 = node(0, 'i', [], [1])
        self.assertEqual(n0.id, 0)
        self.assertEqual(n0.label, 'i')
        self.assertEqual(n0.parents, [])
        self.assertEqual(n0.children, [1])
        self.assertIsInstance(n0, node)
    def test_init_open_digraph(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        self.assertEqual(g.nodes[0], n0list[0])
        self.assertEqual(g.inputs, [1])
        self.assertEqual(g.outputs, [2])
        self.assertIsInstance(g, open_digraph)
        self.assertIsInstance(n0list[0], node)

if __name__ == '__main__':  # the following code is called only when
    unittest.main()         # precisely this file is run
