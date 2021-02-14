import random
import modules.open_digraph as odgraph

def remove_all(l, x):
    try:
        while(True):
            l.remove(x)
    except ValueError:
        pass

def count_occurence(l, x):
    return l.count(x)


def random_int_list(n, bound):
    return [random.randrange(bound+1) for i in range(n)]


def random_matrix(n, bound, null_diag=False, symetric=False, oriented=False, triangular=False):
    matrix = [random_int_list(n, bound) for i in range(n)]
    if (null_diag):
        for x in range(n):
            matrix[x][x] = 0

    if (oriented):
        for i in range(n):
            for j in range(i+1,n):
                if(matrix[j][i] > 0):
                    matrix[i][j] = 0

    if (symetric):
        for x in range(n):
            for y in range(x+1, n):
                matrix[x][y] = matrix[y][x]

    if (triangular):
        for i in range(n):
            for j in range(i+1,n):
                matrix[j][i] = 0

    return matrix


def graph_from_adjacency_matrix(matrix):
    node_list = [odgraph.node(i, '{}'.format(i), [], []) for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(matrix[i][j]):
                node_list[j].add_parent_id(i)
                node_list[i].add_child_id(j)
    return odgraph.open_digraph([], [], node_list)



def random_graph(n, bound, inputs=0, outputs=0, form="free"):
    '''
    pour form on a differentes options :
        "free": un graphe quelconque
        "DAG" : un graphe dirige acyclique
        "oriented" : un graphe oriente
        "undirected" : un graphe non dirige
        "loop-free undirected" : ___________
    '''
    if (form == "free"):
        graphe = graph_from_adjacency_matrix( random_matrix(n, bound) )
    if (form == "DAG"):
        graphe = graph_from_adjacency_matrix( random_matrix(n, bound, triangular = True) )
    elif (form == "oriented"):
        graphe = graph_from_adjacency_matrix( random_matrix(n, bound, oriented = True) )
    elif (form == "undirected"):
        graphe = graph_from_adjacency_matrix( random_matrix(n, bound, oriented = False) )
    elif (form == "loop-free undirected"):
        graphe = graph_from_adjacency_matrix( random_matrix(n, bound, null_diag = True) )
    else:
        print("Invalid parameters")
        
    graphe.set_input_ids(inputs)
    graphe.set_output_ids(outputs)
    return graphe
