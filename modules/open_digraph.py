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

    def __str__(self):
        s = "id: {} \nlabel: {}".format(self.id, self.label)
        s += "\nparents: "
        for i in self.parents:
            s += "{} ".format(i)
        s += "\nchildren: "
        for i in self.children:
            s += "{} ".format(i)
        return s

    def __repr__(self):
        s = 'node({}, {},'.format(self.id, self.label)
        s += '['
        for i in self.parents:
            s += '{},'.format(i)
        s += '],'
        s += '['
        for i in self.children:
            s += '{},'.format(i)
        s += '])'
        return s

    ''' Exemple de différence entre __str__ et __repr__
    str :
        26/01/2021
    repr :
        datetime.datetime(26, 01, 2021)
    '''

    def copy(self):
        return node(self.id, self.label, self.parents, self.children)

    #getters
    def get_id(self):
        return self.id
    def get_label(self):
        return self.label
    def get_parent_ids(self):
        return [i for i in self.parents]
    def get_children_ids(self):
        return [i for i in self.children]

    #setters
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

    def __str__(self):
        s = "inputs: "
        for i in self.inputs:
            s += '{},'.format(i)
        s += "\noutputs: "
        for i in self.outputs:
            s += '{},'.format(i)
        s += "\nnodes: "
        for i in self.nodes:
            s += "{}, ".format(i)
        return s

    def __repr__(self):
        s = "open_digraph( ["
        for i in self.inputs:
            s += '{},'.format(i)
        s += '], ['
        for i in self.outputs:
            s += '{},'.format(i)
        s += '], ['
        for i in self.nodes:
            s += '{},'.format(i)
        s += '] )'
        return s

    def empty():
        return open_digraph([],[],[])

    def copy(self):
        # Il faut passer un tableau et non paramètre et pas un dictionnaire (nodes)
        return open_digraph(self.inputs, self.outputs, [value for key, value in self.nodes.items()])

    #getters
    def get_input_ids(self):
        return self.inputs

    def get_output_ids(self):
        return self.outputs

    def get_id_node_map(self):
        '''
        fruits = {4:'banane', 'pomme':'pomme rouge', 'nb':80}
        fruits['pomme'] va renvoyer 'pomme rouge'
        fruits['fraise'] = "j'adore les fraise" ajoute une valeur
        for key, value in fruits.items() :
            print(value) parcourt la liste
        '''
        #renvoie un dictionnaire id:node

        #Problème : i est un entier (l'id du noeud)
        return {i.get_id():i for i in self.nodes}

    def get_nodes(self):
        return [i for i in self.nodes]

    def get_node_ids(self):
        #Problème : i est un entier (l'id du noeud)
        return [i.get_id() for i in self.nodes]

    def get_node_by_id(self, id):
        #Forcément cassé du coup
        return self.get_id_node_map()[id]

    def get_nodes_by_ids(self, idlist):
        #Forcément cassé du coup
        return [self.get_id_node_map()[i] for i in idlist]

    #setters
    def set_input_ids(self, new_idlist):
        self.inputs = new_idlist

    def set_output_ids(self, new_idlist):
        self.outputs = new_idlist

    def add_input_id(self, new_id):
        self.inputs.append(new_id)

    def add_output_id(self, new_id):
        self.outputs.append(new_id)


    def new_id(self):
        return
