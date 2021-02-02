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
        s = "id: {} \nlabel: {}".format(self.id, self.label)
        s += "\nparents: "
        s += '{}'.format(self.parents, sep=' ')
        s += "\nchildren: "
        s += '{}'.format(self.children, sep=' ')
        return s

    '''
    **Example**
    node(0, d, [2, 3, 4], [5, 6])
    '''
    def __repr__(self):
        s = 'node({}, {}, '.format(self.id, self.label)
        s += '{}'.format(self.parents, sep=',')
        s += ', '
        s += '{}'.format(self.children, sep=',')
        s += ')'
        return s

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

    '''
    **EXAMPLE**
    inputs : [0, 1]
    outputs : [2]
    nodes : 4
    '''
    def __str__(self):
        s = "inputs: "
        s += '{}'.format(self.inputs, sep=',')
        s += "\noutputs: "
        s += '{}'.format(self.outputs, sep=',')
        s += "\nnodes: "
        for i in self.nodes:
            s += "{}, ".format(i) #Virgule
        return s

    '''
    **EXAMPLE**
    open_digraph([0,1], [2], [node(4, 'i', [0, 2], [3])])
    '''
    def __repr__(self):
        s = "open_digraph("
        s += '{}'.format(self.inputs, sep=',')
        s += ', '
        s += '{}'.format(self.outputs, sep=',')
        s += ', ['
        for i in self.nodes.values():
            s += "{}, ".format(repr(i)) '''Trouver un moyen d'enlever la dernière virgule'''
        s += '] )'
        return s

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
