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
