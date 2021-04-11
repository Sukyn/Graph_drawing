import sys
from modules.utils import *
sys.path.append('../')


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


class open_digraph:  # for open directed graph

    def __init__(self, inputs, outputs, nodes):
        '''
        inputs: int list; the ids of the input nodes
        outputs: int list; the ids of the output nodes
        nodes: node list;
        '''
        self.inputs = inputs
        self.outputs = outputs
        # self.nodes: <int,node> dict
        self.nodes = {node.id: node for node in nodes}
        self.compute_indegrees()
        self.compute_outdegrees()

    def compute_indegrees(self):
        # This part is useful to calculate the indegree of nodes
        # First, we reset all values
        for node in self.nodes:
            self.nodes[node].fromworld = 0
        # Then we calculate new ones
        for input in self.inputs:  # The graph should be well formed
            if input in self.get_node_ids():
                self.nodes[input].fromworld += 1

    def compute_outdegrees(self):
        # This part is useful to calculate the indegree of nodes
        # First, we reset all values
        for node in self.nodes:
            self.nodes[node].toworld = 0
        # Then we calculate new ones
        for output in self.outputs:  # The graph should be well formed
            if output in self.get_node_ids():
                self.nodes[output].toworld += 1

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
        **TYPE** void
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

    # ----- GETTERS -----
    # functions to get the attributes of the object
    # (encapsulation)
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

    def multi_getter(self, id, args):
        '''
        This functions is a shortcut if you want to
        find either parents, children or both
        '''
        result = []
        if "parents" in args:
            result += self.get_nodes_by_ids(
                      (self.get_node_by_id(id)).get_parent_ids()
                      )
        if "children" in args:
            result += self.get_nodes_by_ids(
                      (self.get_node_by_id(id)).get_children_ids()
                      )
        return result

    # ----- SETTERS -----
    # functions to modify the attributes of the object
    # (encapsulation)
    def set_input_ids(self, new_idlist):
        self.inputs = new_idlist
        # New computation of the nodes' indegree
        self.compute_indegrees()

    def set_output_ids(self, new_idlist):
        self.outputs = new_idlist
        # New computation of the nodes' outdegree
        self.compute_outdegrees()

    def add_input_id(self, new_id):
        self.inputs.append(new_id)
        self.compute_indegrees()

    def add_output_id(self, new_id):
        self.outputs.append(new_id)
        self.compute_outdegrees()

    def new_id(self):
        '''
        **TYPE** void
        function that returns an unused id for an edge
        '''
        id = 0
        while(id in self.get_node_ids()):
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
        for src, tgt in zip(src_list, tgt_list):
            self.add_edge(src, tgt)

    def add_node(self, label='', parents=[], children=[]):
        '''
        **TYPE** void
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
        node = self.get_node_by_id(id)
        for parent in node.get_parent_ids():
            parent_node = self.get_node_by_id(parent)
            parent_node.remove_child_id_all(id)
        for child in node.get_children_ids():
            child_node = self.get_node_by_id(child)
            child_node.remove_parent_id_all(id)
        self.nodes.pop(id)

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
                    self.remove_edge(src, tgt)
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
        # Getting every id of nodes in the graph
        nodes_ids = self.get_id_node_map()
        for node_id in nodes_ids:
            # Checking that keys and nodes are linked
            if nodes_ids[node_id].get_id() != node_id:
                return False

            children_ids = nodes_ids[node_id].get_children_ids()
            parents_ids = nodes_ids[node_id].get_parent_ids()
            for child_id in children_ids:  # Checking sons are coherent
                n = count_occurence(children_ids, child_id)
                if (count_occurence(nodes_ids[child_id].get_parent_ids(),
                                    nodes_ids[node_id].get_id()) != n):
                    return False
            for parent in parents_ids:  # Checking that parents are coherent
                n = count_occurence(parents_ids, parent)
                if (count_occurence(nodes_ids[parent].get_children_ids(),
                                    nodes_ids[node_id].get_id()) != n):
                    return False

        for input in self.get_input_ids():  # Checking inputs are in nodes
            if input not in nodes_ids:
                return False
        for output in self.get_output_ids():  # Checking outputs are in nodes
            if output not in nodes_ids:
                return False
        return True

    def change_id(self, new_id, node_id):
        '''
        **TYPE** void
        new_id: int; new id of the node
        node_id: int; actual id of the node
        change node_id by new_id
        '''
        if (new_id not in self.get_node_ids()):
            node_map = self.get_id_node_map()
            node = node_map.pop(node_id)
            # Our node map should have the node with another id
            node_map[new_id] = node
            # We change the id
            node.set_id(new_id)

            for child in node.get_children_ids():
                self.get_node_by_id(child).remove_parent_id(node_id)
                node.remove_child_id(child)
            for parent in node.get_parent_ids():
                self.get_node_by_id(parent).remove_child_id(node_id)
                node.remove_parent_id(parent)

    def change_ids(self, new_ids, node_ids):
        '''
        **TYPE** void
        new_ids: int list; new ids of the nodes
        node_ids: int list; actual ids of the nodes
        change all of the node_ids by new_ids
        '''
        list = sorted(zip(new_ids, node_ids), key=lambda x: x[0])
        for i in range(len(list)):
            self.change_id(list[i][0], list[i][1])

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
        return [[count_occurence(self.get_node_by_id(i).get_parent_ids(), j)
                for i in range(n)] for j in range(n)]

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
        i.e. the minimum of each node's outdegree
        '''
        return min([node.outdegree() for node in self.get_nodes()])

    def is_cyclic(self):
        '''
        **TYPE** boolean
        TRUE if the graph is cyclic
        cyclic means that there is a path from a node to itself
        '''

        graph = self.copy()  # We make a copy to avoid removing nodes to the graph

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

    def min_id(self):
        return min(self.get_node_ids())

    def max_id(self):
        return max(self.get_node_ids())

    def shift_indices(self, n):
        new_ids = [(ids + n) for ids in self.get_nodes_by_ids()]
        self.change_ids(new_ids, self.get_nodes_by_ids())

    def iparallel(self, g, in_perm=None, out_perm=None):
        for inp in g.get_input_ids():
            self.add_input_id(inp)
        for outp in g.get_output_ids():
            self.add_output_id(outp)
        if self.max_id() > g.min_id():
            g = g.copy().shift_indices(self.max_id() - g.min_id() + 1)
        for node in g.get_nodes():
            self.get_id_node_map()[node.get_id()] = node

    def parallel(self, g, in_perm, out_perm):
        return self.copy().iparallel(g, in_perm, out_perm)

    def icompose(self, g):
        inputs = g.get_input_ids()
        outputs = self.get_output_ids()
        if not len(inputs) == len(outputs):
            raise ValueError
        else:
            # if the lists 'inputs' and 'outputs' have values in common
            if(bool(set(inputs).intersection(outputs))):
                self.shift_indices(g.max_id() - self.min_id() + 1)
            for i in range(len(inputs)):
                self.add_edge(inputs[i], outputs[i])

    def compose(self, g):
        return self.copy().icompose(g)

    def connected_components(self):
        components = {}
        g = self.copy()
        id_connexe = 0

        while g.get_node_ids():
            nodes_list = [g.min_id()]
            for nodes_id in nodes_list:
                components[nodes_id] = id_connexe
                nodes = g.get_node_by_ids(nodes_id)
                parents = [n.get_parent_ids() for n in nodes]
                children = [n.get_children_ids() for n in nodes]
                g.remove_node_by_id(nodes_id)
                nodes_list += parents + children
            id_connexe += 1
        return (id_connexe + 1, components)

    def graph_permutation(self):
        nb, compo_id = self.connected_components()
        components = []
        for i in range(nb):
            node_ids = [key for (key, value) in compo_id.items() if value == i]
            nodes = self.get_nodes_by_ids(node_ids)
            inputs = [inp for inp in self.get_input_ids()
                      if inp in node_ids]
            outputs = [outp for outp in self.get_output_ids()
                       if outp in node_ids]
            components.append(open_digraph(inputs, outputs, nodes))
        return (components, self.get_input_ids(), self.get_output_ids())

    '''TD8'''

    def dijkstra(self, src, direction=None, tgt=None):

        queue = [src]
        dist = {src: 0}
        prev = {}

        while queue:
            u = queue[0]
            #u = self.get_id(min(Q, key=lambda x: dist[x]))
            queue.remove(u)
            switcher = {
                1: "parents",
                -1: "children",
                None: ["parents", "children"]
            }
            neighbours = self.multi_getter(u.get_id(), switcher.get(direction,
                                           "Invalid direction value"))
            for v in neighbours:
                if v not in dist:
                    queue.append(v)
                if v not in dist or dist[v] > dist[u] + 1:
                    dist[v] = dist[u] + 1
                    prev[v] = u
                if v == tgt:
                    return (dist[v], prev)
        return (dist, prev)

    def shortest_path(self, nodeA, nodeB):
        if nodeB not in self.get_nodes():
            print("nodeB not in the graph")
            return None
        distance, previous = self.dijkstra(nodeA, tgt=nodeB)
        path = [nodeB]
        node = nodeB
        while node != nodeA:
            node = previous[node]
            path.insert(0, node)

        if distance != len(path):
            print("La taille n'est pas bonne")
            return None
        return path

    def parents_distance(self, nodeA, nodeB):
        result = {}
        for nodeA_parent in nodeA.get_parent_ids():
            for nodeB_parent in nodeB.get_parent_ids():
                if nodeA_parent == nodeB_parent:
                    result[nodeA_parent] = (self.dijkstra(nodeA,
                                                          tgt=nodeA_parent)[0],
                                            self.dijkstra(nodeB,
                                                          tgt=nodeB_parent)[0])
        return result

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
            leaves = []
            g.remove_nodes_by_id(leaves)
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
                return i

    def graph_depth(self):
        '''
        **TYPE** int
        returns the graph depth,
        i.e. the number of sub-list in the list
        returned by the topological_sorting function
        '''
        return len(self.topological_sorting())

    def longest_path(self, u, v):
        dist = {u: 0}
        prev = {}

        if self.is_cyclic():
            raise ValueError("The graph isn't acyclic")
        else:
            sorted_list = self.topological_sorting()
            depth = self.node_depth(u)
            # For depths of more than k
            for i in range(depth+1, len(sorted_list)):
                for w in sorted_list[i]:
                    # If w node is different to v node
                    if w.get_id() != v.get_id():
                        for parent in w.get_parent_ids():
                            # If one of the parents of
                            # node w is in the dist dictionary
                            if parent in dist:
                                # We take the parent of dist maximum
                                parent_max = max(dict, key=dict.get)
                                # We give the value of parent_max to dist[w]
                                dist[w] = dist[parent] + 1
                                # We save the parent_max node in prev[w]
                                prev[w] = parent_max
        path = [v]
        node = v
        while node != u:
            node = previous[node]
            path.insert(0, node)
        return path, len(path)

    def node_fusion(self, first_id, second_id, label=None):
        '''
        Function that fusion two nodes
        '''
        # We check if the nodes are in the graph
        node_ids = self.get_node_ids()
        # If not, we print an error
        # (n.b : we could just say "okay let's do nothing")
        if first_id not in node_ids or second_id not in node_ids:
            print("Il existe pas")

        # Getting nodes
        first_node = self.get_node_by_id(first_id)  # The one saved
        second_node = self.get_node_by_id(second_id)  # The one killed

        # Fusion of inputs & outputs
        for id in second_node.get_input_ids():
            first_node.add_input_id(id)
        for id in second_node.get_output_ids():
            first_node.add_output_id(id)
        # Fusion of parents & children
        for child_id in second_node.get_children_ids():
            first_node.add_child_id(child_id)
        for parent_id in second_node.get_children_ids():
            first_node.add_child_id(parent_id)

        # The user can set his own label to the fusion
        if label:
            first_node.set_label(label)

        # GO TO HELL WE DON'T NEED YOU ANYMORE
        self.remove_node_by_id(second_id)


class bool_circ(open_digraph):
    def __init__(self, check=True, *args):
        '''
        **TYPE** boolean
        g: open_digraph or string
        returns True if the graph g is a boolean circuit,
        and creates the instance
        '''

        g = args[0]
        # If g is a string, we create it by parsing
        if isinstance(g, str):
            # Question 4
            if (len(args) > 1):
                self = bool_circ(args.pop(0))
                self.iparallel(bool_circ(args[0]).to_graph())
            else:
                graph = super().__init__([], [], [node(0, '', [], [])])
                current_node = 0
                s2 = ""
                for char in g:
                    if (char == '('):
                        node = graph.get_node_by_id(current_node)
                        node.set_label(node.get_label() + s2)
                        id = graph.add_node()
                        node.add_parent_id(id)
                        current_node = id
                        s2 = ""
                    elif (char == ')'):
                        node = graph.get_node_by_id(current_node)
                        node.set_label(node.get_label() + s2)
                        current_node = node.get_children_ids()[0].get_id()
                        s2 = ""
                    else:
                        s2 += char
                # Question 3
                for node in graph:
                    graph.remove_all(node)
                    for second_node in graph:
                        if (node.get_label() == second_node.get_label()):
                            self.node_fusion(node.get_id(),
                                             second_node.get_id())
                for node in graph:
                    node.set_label("")

                g = graph

        self.inputs = g.get_input_ids()
        self.outputs = g.get_output_ids()
        self.nodes = g.get_id_node_map()
        # We check that the boolean circuit is well formed,
        # to know if we can actually create it
        if (check and not self.is_well_formed()):
            print("Attention votre circuit n'est pas bien formé : ", g)

    def to_graph(self):
        '''
        **TYPE** open_digraph
        That fonction converts a bool_circ into a open_digraph and return it
        '''
        return open_digraph(self.get_input_ids(),
                            self.get_output_ids(),
                            self.get_nodes())

    def is_well_formed(self):
        '''
        **TYPE** boolean
        That fonction tests if the bool_circ is well formed.
        i.e. if he is acyclic and respects th degrees constraints

        We could have nodes with the '0' or the '1' value to
        represent the 0 and 1 constants

        A well formed bool_circ :
        - has all of his copy nodes with one input
        - has all of his AND and OR gates with one output
        - has all of his NOT gate with one input and one output
        - is not cyclic
        '''
        for node in self.get_nodes():
            label = node.get_label()
            if (label == "&"):
                if (node.outdegree() != 1):
                    return False
            if (label == "|"):
                if (node.outdegree() != 1):
                    return False
            if (label == "~"):
                if (node.indegree() != 1 or node.outdegree() != 1):
                    return False
            if (label == ""):
                if (node.indegree() != 1):
                    return False
            else:
                return False
        if self.is_cyclic():
            return False

        return True
