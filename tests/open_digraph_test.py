import sys
import unittest
import data
sys.path.append('../')  # allows us to fetch files from the project root
from modules.open_digraph import *
from modules.utils import *


class InitTest(unittest.TestCase):

    # Test of node initialization
    def test_init_node(self):
        # A node should have 4 parameters :
        #    - an Id (int)
        #    - a label (string)
        #    - some parents (a list)
        #    - some children (a list)

        # Node initialization :
        n0 = node(0, 'i', [], [1])

        # Checking values
        self.assertEqual(n0.id, 0)
        self.assertEqual(n0.label, 'i')
        self.assertEqual(n0.parents, [])
        self.assertEqual(n0.children, [1])

        # Checking type
        self.assertIsInstance(n0, node)

    # Test of graph initialization
    def test_init_open_digraph(self):
        # A graph should have 3 parameters :
        #    - some inputs (from the external world)
        #    - some outputs (to external world)
        #    - a list of the nodes inside the graph

        # Node list of the graph initialization
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        # Graph initialization
        g = open_digraph([1], [2], n0list)

        # Checking values
        self.assertEqual(g.nodes[0], n0list[0])
        self.assertEqual(g.inputs, [1])
        self.assertEqual(g.outputs, [2])

        # Checking types
        self.assertIsInstance(g, open_digraph)
        self.assertIsInstance(n0list[0], node)


class NodeTest(unittest.TestCase):

    # Test of node representation
    def test_repr(self):
        # Nodes should be printable for graph visualization

        # Node sample example initialization
        n0 = node(0, 'i', [], [1])

        # Representation of the node in a printable way
        '''
        print("------ NODE STR ------")
        print(n0)
        print("------ NODE REPR ------")
        print(repr(n0))
        '''
        # Note : feel free to uncomment those lines
        # if you want to check how it is represented

    # Test of graph copy management
    def test_copy(self):
        # A copy of the node should have
        # the same values BUT not be identical inside the memory

        # Node initialization
        n0 = node(0, 'i', [], [1])
        # Creating a copy
        n0copy = n0.copy()

        # Checking values
        self.assertEqual(n0copy.id, n0.id)
        self.assertEqual(n0copy.label, n0.label)
        self.assertEqual(n0copy.parents, n0.parents)
        self.assertEqual(n0copy.children, n0.children)

        # Checking that n0 modifications does not
        # affect n0copy values
        # Id :
        n0.id = 2
        self.assertEqual(n0copy.id, 0)
        # Label :
        n0.label = 'k'
        self.assertEqual(n0copy.label, 'i')
        # Parents :
        n0.parents = [2]
        self.assertEqual(n0copy.parents, [])
        # Children :
        n0.children = []
        self.assertEqual(n0copy.children, [1])

    # Test of node getters
    def test_getters(self):
        # Getters are useful functions
        # to encapsulate our classes
        # and access values without knowing
        # how it is actually represented in our class

        # Node initialization
        n0 = node(0, 'i', [], [1])
        # We can access to every value by a function
        # Id :
        self.assertEqual(n0.get_id(), 0)
        # Label :
        self.assertEqual(n0.get_label(), 'i')
        # Parents :
        self.assertEqual(n0.get_parent_ids(), [])
        # Children :
        self.assertEqual(n0.get_children_ids(), [1])

    # Test of node setters
    def test_setters(self):
        # Setters are useful functions
        # to encapsulate our classes
        # and modify values without knowing
        # how it is actually represented in our class

        # Node initialization
        n0 = node(0, 'i', [], [1])

        # Id modification
        self.assertEqual(n0.get_id(), 0)
        n0.set_id(3)
        self.assertEqual(n0.get_id(), 3)

        # Label modification
        self.assertEqual(n0.get_label(), 'i')
        n0.set_label('j')
        self.assertEqual(n0.get_label(), 'j')

        # Parents modification
        self.assertEqual(n0.get_parent_ids(), [])
        n0.set_parent_ids([2, 3]) # Setting
        self.assertEqual(n0.get_parent_ids(), [2, 3])
        n0.add_parent_id(7) # Adding
        self.assertEqual(n0.get_parent_ids(), [2, 3, 7])
        n0.remove_parent_id(7) # Removing
        self.assertEqual(n0.get_parent_ids(), [2, 3])

        # Children modification
        self.assertEqual(n0.get_children_ids(), [1])
        n0.set_children_ids([]) # Setting
        self.assertEqual(n0.get_children_ids(), [])
        n0.add_child_id(8) # Adding
        self.assertEqual(n0.get_children_ids(), [8])
        n0.remove_child_id(8) # Removing
        self.assertEqual(n0.get_children_ids(), [])

    # Test of indegree calculation
    def test_indegree(self):
        # The indegree of the node is the number
        # of inputs it has

        # We load nodes examples
        node1, node2 = data.exemples_de_node()

        # Checking that indegree are coherent with reality
        self.assertEqual(node1.indegree(), 0)
        self.assertEqual(node2.indegree(), 2)

    # Test of outdegree calculation
    def test_outdegree(self):
        # The outdegree of the node is the number
        # of outputs it has

        # We load nodes examples
        node1, node2 = data.exemples_de_node()

        # Checking that outdegree are coherent with reality
        self.assertEqual(node1.outdegree(), 7)
        self.assertEqual(node2.outdegree(), 4)

    # Test of degree calculation
    def test_degree(self):
        # The degree of the node is the number
        # of outputs and inputs  it has

        # We load nodes examples
        node1, node2 = data.exemples_de_node()

        # Checking that degree are coherent with reality
        self.assertEqual(node1.degree(), node1.indegree() + node1.outdegree())
        self.assertEqual(node1.degree(), 7)
        self.assertEqual(node2.degree(), node2.indegree() + node2.outdegree())
        self.assertEqual(node2.degree(), 6)


class GraphTest(unittest.TestCase):

    # Test of graph representation
    def test_repr(self):
        # Graph should be printable for visualization

        # Node example initialization
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        # Graph initialization
        g = open_digraph([1], [2], n0list)

        # Representation of the graph in a printable way
        '''
        print("------ GRAPHE STR ------")
        print(g)
        print("------ GRAPHE REPR ------")
        print(repr(g))
        '''
        # Note : feel free to uncomment those lines
        # if you want to check how it is represented

    # Test of empty graph generation
    def test_empty(self):
        # An empty graph should be empty, without
        # any node and any imput nor output

        # Loading an empty graph
        g = open_digraph.empty()

        # Checking type
        self.assertIsInstance(g, open_digraph)

        # Checking values
        self.assertEqual(g.inputs, [])
        self.assertEqual(g.outputs, [])
        self.assertEqual(g.nodes, {})

    # Test of graph copy management
    def test_copy(self):
        # A copy of the graph should have
        # the same values BUT not be identical inside the memory

        # Node list initialization
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        # Graph initialization
        g = open_digraph([1], [2], n0list)

        # Creating a copy of the graph
        gCopy = g.copy()

        # Checking that values are the same
        self.assertEqual(gCopy.inputs, g.inputs)
        self.assertEqual(gCopy.outputs, g.outputs)
        self.assertEqual(len(gCopy.get_nodes()), len(g.get_nodes()))

        # Checking that modifications does not affect the copy
        # Inputs :
        g.inputs = [2, 3]
        self.assertEqual(gCopy.inputs, [1])
        # Outputs :
        g.outputs = []
        self.assertEqual(gCopy.outputs, [2])
        # Nodes :
        g.nodes = {}
        self.assertEqual(len(gCopy.get_nodes()), len(n0list))

    # Test of graph getters
    def test_getters(self):
        # Getters are useful functions
        # to encapsulate our classes
        # and access values without knowing
        # how it is actually represented in our class

        # Node list initialization
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        # Graph initialization
        g = open_digraph([1], [2], n0list)

        # We can access values by a function
        # Inputs :
        self.assertEqual(g.get_input_ids(), [1])
        # Outputs :
        self.assertEqual(g.get_output_ids(), [2])
        # Nodes :
        self.assertEqual(g.get_nodes(), n0list)
        # Nodes ids :
        self.assertEqual(g.get_node_ids(), [0, 1, 2, 3, 4])
        # Nodes by a map of their ids :
        self.assertEqual(g.get_id_node_map(), {0: n0list[0],
                                               1: n0list[1],
                                               2: n0list[2],
                                               3: n0list[3],
                                               4: n0list[4]})
        # Node by its id :
        self.assertEqual(g.get_node_by_id(3), n0list[3])
        # Nodes by their ids :
        self.assertEqual(g.get_nodes_by_ids([3, 4]), [n0list[3], n0list[4]])

    # Test of graph setters
    def test_setters(self):
        # Setters are useful functions
        # to encapsulate our classes
        # and modify values without knowing
        # how it is actually represented in our class

        # Nodes initialization
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        # Graph initialization
        g = open_digraph([1], [2], n0list)

        # Input modification
        self.assertEqual(g.get_input_ids(), [1])
        g.set_input_ids([3, 4]) # Setting
        self.assertEqual(g.get_input_ids(), [3, 4])
        g.add_input_id(5) # Adding
        self.assertEqual(g.get_input_ids(), [3, 4, 5])

        # Output modification
        self.assertEqual(g.get_output_ids(), [2])
        g.set_output_ids([]) # Setting
        self.assertEqual(g.get_output_ids(), [])
        g.add_output_id(2) # Adding
        self.assertEqual(g.get_output_ids(), [2])

    # Test of new id generation
    def test_new_id(self):
        # This functions should return the first positive id
        # that is not in the graph

        # Nodes initialization
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        n1list = [node(i, '{}'.format(i), [], [1]) for i in range(0, 5, 2)]
        # Graph initialization
        g = open_digraph([1], [2], n0list)
        g1 = open_digraph([1], [2], n1list)

        # Getting a new id
        id = g.new_id()
        id1 = g1.new_id()

        # Checking that results are coherent with reality
        self.assertEqual(g.new_id(), 5)
        self.assertEqual(g1.new_id(), 1)

    # Test of edge management
    def test_edges_management(self):
        n0list = [node(i, '{}'.format(i), [], []) for i in range(5)]
        g = open_digraph([1], [2], n0list)

        g.add_edge(2, 3)
        self.assertEqual(g.get_node_by_id(3).get_parent_ids(), [2])
        self.assertEqual(g.get_node_by_id(2).get_children_ids(), [3])
        g.remove_edge(2, 3)
        self.assertEqual(g.get_node_by_id(3).get_parent_ids(), [])
        self.assertEqual(g.get_node_by_id(2).get_children_ids(), [])

        g.add_edges([2, 3], [1, 4])
        self.assertEqual(g.get_node_by_id(1).get_parent_ids(), [2])
        self.assertEqual(g.get_node_by_id(3).get_children_ids(), [4])

        g.add_edge(2, 1)
        g.remove_edges([2, 3], [1, 4])
        self.assertEqual(g.get_node_by_id(1).get_parent_ids(), [])

        g.add_node()
        self.assertEqual(g.get_node_ids(), [0, 1, 2, 3, 4, 5])

        g.remove_node_by_id(4)
        self.assertEqual(g.get_node_ids(), [0, 1, 2, 3, 5])
        g.remove_nodes_by_id([2, 3, 4, 5])
        self.assertEqual(g.get_node_ids(), [0, 1])

    # Test of well forming checking
    def test_well_formed(self):
        n0list = [node(i, '{}'.format(i), [], []) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        self.assertEqual(g.is_well_formed(), True)

        good_list = [node(1, '1', [2, 3], [3]),
                     node(2, '2', [], [1]),
                     node(3, '3', [1], [1])]
        g_good = open_digraph([1], [2], good_list)
        self.assertEqual(g_good.is_well_formed(), True)

        wrong_list = [node(1, '1', [2, 3], [3]),
                      node(2, '2', [], [1, 2]),
                      node(3, '3', [1], [1])]
        g_wrong = open_digraph([1], [2], wrong_list)
        self.assertEqual(g_wrong.is_well_formed(), False)

        wrong_list2 = [node(1, '1', [2, 3], [3]),
                       node(2, '2', [], [1]),
                       node(3, '3', [1], [1])]
        g_wrong2 = open_digraph([1], [2, 4], wrong_list2)
        self.assertEqual(g_wrong2.is_well_formed(), False)

    # Test of graph normalization
    def test_normalize(self):
        good_list = [node(1, '1', [2, 3], [3]),
                     node(2, '2', [], [1]),
                     node(3, '3', [1], [1])]
        g_good = open_digraph([1], [2], good_list)
        matrix = g_good.adjacency_matrix()

    # ----- Test of degree checking -----
    # MAX IN
    def test_max_indegree(self):
        g = data.boolean_graph()
        self.assertEqual(g.max_indegree(), 2)
        h = data.cyclic_not_well_formed()
        self.assertEqual(h.max_indegree(), 4)

    # MIN IN
    def test_min_indegree(self):
        g = data.boolean_graph()
        self.assertEqual(g.min_indegree(), 1)
        h = data.cyclic_not_well_formed()
        self.assertEqual(h.min_indegree(), 0)

    # MAX OUT
    def test_max_outdegree(self):
        g = data.boolean_graph()
        self.assertEqual(g.max_outdegree(), 2)
        h = data.cyclic_not_well_formed()
        self.assertEqual(h.max_outdegree(), 2)

    # MIN OUT
    def test_min_outdegree(self):
        g = data.boolean_graph()
        self.assertEqual(g.min_outdegree(), 1)
        h = data.cyclic_not_well_formed()
        self.assertEqual(h.min_outdegree(), 1)

    # Test of cyclicity checking
    def test_is_cyclic(self):
        g = data.boolean_graph()
        self.assertEqual(g.is_cyclic(), False)
        h = data.cyclic_not_well_formed()
        self.assertEqual(h.is_cyclic(), True)

    # ----- Test of id value checking -----
    # MIN
    def test_min_id(self):
        g = data.boolean_graph()
        self.assertEqual(g.min_id(), 0)
        h = data.cyclic_not_well_formed()
        self.assertEqual(h.min_id(), 5)

    # MAX
    def test_max_id(self):
        g = data.boolean_graph()
        self.assertEqual(g.max_id(), 4)
        h = data.cyclic_not_well_formed()
        self.assertEqual(h.max_id(), 8)

    # Test of indice shifting management
    def test_shift_indices(self):
        g = data.boolean_graph()
        g.shift_indices(3)
        self.assertEqual(g.min_id(), 3)
        self.assertEqual(g.max_id(), 7)
        h = data.cyclic_not_well_formed()
        h.shift_indices(100)
        self.assertEqual(h.min_id(), 105)
        self.assertEqual(h.max_id(), 108)

    # Test of parallization (fusion) of graphs
    # With modifications of the graph :
    def test_iparallel(self):
        g = data.boolean_graph()
        h = data.cyclic_not_well_formed()
        inputs = g.get_input_ids()
        g.iparallel(h)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8], g.get_node_ids())
        self.assertEqual([0, 2, 5, 5, 6], g.get_input_ids())

    # Without modifications of the graph :
    def test_parallel(self):
        g = data.boolean_graph()
        h = data.cyclic_not_well_formed()
        test = g.parallel(h, [3], [7])
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8], test.get_node_ids())

    # Test of composition (fusion with links) of graphs
    # With modifications of the graph :
    def test_icompose(self):
        g = data.boolean_graph()
        h = data.cyclic_not_well_formed()
        h.icompose(g)
        self.assertEqual(h.get_input_ids(), [5, 5, 6])
        self.assertEqual(h.get_output_ids(), [1, 4])
        self.assertEqual(h.get_node_by_id(5).get_children_ids(), [0, 6])
        self.assertEqual(h.get_node_by_id(7).get_children_ids(), [2])
        self.assertEqual(h.get_node_by_id(0).get_parent_ids(), [5])
        self.assertEqual(h.get_node_by_id(2).get_parent_ids(), [7])

    # Without modifications of the graph :
    def test_compose(self):
        g = data.boolean_graph()
        h = data.cyclic_not_well_formed()
        test = h.compose(g)
        self.assertEqual(test.get_input_ids(), [5, 5, 6])
        self.assertEqual(test.get_output_ids(), [1, 4])
        self.assertEqual(test.get_node_by_id(5).get_children_ids(), [0, 6])
        self.assertEqual(test.get_node_by_id(7).get_children_ids(), [2])
        self.assertEqual(test.get_node_by_id(0).get_parent_ids(), [5])
        self.assertEqual(test.get_node_by_id(2).get_parent_ids(), [7])

    # Test of connected components of a graph management
    def test_connected_components(self):
        g = data.composed_graph()
        nodes = g.get_node_ids()
        connexe, components = g.connected_components()
        self.assertEqual(connexe, 5)
        self.assertEqual(components[1], 0)
        self.assertEqual(components[2], 0)
        self.assertEqual(components[3], 1)
        self.assertEqual(components[4], 2)
        self.assertEqual(components[5], 3)
        self.assertEqual(components[6], 3)
        self.assertEqual(components[7], 3)
        self.assertEqual(components[8], 4)
        self.assertEqual(components[9], 4)
        self.assertEqual(components[10], 4)
        self.assertEqual(components[11], 4)

    # Test of graph permutations management
    def test_graph_permutation(self):
        g = data.composed_graph()
        components, inputs, outputs = g.graph_permutation()
        self.assertEqual(inputs, [1, 3])
        self.assertEqual(outputs, [2, 3])
        self.assertEqual(components[0].get_node_ids(), [1, 2])
        self.assertEqual(components[1].get_node_ids(), [3])
        self.assertEqual(components[2].get_node_ids(), [4])
        self.assertEqual(components[3].get_node_ids(), [5, 7, 6])
        self.assertEqual(components[4].get_node_ids(), [8, 10, 9, 11])

    # Test of shortest path between two nodes calculation
    def test_shortest_path(self):
        g = data.normal_graph()
        n0 = g.get_node_by_id(0)
        n3 = g.get_node_by_id(3)
        n7 = g.get_node_by_id(7)
        self.assertEqual(g.shortest_path(n0, n3), [0, 3])
        self.assertEqual(g.shortest_path(n0, n7), [0, 3, 7])

    # Test of parents distance calculation
    def test_parents_distance(self):
        g = data.normal_graph()
        distance = g.parents_distance(g.get_node_by_id(5), g.get_node_by_id(8))
        self.assertEqual(distance, {0: (2, 3), 3: (1, 2), 1: (1, 1)})

    # Test of topological sorting of a graph
    def test_topological_sorting(self):
        g = data.normal_graph()
        top_sort = g.topological_sorting()
        self.assertEqual(top_sort, [[0, 1, 2], [3, 4], [5, 6], [7, 8, 9]])

    # Test of node depth calculation
    def test_node_depth(self):
        g = data.normal_graph()
        self.assertEqual(g.node_depth(g.get_node_by_id(0)), 0)
        self.assertEqual(g.node_depth(g.get_node_by_id(4)), 1)
        self.assertEqual(g.node_depth(g.get_node_by_id(5)), 2)
        self.assertEqual(g.node_depth(g.get_node_by_id(7)), 3)

    # Test of graph depth calculation
    def test_graph_depth(self):
        g = data.normal_graph()
        self.assertEqual(g.graph_depth(), 4)

    # Test of longest path between two nodes calculation
    def test_longest_path(self):
        g = data.normal_graph()
        n0 = g.get_node_by_id(0)
        n3 = g.get_node_by_id(3)
        n5 = g.get_node_by_id(5)
        n7 = g.get_node_by_id(7)
        chemin, distance = g.longest_path(n0, n7)
        self.assertEqual(chemin, [0, 3, 5, 7])
        self.assertEqual(distance, 4)


class BoolCircTest(unittest.TestCase):

    # Test of boolean circuit initialization
    def test_init(self):
        node1 = node(0, '',  [],     [1, 3])
        node2 = node(1, '&', [0, 2], [])
        node3 = node(2, '',  [],     [1, 3])
        node4 = node(3, '|', [0, 2], [4])
        node5 = node(4, '~', [3],    [])
        nodelist = [node1, node2, node3, node4, node5]
        g = open_digraph([0, 2], [1, 4], nodelist)
        b1 = bool_circ(g, check=False)

        self.assertEqual(b1.get_input_ids(), [0, 2])
        self.assertEqual(b1.get_output_ids(), [1, 4])
        self.assertEqual(b1.get_nodes(), nodelist)

        node6 = node(5, '&', [6, 8], [6])
        node7 = node(6, '~', [5],    [5, 7])
        node8 = node(7, '&', [6],    [])
        node9 = node(8, '',  [],     [5])
        nodelist2 = [node6, node7, node8, node9]
        h = open_digraph([5, 5, 6], [5, 7], nodelist2)
        b2 = bool_circ(h, check=False)

        self.assertEqual(b2.get_input_ids(), [5, 5, 6])
        self.assertEqual(b2.get_output_ids(), [5, 7])
        self.assertEqual(b2.get_nodes(), nodelist2)

    # Test of graph convertion management
    def test_to_graph(self):

        # Creation of open_digraphs
        g1 = data.boolean_graph()
        g2 = data.cyclic_not_well_formed()
        g3 = data.cyclic_graph()
        g4 = data.not_well_formed()

        # Creation of the bool_circ from the open_digraphs
        b1 = bool_circ(g1, check=False)
        b2 = bool_circ(g2, check=False)
        b3 = bool_circ(g3, check=False)
        b4 = bool_circ(g4, check=False)
        # Convertion of the bool_circs into open_digraphs
        b1.to_graph()
        b2.to_graph()
        b3.to_graph()
        b4.to_graph()
        # Test the equalities
        self.assertEqual(b1, g1)
        self.assertEqual(b2, g2)
        self.assertEqual(b3, g3)
        self.assertEqual(b4, g4)

    # Test of circuit's validity checking
    def test_is_well_formed(self):

        # Creation of open_digraphs
        g1 = data.boolean_graph()
        g2 = data.cyclic_not_well_formed()
        g3 = data.cyclic_graph()
        g4 = data.not_well_formed()

        # On teste si l'appel de bool_circ
        # print un message d'erreur ou non (il faudra
        # remplacer par des Raise)
        b1 = bool_circ(g1)  # On n'a pas de message d'erreur
        print("We'll have 3 error messages : ")
        b2 = bool_circ(g2)  # On a bien un message d'erreur
        b3 = bool_circ(g3)  # On a bien un message d'erreur
        b4 = bool_circ(g4)  # On a bien un message d'erreur

    '''Test TD10'''
    def test_random_bool_circ(self):
        pass


if __name__ == '__main__':  # the following code is called only when
    unittest.main()         # precisely this file is run
