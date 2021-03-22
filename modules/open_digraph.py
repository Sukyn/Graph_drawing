import sys
sys.path.append('../')
from modules.utils import *

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
        self.fromworld = 0
        self.toworld = 0

    def __str__(self):
        '''
        **TYPE** string
        '''
        ######  Example  ######
        # id : 0
        # label : d
        # parents : [2, 3, 4]
        # children : [5, 6]
        # will return (0, d, [2, 3, 4], [5, 6])
        return ("("+str(self.id)+", "+self.label+", "
              +str(self.parents)+", "+str(self.children)+")")

    def __repr__(self):
        '''
        **TYPE** string
        '''
        ######  Example  ######
        # id : 0
        # label : d
        # parents : [2, 3, 4]
        # children : [5, 6]
        # will return  node(0, d, [2, 3, 4], [5, 6])
        return "node"+str(self)

    def copy(self):
        '''
        **TYPE** node
        function that returns a copy of the object
        '''
        return node(self.id, self.label, self.parents, self.children)

    '''
    GETTERS
    functions to get the attributes of the object
    (encapsulation)
    '''
    def get_id(self):
        return self.id
    def get_label(self):
        return self.label
    def get_parent_ids(self):
        return self.parents
    def get_children_ids(self):
        return self.children

    '''
    SETTERS
    functions to modify the attributes of the object
    (encapsulation)
    '''
    def set_id(self, new_id):
        self.id = new_id
    def set_label(self, new_label):
        self.label = new_label
    def set_parent_ids(self, new_ids):
        self.parents = new_ids
    def set_children_ids(self, new_ids):
        self.children = new_ids
    def add_child_id(self, new_id):
        self.children.append(new_id)
    def add_parent_id(self, new_id):
        self.parents.append(new_id)


    def remove_parent_id(self, id):
        '''
        **TYPE** void
        id: int; id of the parent
        remove the parent using its id
        '''
        try:
            self.parents.remove(id)
        except ValueError:
            pass

    def remove_child_id(self, id):
        '''
        **TYPE** void
        id: int; id of the child
        remove the child using its id
        '''
        try:
            self.children.remove(id)
        except ValueError:
            pass

    def remove_parent_id_all(self, id):
        '''
        **TYPE** void
        id: int; id of the parents
        remove all of the parents with the id
        '''
        remove_all(self.parents, id)

    def remove_child_id_all(self, id):
        '''
        **TYPE** void
        id: int; id of the children
        remove all of the children with the id
        '''
        remove_all(self.children, id)

    def indegree(self):
        '''
        **TYPE** int
        returns the indegree of the node, i.e. the number of parents it has
        '''
        return len(self.get_parent_ids()) + self.fromworld

    def outdegree(self):
        '''
        **TYPE** int
        returns the outdegree of the node, i.e. the number of children it has
        '''
        return len(self.get_children_ids()) + self.toworld

    def degree(self):
        '''
        **TYPE** int
        returns the total degree of the node, i.e. the number of
        parents and children it has
        '''
        return self.outdegree() + self.indegree()
























class open_digraph: # for open directed graph

    def __init__(self, inputs, outputs, nodes):
        '''
        inputs: int list; the ids of the input nodes
        outputs: int list; the ids of the output nodes
        nodes: node list;
        '''
        self.inputs = inputs
        self.outputs = outputs
        self.nodes = {node.id:node for node in nodes} # self.nodes: <int,node> dict
        for inp in inputs:
            if inp in self.nodes:
                self.get_node_by_id(inp).fromworld += 1
        for outp in outputs:
            if outp in self.nodes:
                self.get_node_by_id(outp).toworld += 1


    def __str__(self):
        '''
        **TYPE** string
        '''
        # **EXAMPLE** ([0, 1], [2], 4)
        return ("("+str(self.inputs)+", "+str(self.outputs)
                    +", "+str(self.nodes)+")")

    def __repr__(self):
        '''
        **EXAMPLE**
        open_digraph([0,1], [2], [node(4, 'i', [0, 2], [3])])
        '''
        return "open_digraph"+str(self)

    def __eq__(self, g):
        '''
        **TYPE** boolean
        return self == g
        '''
        inp = self.inputs == g.inputs
        out = self.outputs == g.outputs
        node = self.nodes == g.nodes
        return inp and out and node

    def empty():
        '''
        **TYPE** void
        constructor of an empty graph
        no inputs, no outputs, no nodes
        '''
        return open_digraph([],[],[])

    def copy(self):
        '''
        **TYPE** open_digraph
        function that returns a copy of the object
        '''
        return open_digraph(self.inputs, self.outputs, self.nodes.values())

    '''
    GETTERS
    functions to get the attributes of the object
    (encapsulation)
    '''
    def get_input_ids(self):
        return self.inputs
    def get_output_ids(self):
        return self.outputs
    def get_id_node_map(self):
        return self.nodes
    def get_nodes(self):
        return list(self.nodes.values())
    def get_node_ids(self):
        return [i for i in self.nodes]
    def get_node_by_id(self, id):
        return self.nodes[id]
    def get_nodes_by_ids(self, idlist):
        return [self.nodes[i] for i in idlist]
    def get_length(self):
        return len(self.nodes)
    '''
    SETTERS
    functions to modify the attributes of the object
    (encapsulation)
    '''
    def set_input_ids(self, new_idlist):
        self.inputs = new_idlist
    def set_output_ids(self, new_idlist):
        self.outputs = new_idlist
    def add_input_id(self, new_id):
        self.inputs.append(new_id)
    def add_output_id(self, new_id):
        self.outputs.append(new_id)

    def new_id(self):
        '''
        **TYPE** void
        function that returns an unused id for an edge
        '''
        id = 0
        while(self.nodes.get(id, None) != None):
            id += 1
        return id

    def add_edge(self, src, tgt):
        '''
        **TYPE** void
        src: int; id of the source node
        tgt: int; id of the target node
        function to add edge
        '''
        self.get_node_by_id(src).children.append(tgt)
        self.get_node_by_id(tgt).parents.append(src)

    def add_edges(self, src_list, tgt_list):
        '''
        **TYPE** void
        src_list: int list; ids of the source nodes
        tgt_list: int list; ids of the target nodes
        fonction to add edges
        '''
        for src,tgt in zip(src_list,tgt_list):
            self.add_edge(src, tgt)

    def add_node(self, label = '', parents = [], children = []):
        '''
        **TYPE** void
        label: string; label of the node to add
        parents: int list; parents' ids of the node to add
        children: int list; children's ids of the node to add
        '''
        id = self.new_id()
        thisnode = node(id, label, [], [])
        self.nodes[thisnode.id] = thisnode
        for parent in parents:
            self.add_edge(parent, id)
        for child in children:
            self.add_edge(id, child)
        return id

    def remove_edge(self, src, tgt):
        '''
        **TYPE** void
        src: int; id of the source node
        tgt : int; id of the target node
        function to remove edge
        '''
        self.get_node_by_id(src).children.remove(tgt)
        self.get_node_by_id(tgt).parents.remove(src)

    def remove_node_by_id(self, id):
        '''
        **TYPE** void
        id: int; id of the node to remove
        remove the node with the id
        '''
        for parent in self.get_node_by_id(id).parents :
            self.get_node_by_id(parent).remove_child_id_all(id)
        for child in self.get_node_by_id(id).children :
            self.get_node_by_id(child).remove_parent_id_all(id)
        del self.nodes[id]


    def remove_edges(self, src_list, tgt_list):
        '''
        **TYPE** void
        src_list: int list; ids of the source nodes
        tgt_list: int list; ids of the target nodes
        fonction to remove edges
        '''
        for src, tgt in zip(src_list, tgt_list):
            try:
                while(True):
                    self.remove_edge(src,tgt)
            except ValueError:
                pass
    def remove_nodes_by_id(self, id_list):
        '''
        **TYPE** void
        id_list: int list; list of the nodes' ids
        remove the nodes with the ids
        '''
        for id in id_list:
            try:
                self.remove_node_by_id(id)
            except KeyError:
                pass


    def is_well_formed(self):
        '''
        **TYPE** boolean
        function that verify if the graph is well formed
        return True if the graph is well formed
        '''
        nodes_ids = self.get_id_node_map() # Getting every id of nodes in the graph
        for node_id in nodes_ids:
            if nodes_ids[node_id].get_id() != node_id: # Checking that keys and nodes are linked
                return False

            sons = nodes_ids[node_id].get_children_ids()
            parents = nodes_ids[node_id].get_parent_ids()
            for child in sons: # Checking sons are coherent
                n = count_occurence(sons, child)
                if (count_occurence(nodes_ids[child].get_parent_ids(), nodes_ids[node_id].get_id()) != n):
                    return False
            for parent in parents: # Checking that parents are coherent
                n = count_occurence(parents, parent)
                if (count_occurence(nodes_ids[parent].get_children_ids(), nodes_ids[node_id].get_id()) != n):
                    return False

        for inp in self.get_input_ids(): # Checking inputs are in nodes
            if inp not in nodes_ids:
                return False
        for outp in self.get_output_ids(): # Checking outputs are in nodes
            if outp not in nodes_ids:
                return False
        return True

    def change_id(self, new_id, node_id):
        '''
        **TYPE** void
        new_id: int; new id of the node
        node_id: int; actual id of the node
        change node_id by new_id
        '''
        if(new_id in self.get_node_ids()):
            print("The node id already exists")
            #raise
        elif(node_id == new_id):
            pass
        else:
            self.get_id_node_map()[new_id] = self.get_id_node_map().pop(node_id)
            for node in self.get_nodes():
                if node_id in node.get_parent_ids():
                    node.remove_parent_id(node_id)
                    node.add_parent_id(new_id)
                if node_id in node.get_children_ids():
                    node.remove_child_id(node_id)
                    node.add_child_id(new_id)


    def change_ids(self, new_ids, node_ids):
        '''
        **TYPE** void
        new_ids: int list; new ids of the nodes
        node_ids: int list; actual ids of the nodes
        change all of the node_ids by new_ids
        '''
        list = sorted(zip(new_ids, node_ids), key = lambda x: x[0])
        for new_id, node_id in list:
            self.change_id(new_id, node_id)

    def normalize_ids(self):
        '''
        **TYPE** void
        change every nodes ids with the first natural numbers
        '''
        normalized_list = [i for i in range(self.get_length())]
        old_ids = self.get_node_ids()
        self.change_ids(normalized_list, old_ids)

    def adjacency_matrix(self):
        '''
        **TYPE** int list list
        return the adjacency_matrix of the graph
        '''
        n = self.get_length()
        self.normalize_ids()
        return [[count_occurence(self.get_node_by_id(i).get_parent_ids(), j) for i in range(n)] for j in range(n)]


    def max_indegree(self):
        '''
        **TYPE** int
        returns the maximum indegree of the graph,
        i.e. the maximum of each node's indegree
        '''
        return max([node.indegree() for node in self.get_nodes()])

    def min_indegree(self):
        '''
        **TYPE** int
        returns the minimum indegree of the graph,
        i.e. the minimum of each node's indegree
        '''
        return min([node.indegree() for node in self.get_nodes()])

    def max_outdegree(self):
        '''
        **TYPE** int
        returns the maximum outdegree of the graph,
        i.e. the maximum of each node's outdegree
        '''
        return max([node.outdegree() for node in self.get_nodes()])

    def min_outdegree(self):
        '''
        **TYPE** int
        returns the miniimum indegree of the graph,
        i.e. the miniimum of each node's outdegree
        '''
        return min([node.outdegree() for node in self.get_nodes()])

    def is_cyclic(self):
        '''
        **TYPE** boolean
        TRUE if the graph is cyclic
        cyclic means that there is a path from a node to itself
        '''
        g = self.copy() # We make a copy to avoid removing nodes to the graph
        def sub_is_cyclic(g):
            # If there is no node in the graph, it is acyclic by definition
            if not g.get_nodes():
                return False
            else:
                for node in g.get_nodes():
                    # We check if the node is a leaf (i.e. no children)
                    if not node.get_children_ids():
                        leaf = node.get_id()
                        # If you remove a leaf to a graph, and that this child graph is cyclic,
                        # it means that the original graph is cyclic, and this is the same
                        # for acyclic graphs
                        g.remove_node_by_id(leaf)
                        return sub_is_cyclic(g)
                # If there are nodes BUT not any leaf, it means that the graph is a cycle
                return True
        return sub_is_cyclic(g)

















class bool_circ(open_digraph):
    def __init__(self, g):
        '''
        **TYPE** boolean
        g: open_digraph
        returns True if the graph g is a boolean circuit, and creates the instance
        '''
        nodes = [g.nodes[node] for node in g.nodes]
        self = super().__init__(g.inputs, g.outputs, nodes)
        # We check that the boolean circuit is well formed, to know if we can actually create it
        return bool_circ.is_well_formed()

    def to_graph(self):
        #QUESTION 2
        '''
        **TYPE** open_digraph
        That fonction converts a bool_circ into a open_digraph and return it
        '''
        return open_digraph(self.input_ids(), self.get_output_ids(), self.get_nodes(), self.get_ids())

    def is_well_formed(self):
        #QUESTION 6
        '''
        **TYPE** boolean
        That fonction tests if the bool_circ is well formed.
        i.e. if he is acyclic and respects th degrees constraints

        We could have nodes with the '0' or the '1' value to represent the 0 and 1 constants

        A well formed bool_circ :
        - has all of his copy nodes with one input
        - has all of his AND and OR gates with one output
        - has all of his NOT gate with one input and one output
        - is not cyclic
        '''
        if self.to_graph().is_cyclic():
            return False
        else:
            for node in self.to_graph().get_nodes():
                if (node.get_label() == ""):
                    if (node.indegree() != 1):
                        return False
                if (node.get_label() == "&"):
                    if (node.outdegree() != 1):
                        return False
                if (node.get_label() == "|" ):
                    if (node.outdegree() != 1):
                        return False
                if (node.get_label() == "~"):
                    if (node.indegree() != 1 or node.outdegree() != 1):
                        return False
            return True
