import modules.utils as utils
from modules.open_digraph_mix.open_digraph_getters_setters import *
from modules.open_digraph_mix.open_digraph_management import *
from modules.open_digraph_mix.open_digraph_composition import *
from modules.open_digraph_mix.open_digraph_dijkstra import *
import random

class node:
    def __init__(self, identity, label, parents, children):
        '''
        **TYPE** void
        identity: int; its unique id in the graph
        label: string;
        parents: int list; a sorted list containing the ids of its parents
        children: int list; a sorted list containing the ids of its children
        '''
        self.id = identity
        self.label = label
        self.parents = parents
        self.children = children

    def __str__(self):
        '''
        **TYPE** string
        '''
        # -----  Example  -----
        # id : 0
        # label : d
        # parents : [2, 3, 4]
        # children : [5, 6]
        # will return (0, d, [2, 3, 4], [5, 6])
        return ("(" + str(self.id) + ", " + self.label + ", " +
                str(self.parents) + ", " + str(self.children) + ")")

    def __repr__(self):
        '''
        **TYPE** string
        '''
        # -----  Example  -----
        # id : 0
        # label : d
        # parents : [2, 3, 4]
        # children : [5, 6]
        # will return  node(0, d, [2, 3, 4], [5, 6])
        return "node" + str(self)

    def copy(self):
        '''
        **TYPE** node
        function that returns a copy of the object
        '''
        return node(self.get_id(),
                    self.get_label(),
                    self.get_parent_ids().copy(),
                    self.get_children_ids().copy())

    # ----- GETTERS -----
    # functions to get the attributes of the object
    # (encapsulation)
    def get_id(self):
        return self.id

    def get_label(self):
        return self.label

    def get_parent_ids(self):
        return self.parents

    def get_children_ids(self):
        return self.children

    # ----- SETTERS -----
    # functions to modify the attributes of the object
    # (encapsulation)
    def set_id(self, new_id):
        self.id = new_id

    def set_label(self, new_label):
        self.label = new_label

    def set_parent_ids(self, new_ids):
        self.parents = new_ids
        self.parents.sort()

    def set_children_ids(self, new_ids):
        self.children = new_ids
        self.children.sort()

    def add_child_id(self, new_id):
        self.children.append(new_id)
        self.children.sort()

    def add_parent_id(self, new_id):
        self.parents.append(new_id)
        self.parents.sort()

    def remove_parent_id(self, id):
        '''
        **TYPE** void
        id: int; id of the parent
        remove the parent using its id
        '''
        try:
            self.parents.remove(id)
        except ValueError as ve:
            print("Trying to remove a non-existing parent of the node :", ve)

    def remove_child_id(self, id):
        '''
        **TYPE** void
        id: int; id of the child
        remove the child using its id
        '''
        try:
            self.children.remove(id)
        except ValueError as ve:
            print("Trying to remove a non-existing child of the node :", ve)

    def remove_parent_id_all(self, id):
        '''
        **TYPE** void
        id: int; id of the parents
        remove all of the parents with the id
        '''
        utils.remove_all(self.parents, id)

    def remove_child_id_all(self, id):
        '''
        **TYPE** void
        id: int; id of the children
        remove all of the children with the id
        '''
        utils.remove_all(self.children, id)


class open_digraph(open_digraph_getters_setters,
                   open_digraph_management,
                   open_digraph_composition,
                   open_digraph_dijkstra):  # for open directed graph

    def __init__(self, inputs, outputs, nodes):
        '''
        inputs: int list; the ids of the input nodes
        outputs: int list; the ids of the output nodes
        nodes: node list;
        '''
        __all__ = ["open_digraph_getters_setters",
                           "open_digraph_management",
                           "open_digraph_composition",
                           "open_digraph_dijkstra"]
        self.inputs = inputs
        self.outputs = outputs
        # self.nodes: <int,node> dict
        self.nodes = {node.id: node for node in nodes}

    def __str__(self):
        '''
        **TYPE** string
        '''
        # **EXAMPLE** ([0, 1], [2], 4)
        return ("(" + str(self.inputs) + ", " + str(self.outputs) +
                ", " + str(self.nodes) + ")")

    def __repr__(self):
        '''
        **EXAMPLE**
        open_digraph([0,1], [2], [node(4, 'i', [0, 2], [3])])
        '''
        return "open_digraph" + str(self)

    def __eq__(self, g):
        '''
        **TYPE** boolean
        return self == g
        '''
        # We check that inputs are equals
        if not (self.inputs == g.inputs):
            return False
        # We check that outputs are equals
        if not (self.outputs == g.outputs):
            return False
        # We check that nodes are equals
        if not (self.nodes == g.nodes):
            return False
        # If they're all equals, then the graphs are equals
        return True

    def empty():
        '''
        **TYPE** open digraph
        constructor of an empty graph
        no inputs, no outputs, no nodes
        '''
        return open_digraph([], [], [])

    def copy(self):
        '''
        **TYPE** open_digraph
        function that returns a copy of the object
        '''
        return open_digraph(self.get_input_ids().copy(),
                            self.get_output_ids().copy(),
                            [i.copy() for i in self.get_nodes()])

    def new_id(self):
        '''
        **TYPE** void
        function that returns an unused id for an edge
        '''
        id = 0
        while(id in self.get_node_ids()):
            id += 1
        return id

    def is_well_formed(self):
        '''
        **TYPE** boolean
        function that verify if the graph is well formed
        return True if the graph is well formed
        '''
        # List of valid labels
        valid_label = ["&", "|", "∼", "^", "0", "1", ""]

        # Getting every id of nodes in the graph
        nodes_ids = self.get_id_node_map()
        for node_id in nodes_ids:

            # Checking that labels are valid
            if nodes_ids[node_id].get_label() not in valid_label:
                return False

            # Checking that keys and nodes are linked
            if nodes_ids[node_id].get_id() != node_id:
                return False

            children_ids = nodes_ids[node_id].get_children_ids()
            parents_ids = nodes_ids[node_id].get_parent_ids()
            for child_id in children_ids:  # Checking sons are coherent
                n = utils.count_occurence(children_ids, child_id)
                if (utils.count_occurence(nodes_ids[child_id].get_parent_ids(),
                                          nodes_ids[node_id].get_id()) != n):
                    return False
            for parent in parents_ids:  # Checking that parents are coherent
                n = utils.count_occurence(parents_ids, parent)
                if (utils.count_occurence(nodes_ids[parent].get_children_ids(),
                                          nodes_ids[node_id].get_id()) != n):
                    return False

        for input in self.get_input_ids():  # Checking inputs are in nodes
            if input not in nodes_ids:
                return False
        for output in self.get_output_ids():  # Checking outputs are in nodes
            if output not in nodes_ids:
                return False
        return True

    def normalize_ids(self):
        '''
        **TYPE** void
        change every nodes ids with the first natural numbers
        '''
        normalized_list = [i for i in range(self.get_length())]
        old_ids = self.get_node_ids()

        self.change_ids(old_ids, normalized_list)

    def adjacency_matrix(self):
        '''
        **TYPE** int list list
        return the adjacency_matrix of the graph
        '''
        n = self.get_length()

        self.normalize_ids()

        return [[utils.count_occurence(self.get_node_by_id(i).get_parent_ids(),
                                       j)
                for i in range(n)] for j in range(n)]

    def is_cyclic(self):
        '''
        **TYPE** boolean
        TRUE if the graph is cyclic
        cyclic means that there is a path from a node to itself
        '''
        # We make a copy to avoid removing nodes to the graph
        graph = self.copy()

        def sub_is_cyclic(graph):
            # If there is no node in the graph, it is acyclic by definition
            if not graph.get_nodes():
                return False
            else:
                for node in graph.get_nodes():
                    # We check if the node is a leaf (i.e. no children)
                    if not node.get_children_ids():
                        leaf = node.get_id()
                        # If you remove a leaf to a graph,
                        # and that this child graph is cyclic,
                        # it means that the original graph is cyclic,
                        # and this is the same for acyclic graphs
                        graph.remove_node_by_id(leaf)
                        return sub_is_cyclic(graph)
                # If there are nodes BUT not any leaf,
                # it means that the graph is a cycle
                return True

        return sub_is_cyclic(graph)

    def graph_from_adjacency_matrix(matrix):
        node_list = [node(i, '{}'.format(i), [], []) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                for k in range(matrix[i][j]):
                    node_list[j].add_parent_id(i)
                    node_list[i].add_child_id(j)
        return open_digraph([], [], node_list)

    def random_graph(n, bound, inputs=[], outputs=[], form="free"):
        '''
        pour form on a differentes options :
            "free": un graphe quelconque
            "DAG" : un graphe dirige acyclique
            "oriented" : un graphe oriente
            "undirected" : un graphe non dirige
            "loop-free undirected" : ___________
        '''
        if (form == "free"):
            graphe = open_digraph.graph_from_adjacency_matrix( utils.random_matrix(n, bound) )
        elif (form == "DAG"):
            graphe = open_digraph.graph_from_adjacency_matrix( utils.random_matrix(n, bound, triangular = True, null_diag = True) )
        elif (form == "oriented"):
            graphe = open_digraph.graph_from_adjacency_matrix( utils.random_matrix(n, bound, oriented = True) )
        elif (form == "undirected"):
            graphe = open_digraph.graph_from_adjacency_matrix( utils.random_matrix(n, bound, oriented = False) )
        elif (form == "loop-free undirected"):
            graphe = open_digraph.graph_from_adjacency_matrix( utils.random_matrix(n, bound, null_diag = True) )
        else:
            print("Invalid parameters")
            return

        graphe.set_input_ids(inputs)
        graphe.set_output_ids(outputs)
        return graphe

    def topological_sorting(self):
        '''
        **TYPE** Two-dimensional list
        return the topological sorting 'compressed upwards' of the graph
        '''
        # We work on a copy of the graph
        g = self.copy()
        sorting = []
        leaves = []
        # While the graph has nodes
        while(len(g.get_nodes()) > 0):
            for node in g.get_nodes():
                # We check if the node is a leaf (i.e. no children)
                if not node.get_children_ids():
                    leaves.append(node.get_id())
            # We detect if the graph is cyclic
            # (i.e. if there are no more leaves but the graph
            #  is non-empty)
            if leaves == []:
                raise ValueError("The graph isn't acyclic")
            # We get this list of leaves in our sorting table,
            # then we remove these leaves from the graph
            sorting.append(leaves)
            g.remove_nodes_by_id(leaves)
            leaves = []

        sorting.sort(key=lambda x: x[0])
        return sorting

    def node_depth(self, node):
        '''
        **TYPE** int
        node: node of the graph
        returns the node depth,
        i.e. the index of the sub-list where
        the id of the node is located in
        the list returned by the topological_sorting function
        '''
        for i, x in enumerate(self.topological_sorting()):
            if node.get_id() in x:
                return i+1

    def graph_depth(self):
        '''
        **TYPE** int
        returns the graph depth,
        i.e. the number of sub-list in the list
        returned by the topological_sorting function
        '''
        return len(self.topological_sorting())

    def add_node(self, label='', parents=[], children=[]):
        '''
        **TYPE** int
        label: string; label of the node to add
        parents: int list; parents' ids of the node to add
        children: int list; children's ids of the node to add
        '''
        # This should return an Id that is not in the graph
        id = self.new_id()
        # Note : parents & children will be added after
        thisNode = node(id, label, [], [])
        self.nodes[id] = thisNode
        for parent in parents:
            self.add_edge(parent, id)
        for child in children:
            self.add_edge(id, child)
        return id

    def indegree(self, node):
        '''
        **TYPE** int
        returns the indegree of the node, i.e. the number of parents it has
        '''
        return len(node.get_parent_ids()) + utils.count_occurence(self.get_input_ids(), node.get_id())

    def outdegree(self, node):
        '''
        **TYPE** int
        returns the outdegree of the node, i.e. the number of children it has
        '''
        return len(node.get_children_ids()) + utils.count_occurence(self.get_output_ids(), node.get_id())

    def degree(self, node):
        '''
        **TYPE** int
        returns the total degree of the node, i.e. the number of
        parents and children it has
        '''
        return self.outdegree(node) + self.indegree(node)
