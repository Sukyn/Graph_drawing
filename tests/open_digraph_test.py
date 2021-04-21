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

    # Test of boolean circuit initialization
    def test_init_bool_birc(self):
        # A boolean circuit is a graph
        # with some particularities
        # '' are input nodes
        # '&' are AND nodes
        # '|' are OR nodes
        # '~ are NOT nodes
        # It allows us to make logical phrases'

        # Nodes initialization
        node1 = node(0, '',  [],     [1, 3])
        node2 = node(1, '&', [0, 2], [])
        node3 = node(2, '',  [],     [1, 3])
        node4 = node(3, '|', [0, 2], [4])
        node5 = node(4, '~', [3],    [])
        nodelist = [node1, node2, node3, node4, node5]
        # Graph initialization
        g = open_digraph([0, 2], [1, 4], nodelist)
        # Boolean circuit conversion
        b1 = bool_circ(g)

        # Checking values
        self.assertEqual(b1.get_input_ids(), [0, 2])
        self.assertEqual(b1.get_output_ids(), [1, 4])
        self.assertEqual(b1.get_nodes(), nodelist)

        # here is another example...
        node6 = node(5, '&', [6, 8], [6])
        node7 = node(6, '~', [5],    [5, 7])
        node8 = node(7, '&', [6],    [])
        node9 = node(8, '',  [],     [5])
        nodelist2 = [node6, node7, node8, node9]
        h = open_digraph([5, 5, 6], [5, 7], nodelist2)
        # But this one is **not** a valid boolean circuit
        # If we want to force its creation, we can put the check argument
        # as false, it will create it but it should not be
        # manipulated afterwards !!
        b2 = bool_circ(h, check=False)

        # Checking values
        self.assertEqual(b2.get_input_ids(), [5, 5, 6])
        self.assertEqual(b2.get_output_ids(), [5, 7])
        self.assertEqual(b2.get_nodes(), nodelist2)


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
        # An edge between two nodes can be
        # represented as on oriented arrow from
        # a parent node to a child node

        # Nodes initialization
        n0list = [node(i, '{}'.format(i), [], []) for i in range(5)]
        # Graph initialization
        g = open_digraph([1], [2], n0list)

        # Checking edges management
        # Initial state :
        self.assertEqual(g.get_node_by_id(3).get_parent_ids(), [])
        self.assertEqual(g.get_node_by_id(2).get_children_ids(), [])
        # Adding an edge :
        g.add_edge(2, 3)
        self.assertEqual(g.get_node_by_id(3).get_parent_ids(), [2])
        self.assertEqual(g.get_node_by_id(2).get_children_ids(), [3])
        # Removing an edge :
        g.remove_edge(2, 3)
        self.assertEqual(g.get_node_by_id(3).get_parent_ids(), [])
        self.assertEqual(g.get_node_by_id(2).get_children_ids(), [])
        # Adding several edges :
        g.add_edges([2, 3], [1, 4])
        self.assertEqual(g.get_node_by_id(1).get_parent_ids(), [2])
        self.assertEqual(g.get_node_by_id(3).get_children_ids(), [4])
        self.assertEqual(g.get_node_by_id(4).get_parent_ids(), [3])
        self.assertEqual(g.get_node_by_id(2).get_children_ids(), [1])
        # Removing several edges :
        g.remove_edges([2, 3], [1, 4])
        self.assertEqual(g.get_node_by_id(1).get_parent_ids(), [])
        self.assertEqual(g.get_node_by_id(4).get_parent_ids(), [])
        self.assertEqual(g.get_node_by_id(3).get_children_ids(), [])
        self.assertEqual(g.get_node_by_id(2).get_children_ids(), [])
        # Note : It should also remove several edges from a node to another
        g.add_edges([2, 3], [1, 4])
        g.add_edge(2, 1)
        g.remove_edges([2, 3], [1, 4])
        self.assertEqual(g.get_node_by_id(1).get_parent_ids(), [])
        self.assertEqual(g.get_node_by_id(4).get_parent_ids(), [])
        self.assertEqual(g.get_node_by_id(3).get_children_ids(), [])
        self.assertEqual(g.get_node_by_id(2).get_children_ids(), [])

    # Test of node management
    def test_node_management(self):
        # We should be able to add and delete
        # nodes of the graph

        # Nodes initialization
        n0list = [node(i, '{}'.format(i), [], []) for i in range(5)]
        # Graph initialization
        g = open_digraph([1], [2], n0list)

        # Initial state
        self.assertEqual(g.get_node_ids(), [0, 1, 2, 3, 4])
        # We add a new node, it calls the "new_id()" method
        # so the new node should have an id that is the first
        # positive integer not attributed
        g.add_node()
        self.assertEqual(g.get_node_ids(), [0, 1, 2, 3, 4, 5])

        # Removing a node
        g.remove_node_by_id(4)
        self.assertEqual(g.get_node_ids(), [0, 1, 2, 3, 5])
        # Removing several nodes
        g.remove_nodes_by_id([2, 3, 4, 5])
        self.assertEqual(g.get_node_ids(), [0, 1])

    # Test of well forming checking
    def test_well_formed(self):
        # A graph is well formed if for any node A that
        # is the parent of node B, then node B is a
        # child of node A.
        # Inputs and outputs should be linked to
        # existing nodes of the graph
        # (And some other class particularities)

        # Nodes initialization
        n0list = [node(i, '{}'.format(i), [], []) for i in range(5)]
        # Graph initialization
        g = open_digraph([1], [2], n0list)

        # There are no edges in this graph
        # It should be well formed
        self.assertEqual(g.is_well_formed(), True)

        # Well formed graph initialization
        # Nodes
        good_list = [node(1, '1', [2, 3], [3]),
                     node(2, '2', [], [1]),
                     node(3, '3', [1], [1])]
        # Graph
        g_good = open_digraph([1], [2], good_list)
        # We can see that the validity condition is respected
        # so it should be a well formed graph
        self.assertEqual(g_good.is_well_formed(), True)

        # Not well formed graph initialization
        # Nodes
        wrong_list = [node(1, '1', [2, 3], [3]),
                      node(2, '2', [], [1, 2]),
                      node(3, '3', [1], [1])]
        # Graph
        g_wrong = open_digraph([1], [2], wrong_list)
        # We can see that 2 is a child of 2, but there is no
        # 2 in its parents
        # the graph should not be well formed !
        self.assertEqual(g_wrong.is_well_formed(), False)

        # ANother example of not well formed graph initialization
        # Nodes
        wrong_list2 = [node(1, '1', [2, 3], [3]),
                       node(2, '2', [], [1]),
                       node(3, '3', [1], [1])]
        # Graph
        g_wrong2 = open_digraph([1], [2, 4], wrong_list2)
        # We can see that there is an output from 4, but there
        # is no node with 4 id in the graph
        # it should not be well formed
        self.assertEqual(g_wrong2.is_well_formed(), False)

    # Test of graph normalization
    def test_normalize(self):
        # A normalized graph is a graph of which ids
        # are the first n positive or null integers where n is the
        # number of nodes in the graph

        # Nodes initialization
        node_list = [node(1, '1', [2, 3], [3]),
                     node(2, '2', [], [1]),
                     node(3, '3', [1], [1])]
        # Graph initialization
        g_good = open_digraph([1], [2], node_list)
        # Our graph has 1,2,3 as ids,
        # after a normalization it should be 0,1,2
        # but with the exact same properties
        matrix = g_good.adjacency_matrix()
        '''
        # TO DO ------
        # TO DO ------
        # TO DO ------
        # TO DO ------
        # TO DO ------
        # TO DO -----
        # TO DO -----
        # TO DO -----
        '''

    # ----- Test of degree checking -----
    # MAX IN
    def test_max_indegree(self):
        # The max indegree of a graph is the maximum
        # of each node's indegree

        # We load an example graph
        g = data.boolean_graph()
        self.assertEqual(g.max_indegree(), 2)
        h = data.cyclic_not_well_formed()
        self.assertEqual(h.max_indegree(), 4)

    # MIN IN
    def test_min_indegree(self):
        # The min indegree of a graph is the minimum
        # of each node's indegree

        # We load an example graph
        g = data.boolean_graph()
        self.assertEqual(g.min_indegree(), 1)
        # We load another example graph
        h = data.cyclic_not_well_formed()
        self.assertEqual(h.min_indegree(), 0)

    # MAX OUT
    def test_max_outdegree(self):
        # The max outdegree of a graph is the maximum
        # of each node's outdegree

        # We load an example graph
        g = data.boolean_graph()
        self.assertEqual(g.max_outdegree(), 2)
        # We load another example graph
        h = data.cyclic_not_well_formed()
        self.assertEqual(h.max_outdegree(), 2)

    # MIN OUT
    def test_min_outdegree(self):
        # The min outdegree of a graph is the minimum
        # of each node's outdegree

        # We load an example graph
        g = data.boolean_graph()
        self.assertEqual(g.min_outdegree(), 1)
        # We load another example graph
        h = data.cyclic_not_well_formed()
        self.assertEqual(h.min_outdegree(), 1)

    # Test of cyclicity checking
    def test_is_cyclic(self):
        # A cyclic graph is a graph which has a path
        # from a node to itself.

        # We load an example graph
        g = data.boolean_graph()
        # As it is a boolean graph, it should by definition not be cylic
        self.assertEqual(g.is_cyclic(), False)
        # We load another example graph
        h = data.cyclic_not_well_formed()
        # This one should be cyclic
        self.assertEqual(h.is_cyclic(), True)

    # ----- Test of id value checking -----
    # MIN
    def test_min_id(self):
        # The min id of a graph is the lowest value
        # of each node's id

        # We load an example graph
        g = data.boolean_graph()
        self.assertEqual(g.min_id(), 0)
        # We load another example graph
        h = data.cyclic_not_well_formed()
        self.assertEqual(h.min_id(), 5)

    # MAX
    def test_max_id(self):
        # The min id of a graph is the highest value
        # of each node's id

        # We load an example graph
        g = data.boolean_graph()
        self.assertEqual(g.max_id(), 4)
        # We load another example graph
        h = data.cyclic_not_well_formed()
        self.assertEqual(h.max_id(), 8)

    # Test of indice shifting management
    def test_shift_indices(self):
        # An indice shifting of a graph is an addition
        # of a value to every node's id

        # We load an example graph
        g = data.boolean_graph()
        # As we saw in previous tests, its minimum id is 0
        # and its maximum id is 4
        g.shift_indices(3)
        # After a shifting it should be 3 and 7
        self.assertEqual(g.min_id(), 3)
        self.assertEqual(g.max_id(), 7)

        # We load another example graph
        h = data.cyclic_not_well_formed()
        # As we saw in previous tests, its minimum id is 5
        # and its maximum id is 8
        h.shift_indices(100)
        # After a shifting it should be 105 and 108
        self.assertEqual(h.min_id(), 105)
        self.assertEqual(h.max_id(), 108)

    # Test of parallization (fusion) of graphs
    # With modifications of the graph :
    def test_iparallel(self):
        # A parallelized graph is the composition
        # of two graph but as different
        # connected components

        # We load two example graph
        g = data.boolean_graph()
        h = data.cyclic_not_well_formed()

        # Initial state
        self.assertEqual([0, 1, 2, 3, 4], g.get_node_ids())
        self.assertEqual([0, 2], g.get_input_ids())
        self.assertEqual([1, 4], g.get_output_ids())
        self.assertEqual([5, 6, 7, 8], h.get_node_ids())
        self.assertEqual([5, 5, 6], h.get_input_ids())
        self.assertEqual([5, 7], h.get_output_ids())
        # Parallel composition
        g.iparallel(h)
        # g should now have all values of h
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8], g.get_node_ids())
        self.assertEqual([0, 2, 5, 5, 6], g.get_input_ids())
        self.assertEqual([1, 4, 5, 7], g.get_output_ids())
        # And h should not have been modified
        self.assertEqual([5, 6, 7, 8], h.get_node_ids())
        self.assertEqual([5, 5, 6], h.get_input_ids())

    # Without modifications of the graph :
    def test_parallel(self):
        # A parallelized graph is the composition
        # of two graph but as different
        # connected components

        # We load two example graph
        g = data.boolean_graph()
        h = data.cyclic_not_well_formed()

        # Initial state
        self.assertEqual([0, 1, 2, 3, 4], g.get_node_ids())
        self.assertEqual([0, 2], g.get_input_ids())
        self.assertEqual([1, 4], g.get_output_ids())
        self.assertEqual([5, 6, 7, 8], h.get_node_ids())
        self.assertEqual([5, 5, 6], h.get_input_ids())
        self.assertEqual([5, 7], h.get_output_ids())

        # Parallel composition
        # test should be a parallel composition of g and h
        test = g.parallel(h, [3], [7])
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8], test.get_node_ids())
        self.assertEqual([0, 2, 5, 5, 6], test.get_input_ids())
        self.assertEqual([1, 4, 5, 7], test.get_output_ids())
        # But g and h should not have been modified
        self.assertEqual([0, 1, 2, 3, 4], g.get_node_ids())
        self.assertEqual([0, 2], g.get_input_ids())
        self.assertEqual([1, 4], g.get_output_ids())
        self.assertEqual([5, 6, 7, 8], h.get_node_ids())
        self.assertEqual([5, 5, 6], h.get_input_ids())
        self.assertEqual([5, 7], h.get_output_ids())

    # Test of composition (fusion with links) of graphs
    # With modifications of the graph :
    def test_icompose(self):
        # A composed graph is the composition
        # of two graph but as the same
        # connected components

        # We load two example graph
        g = data.boolean_graph()
        h = data.cyclic_not_well_formed()

        # Initial state
        self.assertEqual([0, 1, 2, 3, 4], g.get_node_ids())
        self.assertEqual([0, 2], g.get_input_ids())
        self.assertEqual([1, 4], g.get_output_ids())
        self.assertEqual([5, 6, 7, 8], h.get_node_ids())
        self.assertEqual([5, 5, 6], h.get_input_ids())
        self.assertEqual([5, 7], h.get_output_ids())

        # Composition
        # Note : we can not compose g with h because g has 2 outputs
        # and h has 3 inputs, but the other way is OK
        h.icompose(g)

        # Checking values (composition)
        self.assertEqual(h.get_input_ids(), [5, 5, 6])
        self.assertEqual(h.get_output_ids(), [1, 4])
        self.assertEqual(h.get_node_ids(), [0, 1, 2, 3, 4, 5, 6, 7, 8])
        # And it should now have edges between h outputs and
        # g inputs
        self.assertEqual(h.get_node_by_id(5).get_children_ids(), [0, 6])
        self.assertEqual(h.get_node_by_id(7).get_children_ids(), [2])
        self.assertEqual(h.get_node_by_id(0).get_parent_ids(), [5])
        self.assertEqual(h.get_node_by_id(2).get_parent_ids(), [7])
        # g should not have been modified
        self.assertEqual([0, 1, 2, 3, 4], g.get_node_ids())
        self.assertEqual([0, 2], g.get_input_ids())
        self.assertEqual([1, 4], g.get_output_ids())

    # Without modifications of the graph :
    def test_compose(self):
        # A composed graph is the composition
        # of two graph but as the same
        # connected components

        # We load two example graph
        g = data.boolean_graph()
        h = data.cyclic_not_well_formed()

        # Initial state
        self.assertEqual([0, 1, 2, 3, 4], g.get_node_ids())
        self.assertEqual([0, 2], g.get_input_ids())
        self.assertEqual([1, 4], g.get_output_ids())
        self.assertEqual([5, 6, 7, 8], h.get_node_ids())
        self.assertEqual([5, 5, 6], h.get_input_ids())
        self.assertEqual([5, 7], h.get_output_ids())

        # Composition
        # Note : we can not compose g with h because g has 2 outputs
        # and h has 3 inputs, but the other way is OK
        test = h.compose(g)

        # Checking values (composition)
        self.assertEqual(test.get_input_ids(), [5, 5, 6])
        self.assertEqual(test.get_output_ids(), [1, 4])
        self.assertEqual(test.get_node_ids(), [0, 1, 2, 3, 4, 5, 6, 7, 8])
        # And it should now have edges between h outputs and
        # g inputs
        self.assertEqual(test.get_node_by_id(5).get_children_ids(), [0, 6])
        self.assertEqual(test.get_node_by_id(7).get_children_ids(), [2])
        self.assertEqual(test.get_node_by_id(0).get_parent_ids(), [5])
        self.assertEqual(test.get_node_by_id(2).get_parent_ids(), [7])
        # But g and h should not have been modified
        self.assertEqual([0, 1, 2, 3, 4], g.get_node_ids())
        self.assertEqual([0, 2], g.get_input_ids())
        self.assertEqual([1, 4], g.get_output_ids())
        self.assertEqual([5, 6, 7, 8], h.get_node_ids())
        self.assertEqual([5, 5, 6], h.get_input_ids())
        self.assertEqual([5, 7], h.get_output_ids())

    # Test of connected components of a graph management
    def test_connected_components(self):
        # A connected component is a set of nodes in which
        # every nodes are linked together by edges
        # If two nodes are not in the same connected component
        # it means that there is no path from one to another

        # Loading graph example
        g = data.composed_graph()
        # The connected_components() method returns
        # the number of connected components and
        # a dictionnary that links a node to a
        # connected component
        connexe, components = g.connected_components()
        # There are 5 connected components in this graph
        self.assertEqual(connexe, 5)
        # The first two nodes are in the same connected component
        self.assertEqual(components[1], 0)
        self.assertEqual(components[2], 0)
        # The third node is in alone in its connected component
        # i.e. it doesn't have any parent nor child
        self.assertEqual(components[3], 1)
        # Same for the fourth one
        self.assertEqual(components[4], 2)
        # The 5th, 6th and 7th nodes are in the same connected component
        # i.e. they are linked by edges
        self.assertEqual(components[5], 3)
        self.assertEqual(components[6], 3)
        self.assertEqual(components[7], 3)
        # The 58th, 9th, 0th and 11th nodes are in the same connected component
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
        self.assertEqual(components[3].get_node_ids(), [5, 6, 7])
        self.assertEqual(components[4].get_node_ids(), [8, 9, 10, 11])
        '''
        # TO DO -----
        # TO DO -----
        # TO DO -----
        # TO DO -----
        # TO DO -----
        # TO DO -----
        # TO DO -----
        # TO DO -----
        # TO DO -----
        # TO DO -----
        # TO DO -----
        '''
        # Avis Colin : Je crois que le fait de toujours sort les getters
        #              pour avoir des résultats standardisés bloque
        #              les permutations

    # Test of shortest path between two nodes calculation
    def test_shortest_path(self):
        # The shortest path between two nodes is the path
        # with the less jumps to get from a node to another

        # Load graph example
        g = data.normal_graph()
        # Getting nodes
        n0 = g.get_node_by_id(0)
        n3 = g.get_node_by_id(3)
        n7 = g.get_node_by_id(7)
        # 0 and 3 are linked, the shortest path should just be the jump
        # from one to the other
        self.assertEqual(g.shortest_path(n0, n3), [0, 3])
        # 7 is the child of 3, so the shortest path should be the path
        # from 0 to 7, passing by 3
        self.assertEqual(g.shortest_path(n0, n7), [0, 3, 7])

    # Test of parents distance calculation
    def test_parents_distance(self):
        # The parents distance method returns a dictionnary that
        # contains the distance between mutual parents of the two nodes
        # and each node
        # It helps us compare the distance of parent nodes of both nodes.

        # Loading graph example
        g = data.normal_graph()

        # The nodes 5 and 8 are descendants of 0, 3 and 1 (mutual ancestors)
        distance = g.parents_distance(g.get_node_by_id(5), g.get_node_by_id(8))
        # 5 is the child of 3, but 8 is the grand child of 3
        self.assertEqual(distance, {0: (2, 3), 3: (1, 2), 1: (1, 1)})

    # Test of topological sorting of a graph
    def test_topological_sorting(self):
        # The topological sorting of a graph represents the "hierarchy"
        # of nodes inside the graph.
        # If a node does not have any child, it is in the lowest level
        # if it is the father of a node, it is on the level above, etc...

        # Loading graph example
        g = data.normal_graph()

        # We sort it
        top_sort = g.topological_sorting()
        # 7, 8, 9 does not have any child, they should be at the end
        # 5 and 6 have a child, it should be on the level above
        # 3 and 4 have grand children, so it is in the level above, etc...
        self.assertEqual(top_sort, [[0, 1, 2], [3, 4], [5, 6], [7, 8, 9]])

    # Test of node depth calculation
    def test_node_depth(self):
        # The depth of a node is the amount of levels of parents it has
        # If the node does not have any parent, its depth should be 1
        # If it is the child of a node but not the grandchild of any other node
        # its depth should be 2, etc...

        # Loading graph
        g = data.normal_graph()
        # Note : We can check that depth are coherent with the topological
        # sorting of the graph
        self.assertEqual(g.node_depth(g.get_node_by_id(0)), 1)
        self.assertEqual(g.node_depth(g.get_node_by_id(4)), 2)
        self.assertEqual(g.node_depth(g.get_node_by_id(5)), 3)
        self.assertEqual(g.node_depth(g.get_node_by_id(7)), 4)

    # Test of graph depth calculation
    def test_graph_depth(self):
        # The depth of the graph is the maximum of its
        # nodes' depth

        # Loading graph
        g = data.normal_graph()

        # It should be 4, as we saw in previous examples
        self.assertEqual(g.graph_depth(), 4)

    # Test of longest path between two nodes calculation
    def test_longest_path(self):
        # The longest path between two nodes is the
        # path with the maximum amount of jumps to get
        # from a node to another

        # Loading graph example
        g = data.normal_graph()

        # Getting nodes
        n0 = g.get_node_by_id(0)
        n7 = g.get_node_by_id(7)

        # The path between 0 and 7 is either 0, 3, 7
        # or 0, 3, 5, 7,
        # It should return the longest path
        chemin, distance = g.longest_path(n0, n7)
        self.assertEqual(chemin, [0, 3, 5, 7])
        self.assertEqual(distance, 4)


class BoolCircTest(unittest.TestCase):

    # Test of graph convertion management
    def test_to_graph(self):

        # Loading graph examples
        g1 = data.boolean_graph()
        g2 = data.cyclic_not_well_formed()
        g3 = data.cyclic_graph()
        g4 = data.not_well_formed()

        # Conversion to boolean circuit
        # Note : we set the check argument to false
        # so it forces the creation of the boolean circuit
        # even if it it not well formed and shouldn't manipulated
        b1 = bool_circ(g1, check=False)
        b2 = bool_circ(g2, check=False)
        b3 = bool_circ(g3, check=False)
        b4 = bool_circ(g4, check=False)
        # Convertion of the boolean circuits into open digraphs
        # Even if the boolean circuits are not valid, we can convert
        # them into graphs
        b1.to_graph()
        b2.to_graph()
        b3.to_graph()
        b4.to_graph()
        # We check that the reverse conversion returns the same thing
        # as the original graph
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
        # print("We'll have 3 error messages : ")
        # b2 = bool_circ(g2)  # On a bien un message d'erreur
        # b3 = bool_circ(g3)  # On a bien un message d'erreur
        # b4 = bool_circ(g4)  # On a bien un message d'erreur
        '''
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        '''

    '''
    # TO DO -----
    # TO DO -----
    # TO DO -----
    # TO DO -----
    # TO DO -----
    # TO DO -----
    # TO DO -----
    # TO DO -----
    # TO DO -----
    '''
    '''Test TD10'''
    def test_random_bool_circ(self):
        #creation of 5 random bool_circ
        rand_bool1 = bool_circ.random_bool_circ(5 , 1, 1)
        rand_bool2 = bool_circ.random_bool_circ(20, 4, 9)
        rand_bool3 = bool_circ.random_bool_circ(3 , 1, 2)
        rand_bool4 = bool_circ.random_bool_circ(10, 3, 2)
        rand_bool5 = bool_circ.random_bool_circ(10, 3, 2)

        #on vérifie qu'il y a le bon nombre d'input et de output
        #pour vérifier si le graph est bien formé on regarde s'il y a un message d'erreur
        self.assertEqual(len(rand_bool1.get_input_ids() ), 1)
        self.assertEqual(len(rand_bool1.get_output_ids()), 1)
        self.assertEqual(len(rand_bool2.get_input_ids() ), 4)
        self.assertEqual(len(rand_bool2.get_output_ids()), 9)
        self.assertEqual(len(rand_bool3.get_input_ids() ), 1)
        self.assertEqual(len(rand_bool3.get_output_ids()), 2)
        self.assertEqual(len(rand_bool4.get_input_ids() ), 3)
        self.assertEqual(len(rand_bool4.get_output_ids()), 2)
        self.assertEqual(len(rand_bool5.get_input_ids() ), 3)
        self.assertEqual(len(rand_bool5.get_output_ids()), 2)


if __name__ == '__main__':  # the following code is called only when
    unittest.main()         # precisely this file is run
