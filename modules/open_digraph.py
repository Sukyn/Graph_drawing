from modules.utils import *

class node:

    '''
    identity: int; its unique id in the graph
    label: string;
    parents: int list; a sorted list containing the ids of its parents
    children: int list; a sorted list containing the ids of its children
    '''
    def __init__(self, identity, label, parents, children):
        self.id = identity
        self.label = label
        self.parents = parents
        self.children = children

    '''
    **Example**
    id : 0
    label : d
    parents : [2, 3, 4]
    children : [5, 6]
    '''
    def __str__(self):
        return ("("+str(self.id)+", "+self.label+", "
              +str(self.parents)+", "+str(self.children)+")")

    '''
    **Example**
    node(0, d, [2, 3, 4], [5, 6])
    '''
    def __repr__(self):
        return "node"+str(self)

    '''
    function that returns a copy of the object
    '''
    def copy(self):
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
        return [i for i in self.parents]
    def get_children_ids(self):
        return [i for i in self.children]

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
        try:
            self.parents.remove(id)
        except ValueError:
            pass
    def remove_child_id(self, id):
        try:
            self.children.remove(id)
        except ValueError:
            pass
    def remove_parent_id_all(self, id):
        remove_all(self.parents, id)
    def remove_child_id_all(self, id):
        remove_all(self.children, id)








class open_digraph: # for open directed graph


    '''
    inputs: int list; the ids of the input nodes
    outputs: int list; the ids of the output nodes
    nodes: node list;
    '''
    def __init__(self, inputs, outputs, nodes):
        self.inputs = inputs
        self.outputs = outputs
        self.nodes = {node.id:node for node in nodes} # self.nodes: <int,node> dict
        self.ids = [node.id for node in nodes]



    '''
    **EXAMPLE**
        ([0, 1], [2], 4)
    '''
    def __str__(self):
        return ("("+str(self.inputs)+", "+str(self.nodes)
                    +", "+str(self.outputs)+")")

    '''
    **EXAMPLE**
    open_digraph([0,1], [2], [node(4, 'i', [0, 2], [3])])
    '''
    def __repr__(self):
        return "open_digraph"+str(self)

    '''
    constructor of an empty graph
    no inputs, no outputs, no nodes
    '''
    def empty():
        return open_digraph([],[],[])

    '''
    function that returns a copy of the object
    '''
    def copy(self):
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
        return self.nodes.values()
    def get_node_ids(self):
        return [i for i in self.nodes]
    def get_node_by_id(self, id):
        return self.nodes[id]
    def get_nodes_by_ids(self, idlist):
        return [self.nodes[i] for i in idlist]

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
        '''pas fait'''
        return None

    '''
    function that returns an used id for an edge
    '''
    def new_id(self):
        id = 0
        while(self.ids.count(id) > 0):
            id += 1
        return id


    def add_edge(self, src, tgt):
        self.get_node_by_id(src).children.append(tgt)
        self.get_node_by_id(tgt).parents.append(src)

    def add_node(self, label = '', parents = [], children = []):
        id = self.new_id()
        node = node(id, label, parents, children)
        self.nodes[node.id] = node
        for parent in parents:
            self.add_edge(parent, id)
        for child in children:
            self.add_edge(id, child)
        return id

    def remove_edge(self, src, tgt):
        try:
            self.get_node_by_id(src).children.remove(tgt)
            self.get_node_by_id(tgt).parents.remove(src)
        except ValueError:
            print("The edge doesn't exist")

    def remove_node_by_id(self, id):
        try:
            del self.nodes[id]
        except KeyError:
            print("The node doesn't exist")

    def remove_edges(self, src, tgt):
        try:
            while(True):
                remove_edge(src,tgt)
        except ValueError:
            pass

    def remove_nodes_by_id(self, id):
        try:
            while(True):
                del self.nodes[id]
        except KeyError:
            pass


    def is_well_formed(self):
        for node_id in self.nodes:
            if self.nodes[node_id].id != node_id:
                return False

        for inp in self.inputs:
            if inp not in self.nodes:
                return False
        for outp in self.outputs:
            if outp not in self.nodes:
                return False

        for node in self.nodes:
            for child in node.children:
                n = count_occurence(node.children, child)
                if (count_occurence(self.nodes[child].parents, node.id) != n):
                    return False

        return True
        # utiliser count_occurence(l, x) dans utils


''' Explications:
Exemple de différence entre __str__ et __repr__
    str :
        26/01/2021
    repr :
        datetime.datetime(26, 01, 2021)

fruits = {4:'banane', 'pomme':'pomme rouge', 'nb':80}
fruits['pomme'] va renvoyer 'pomme rouge'
fruits['fraise'] = "j'adore les fraise" ajoute une valeur
for key, value in fruits.items() :
    print(value) parcourt la liste'''
