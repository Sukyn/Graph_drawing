import sys
from modules.utils import *
sys.path.append('../')


def boolean_graph():
    '''
    create and return a logical well formed graph possibly boolean
    with :
        2 inputs
        2 outputs
        max_indegree = 2
        max_outdegree = 2
        min_indegree = 1
        min_outdegree = 1
    '''
    node1 = odgraph.node(0,'',[],[1, 3])
    node2 = odgraph.node(1,'&',[0,2],[])
    node3 = odgraph.node(2,'',[],[1, 3])
    node4 = odgraph.node(3,'|',[0,2],[4])
    node5 = odgraph.node(4,'~',[3],[])
    nodelist = [node1,node2,node3,node4,node5]
    g = odgraph.open_digraph([0,2], [1,4], nodelist)

    return g

def cyclic_not_well_formed():
    '''
    create and return a cyclic not well formed graph possibly boolean
    with :
        3 inputs
        2 outputs
        max_indegree = 4
        max_outdegree = 2
        min_indegree = 0
        min_outdegree = 1
    '''
    node1 = odgraph.node(5,'&',[6, 8],[6])
    node2 = odgraph.node(6,'~',[5],[5,7])
    node3 = odgraph.node(7,'&',[6],[])
    node4 = odgraph.node(8,'',[],[5])
    nodelist = [node1,node2,node3,node4]
    h = odgraph.open_digraph([5,5,6],[5,7], nodelist)

    return h

def normal_graph():
    '''
    create and return a logical well formed normal graph
    with :
        2 inputs
        1 outputs
        max_indegree = 2
        max_outdegree = 3
        min_indegree = 0
        min_outdegree = 0
    '''
    node0 = odgraph.node(0,'0',[],[3])
    node1 = odgraph.node(1,'1',[],[4,5,8])
    node2 = odgraph.node(2,'2',[],[4])
    node3 = odgraph.node(3,'3',[0],[5,6,7])
    node4 = odgraph.node(4,'4',[1,2],[6])
    node5 = odgraph.node(5,'5',[1,3],[7])
    node6 = odgraph.node(6,'6',[3,4],[8,9])
    node7 = odgraph.node(7,'7',[3,5],[])
    node8 = odgraph.node(8,'8',[1,6],[])
    node9 = odgraph.node(9,'9',[6],[])
    nodelist = [node0,node1,node2,node3,node4,node5,node6,node7,node8,node9]
    g = odgraph.open_digraph([0,2], [7], nodelist)
    return g

def cyclic_graph():
    '''
    create and return a logical well formed cyclic graph possibly boolean
    with :
        2 inputs
        0 outputs
        max_indegree = 2
        max_outdegree = 2
        min_indegree = 1
        min_outdegree = 0
    '''
    node10 = odgraph.node(1,'',[],[2])
    node11 = odgraph.node(2,'&',[1,4],[4])
    node12 = odgraph.node(3,'',[],[4])
    node13 = odgraph.node(4,'|',[2,3],[2])
    nodelist3 = [node10,node11,node12,node13]
    i = odgraph.open_digraph([1,3],[],nodelist3)
    return i

def not_well_formed():
    '''
    create and return a not well formed graph possibly boolean
    with :
        0 inputs
        0 outputs
        max_indegree = 2
        max_outdegree = 2
        min_indegree = 0
        min_outdegree = 0
    '''
    node14 = odgraph.node(1,'',[],[2])
    node15 = odgraph.node(2,'&',[1],[3,4])
    node16 = odgraph.node(3,'|',[2],[4])
    node17 = odgraph.node(4,'~',[2,3],[5,5])
    node18 = odgraph.node(5,'',[4,4],[])

    '''
                1  ---> 2 ---> 3
                        |      |
                        v      |
                5<------4<------
                /\      |
                |--------
    '''
    nodelist4 = [node14,node15,node16,node17,node18]
    j = odgraph.open_digraph([],[],nodelist4)
    return j

def composed_graph():
    '''
    create and return 4 graphs in one
    with :
        0 inputs
        0 outputs
        max_indegree = 1
        max_outdegree = 1
        min_indegree = 0
        min_outdegree = 0
    '''
    node1 = odgraph.node(1,'1',[],[2])
    node2 = odgraph.node(2,'2',[1],[])
    node3 = odgraph.node(3,'3',[],[])
    node4 = odgraph.node(4,'4',[],[])
    node5 = odgraph.node(5,'5',[7],[6])
    node6 = odgraph.node(6,'6',[5],[7])
    node7 = odgraph.node(7,'7',[6],[5])
    node8 = odgraph.node(8,'8',[],[10])
    node9 = odgraph.node(9,'9',[],[10])
    node10 = odgraph.node(10,'10',[8,9],[11])
    node11 = odgraph.node(11,'11',[10],[])

    nodelist = [node1,node2,node3,node4,node5,node6,node7,node8,node9,node10,node11]
    super_graph = odgraph.open_digraph([1,3],[2,3],nodelist)
    return super_graph
