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

class NodeTest(unittest.TestCase):

    def test_repr(self):
        n0 = node(0, 'i', [], [1])
        print("------ NODE STR ------")
        print(n0)
        print("------ NODE REPR ------")
        print(repr(n0))

    # Tests de copy
    def test_copy(self):
        n0 = node(0, 'i', [], [1])
        n0copy = n0.copy()
        self.assertEqual(n0copy.id, n0.id)
        self.assertEqual(n0copy.label, n0.label)
        self.assertEqual(n0copy.parents, n0.parents)
        self.assertEqual(n0copy.children, n0.children)

    # Tests des getters
    def test_getters(self):
        n0 = node(0, 'i', [], [1])
        self.assertEqual(n0.get_id(), 0)
        self.assertEqual(n0.get_label(), 'i')
        self.assertEqual(n0.get_parent_ids(), [])
        self.assertEqual(n0.get_children_ids(), [1])

    # Tests des setters
    def test_setters(self):
        n0 = node(0, 'i', [], [1])

        n0.set_id(3)
        self.assertEqual(n0.get_id(), 3)

        n0.set_label('j')
        self.assertEqual(n0.get_label(), 'j')

        n0.set_parent_ids([2, 3])
        self.assertEqual(n0.get_parent_ids(), [2, 3])

        n0.set_children_ids([])
        self.assertEqual(n0.get_children_ids(), [])

        n0.add_parent_id(7)
        self.assertEqual(n0.get_parent_ids(), [2, 3, 7])

        n0.add_child_id(8)
        self.assertEqual(n0.get_children_ids(), [8])

class GraphTest(unittest.TestCase):
    def test_repr(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        print("------ GRAPHE STR ------")
        print(g)
        print("------ GRAPHE REPR ------")
        print(repr(g))

    # Tests de Empty
    def test_empty(self):
        g = open_digraph.empty()
        self.assertEqual(open_digraph.empty().inputs, [])
        self.assertEqual(open_digraph.empty().outputs, [])
        self.assertEqual(open_digraph.empty().nodes, {})

    # Tests de copy
    def test_copy(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        gCopy = g.copy()
        self.assertEqual(gCopy.inputs, g.inputs)
        self.assertEqual(gCopy.outputs, g.outputs)
        self.assertEqual(gCopy.nodes, g.nodes)

    # Tests des getters
    def test_getters(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        self.assertEqual(g.get_input_ids(), [1])
        self.assertEqual(g.get_output_ids(), [2])
        #self.assertEqual(g.get_nodes(), n0list)
        self.assertEqual(g.get_node_ids(), [0, 1, 2, 3, 4])
        self.assertEqual(g.get_id_node_map(), {0:n0list[0],
                                               1:n0list[1],
                                               2:n0list[2],
                                               3:n0list[3],
                                               4:n0list[4]})
        self.assertEqual(g.get_node_by_id(3), n0list[3])
        self.assertEqual(g.get_nodes_by_ids([3, 4]), [n0list[3], n0list[4]])

    # Tests des setters
    def test_setters(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        g.set_input_ids([3, 4])
        self.assertEqual(g.get_input_ids(), [3, 4])
        g.set_output_ids([])
        self.assertEqual(g.get_output_ids(), [])
        g.add_input_id(5)
        self.assertEqual(g.get_input_ids(), [3, 4, 5])
        g.add_output_id(2)
        self.assertEqual(g.get_output_ids(), [2])

    def test_new_id(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        id = g.new_id()
        self.assertEqual(g.new_id(), 5)

    def well_formed_test(self):
        n0list = [node(i, '{}'.format(i), [], []) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        self.assertEqual(g.is_well_formed(), True)

        good_list = [node(1, '1', [2, 3], [3]), node(2, '2', [], [1]), node(3, '3', [1], [1])]
        g_good = open_digraph([1], [2], good_list)
        self.assertEqual(g.is_well_formed(), True)

        wrong_list = [node(1, '1', [2, 3], [3]), node(2, '2', [], [1, 2]), node(3, '3', [1], [1])]
        g_good = open_digraph([1], [2], good_list)
        self.assertEqual(g.is_well_formed(), False)

        wrong_list2 = [node(1, '1', [2, 3], [3]), node(2, '2', [], [1]), node(3, '3', [1], [1])]
        g_good = open_digraph([1], [2, 4], good_list)
        self.assertEqual(g.is_well_formed(), False)


if __name__ == '__main__':  # the following code is called only when
    unittest.main()         # precisely this file is run
