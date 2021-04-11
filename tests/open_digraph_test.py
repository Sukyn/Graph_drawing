import sys
sys.path.append('../')# allows us to fetch files from the project root
import unittest
from modules.open_digraph import *


class InitTest(unittest.TestCase):
    def test_init_node(self):
        n0 = node(0, 'i', [], [1])
        self.assertEqual(n0.id, 0)
        self.assertEqual(n0.label, 'i')
        self.assertEqual(n0.parents, [])
        self.assertEqual(n0.children, [1])
        self.assertIsInstance(n0, node)

    def test_init_open_digraph(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        self.assertEqual(g.nodes[0], n0list[0])
        self.assertEqual(g.inputs, [1])
        self.assertEqual(g.outputs, [2])
        self.assertIsInstance(g, open_digraph)
        self.assertIsInstance(n0list[0], node)

class NodeTest(unittest.TestCase):

    def test_repr(self):
        n0 = node(0, 'i', [], [1])
        '''
        print("------ NODE STR ------")
        print(n0)
        print("------ NODE REPR ------")
        print(repr(n0))
        '''

    # Tests de copy
    def test_copy(self):
        n0 = node(0, 'i', [], [1])
        n0copy = n0.copy()
        self.assertEqual(n0copy.id, n0.id)
        self.assertEqual(n0copy.label, n0.label)
        self.assertEqual(n0copy.parents, n0.parents)
        self.assertEqual(n0copy.children, n0.children)

    # Tests des getters
    def test_getters(self):
        n0 = node(0, 'i', [], [1])
        self.assertEqual(n0.get_id(), 0)
        self.assertEqual(n0.get_label(), 'i')
        self.assertEqual(n0.get_parent_ids(), [])
        self.assertEqual(n0.get_children_ids(), [1])

    # Tests des setters
    def test_setters(self):
        n0 = node(0, 'i', [], [1])

        n0.set_id(3)
        self.assertEqual(n0.get_id(), 3)

        n0.set_label('j')
        self.assertEqual(n0.get_label(), 'j')

        n0.set_parent_ids([2, 3])
        self.assertEqual(n0.get_parent_ids(), [2, 3])

        n0.set_children_ids([])
        self.assertEqual(n0.get_children_ids(), [])

        n0.add_parent_id(7)
        self.assertEqual(n0.get_parent_ids(), [2, 3, 7])

        n0.add_child_id(8)
        self.assertEqual(n0.get_children_ids(), [8])

    def test_remove(self):
        n0 = node(0, 'i', [], [1])

        n0.add_parent_id(7)
        n0.remove_parent_id(7)
        self.assertEqual(n0.get_parent_ids(), [])

        n0.set_children_ids([7,8])
        n0.remove_child_id(7)
        self.assertEqual(n0.get_children_ids(), [8])

        n0.set_parent_ids([2, 2])
        n0.remove_parent_id_all(2)
        self.assertEqual(n0.get_parent_ids(), [])

        n0.set_children_ids([3,3,4])
        n0.remove_child_id_all(3)
        self.assertEqual(n0.get_children_ids(), [4])

    '''TEST TD6'''
    def exemples_de_node(self):
        '''
        on renvoie un couple de node exemples pour faire les tests
        '''
        node1 = odgraph.node(0, "Isabelle", [], [1,2,7,3,5,2,2])
        node2 = odgraph.node(1, "Adjani", [4,4], [7,5,5,8])
        return (node1,node2)

    def test_indegree(self):
        node1, node2 = self.exemples_de_node()
        self.assertEqual(node1.indegree(), 0)
        self.assertEqual(node2.indegree(), 2)

    def test_outdegree(self):
        node1, node2 = self.exemples_de_node()
        self.assertEqual(node1.outdegree(), 7)
        self.assertEqual(node2.outdegree(), 4)

    def test_degree(self):
        node1, node2 = self.exemples_de_node()
        self.assertEqual(node1.degree(), 7)
        self.assertEqual(node2.degree(), 6)


class GraphTest(unittest.TestCase):
    def test_repr(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        '''
        print("------ GRAPHE STR ------")
        print(g)
        print("------ GRAPHE REPR ------")
        print(repr(g))
        '''

    # Tests de Empty
    def test_empty(self):
        g = open_digraph.empty()
        self.assertEqual(open_digraph.empty().inputs, [])
        self.assertEqual(open_digraph.empty().outputs, [])
        self.assertEqual(open_digraph.empty().nodes, {})

    # Tests de copy
    def test_copy(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        gCopy = g.copy()
        self.assertEqual(gCopy.inputs, g.inputs)
        self.assertEqual(gCopy.outputs, g.outputs)
        self.assertEqual(gCopy.nodes, g.nodes.copy())

    # Tests des getters
    def test_getters(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        self.assertEqual(g.get_input_ids(), [1])
        self.assertEqual(g.get_output_ids(), [2])
        self.assertEqual(g.get_nodes(), n0list)
        self.assertEqual(g.get_node_ids(), [0, 1, 2, 3, 4])
        self.assertEqual(g.get_id_node_map(), {0:n0list[0],
                                               1:n0list[1],
                                               2:n0list[2],
                                               3:n0list[3],
                                               4:n0list[4]})
        self.assertEqual(g.get_node_by_id(3), n0list[3])
        self.assertEqual(g.get_nodes_by_ids([3, 4]), [n0list[3], n0list[4]])

    # Tests des setters
    def test_setters(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        g.set_input_ids([3, 4])
        self.assertEqual(g.get_input_ids(), [3, 4])
        g.set_output_ids([])
        self.assertEqual(g.get_output_ids(), [])
        g.add_input_id(5)
        self.assertEqual(g.get_input_ids(), [3, 4, 5])
        g.add_output_id(2)
        self.assertEqual(g.get_output_ids(), [2])

    def test_new_id(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        id = g.new_id()
        self.assertEqual(g.new_id(), 5)

    def test_edges_management(self):
        n0list = [node(i, '{}'.format(i), [], []) for i in range(5)]
        g = open_digraph([1], [2], n0list)

        g.add_edge(2, 3)
        self.assertEqual(g.get_node_by_id(3).get_parent_ids(), [2])
        self.assertEqual(g.get_node_by_id(2).get_children_ids(), [3])
        g.remove_edge(2, 3)
        self.assertEqual(g.get_node_by_id(3).get_parent_ids(), [])
        self.assertEqual(g.get_node_by_id(2).get_children_ids(), [])

        g.add_edges([2, 3], [1, 4])
        self.assertEqual(g.get_node_by_id(1).get_parent_ids(), [2])
        self.assertEqual(g.get_node_by_id(3).get_children_ids(), [4])

        g.add_edge(2, 1)
        g.remove_edges([2, 3], [1, 4])
        self.assertEqual(g.get_node_by_id(1).get_parent_ids(), [])

        g.add_node()
        self.assertEqual(g.get_node_ids(), [0, 1, 2, 3, 4, 5])

        g.remove_node_by_id(4)
        self.assertEqual(g.get_node_ids(), [0, 1, 2, 3, 5])
        g.remove_nodes_by_id([2,3,4, 5])
        self.assertEqual(g.get_node_ids(), [0, 1])

    def test_well_formed(self):
        n0list = [node(i, '{}'.format(i), [], []) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        self.assertEqual(g.is_well_formed(), True)

        good_list = [node(1, '1', [2, 3], [3]), node(2, '2', [], [1]), node(3, '3', [1], [1])]
        g_good = open_digraph([1], [2], good_list)
        self.assertEqual(g_good.is_well_formed(), True)

        wrong_list = [node(1, '1', [2, 3], [3]), node(2, '2', [], [1, 2]), node(3, '3', [1], [1])]
        g_wrong = open_digraph([1], [2], wrong_list)
        self.assertEqual(g_wrong.is_well_formed(), False)

        wrong_list2 = [node(1, '1', [2, 3], [3]), node(2, '2', [], [1]), node(3, '3', [1], [1])]
        g_wrong2 = open_digraph([1], [2, 4], wrong_list2)
        self.assertEqual(g_wrong2.is_well_formed(), False)

    def test_normalize(self):
        good_list = [node(1, '1', [2, 3], [3]), node(2, '2', [], [1]), node(3, '3', [1], [1])]
        g_good = open_digraph([1], [2], good_list)
        matrix = g_good.adjacency_matrix()
        '''for lin in matrix:
            print(lin)'''

    '''TEST TD6'''

    def exemples_de_graphe(self):
        '''
        on crée deux graph exemples qu'on réutilisera pour les tests
        return le couple (g,h)
        avec g un graph logique cohérant
        et h cyclique et incohérant
        '''
        node1 = odgraph.node(0,'',[],[1, 3])
        node2 = odgraph.node(1,'&',[0,2],[])
        node3 = odgraph.node(2,'',[],[1, 3])
        node4 = odgraph.node(3,'|',[0,2],[4])
        node5 = odgraph.node(4,'~',[3],[])
        nodelist = [node1,node2,node3,node4,node5]
        g = odgraph.open_digraph([0,2], [1,4], nodelist)

        node6 = odgraph.node(5,'&',[6, 8],[6])
        node7 = odgraph.node(6,'~',[5],[5,7])
        node8 = odgraph.node(7,'&',[6],[])
        node9 = odgraph.node(8,'',[],[5])
        nodelist2 = [node6,node7,node8,node9]
        h = odgraph.open_digraph([5,5,6],[5,7], nodelist2)

        return (g,h)

    def test_max_indegree(self):
        g,h = self.exemples_de_graphe()
        self.assertEqual(g.max_indegree(), 2)
        self.assertEqual(h.max_indegree(), 4)

    def test_min_indegree(self):
        g,h = self.exemples_de_graphe()
        self.assertEqual(g.min_indegree(), 1)
        self.assertEqual(h.min_indegree(), 0)

    def test_max_outdegree(self):
        g,h = self.exemples_de_graphe()
        self.assertEqual(g.max_outdegree(), 2)
        self.assertEqual(h.max_outdegree(), 2)

    def test_min_outdegree(self):
        g,h = self.exemples_de_graphe()
        self.assertEqual(g.min_outdegree(), 1)
        self.assertEqual(h.min_outdegree(), 1)

    def test_is_cyclic(self):
        g,h = self.exemples_de_graphe()
        self.assertEqual(g.is_cyclic(), False)
        self.assertEqual(h.is_cyclic(), True)

    '''Test TD7'''
    def test_min_id (self):
        g,h = self.exemples_de_graphe()
        self.assertEqual(g.min_id(),0)
        self.assertEqual(h.min_id(),5)
    def test_max_id (self):
        g,h = self.exemples_de_graphe()
        self.assertEqual(g.max_id(),4)
        self.assertEqual(h.max_id(),8)
    def test_shift_indices(self, n):
        g,h = self.exemples_de_graphe()
        g.shift_indices(3)
        self.assertEqual(g.min_id(),3)
        self.assertEqual(g.max_id(),8)
        h.shift_indices(100)
        self.assertEqual(h.min_id(),104)
        self.assertEqual(h.max_id(),108)
    def test_iparallel(self):
        g,h = self.exemples_de_graphe()
        inputs = g.get_input_ids()
        g.iparallel(h,[3],[7])
        self.assertEqual([1,2,3,4,5,6,7,8],g.get_node_ids())
        self.assertEqual(inputs + h.get_input_ids() + [3,7], g.get_input_ids())
    def test_parallel(self):
        g,h = self.exemples_de_graphe()
        g.iparallel(h,[3],[7])
        self.assertEqual([1,2,3,4,5,6,7,8],g.get_node_ids())
    def test_icompose(self):
        g,h = self.exemples_de_graphe()
        h.icompose(g)
        assertEqual(h.get_input_ids(), [5,5,6])
        assertEqual(h.get_output_ids(), [1,4])
        assertEqual(h.get_node_by_id(5).get_children_ids(), [0,6])
        assertEqual(h.get_node_by_id(7).get_children_ids(), [2])
        assertEqual(h.get_node_by_id(0).get_parents_ids(), [5])
        assertEqual(h.get_node_by_id(2).get_parents_ids(), [7])
    def test_compose(self):
        g,h = self.exemples_de_graphe()
        h.icompose(g)
        assertEqual(test.get_input_ids(), [5,5,6])
        assertEqual(test.get_output_ids(), [1,4])
        assertEqual(test.get_node_by_id(5).get_children_ids(), [0,6])
        assertEqual(test.get_node_by_id(7).get_children_ids(), [2])
        assertEqual(test.get_node_by_id(0).get_parents_ids(), [5])
        assertEqual(test.get_node_by_id(2).get_parents_ids(), [7])
    def test_connected_components(self):
        pass
    def test_graph_permutation(self):
        pass

    '''Test TD8'''
    def exemple_td8(self):
        '''
        on crée un graphe exemple qu'on réutilisera pour les tests
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
        nodelist = [node1,node2,node3,node4,node5,node6,node7,node8,node9]
        g = odgraph.open_digraph([0,2], [7], nodelist)
        return g

    def test_shortest_path(self):
        g = self.exemple_td8()
        self.assertEqual(g.shortest_path(g.get_node_by_id(0),g.get_node_by_id(3)),[g.get_node_by_id(0),g.get_node_by_id(3)])
        self.assertEqual(g.shortest_path(g.get_node_by_id(0),g.get_node_by_id(7)),[g.get_node_by_id(0),g.get_node_by_id(3),g.get_node_by_id(7)])

    def test_parents_distance(self):
        g = self.exemple_td8()
        self.assertEqual(g.parents_distance(g.get_node_by_id(5),g.get_node_by_id(8)), {0 : (2,3), 3 : (1,2), 1 : (1,1)})
    '''
    def test_topological_sorting(self):
        g = self.exemple_td8()
        self.assertEqual(g.topological_sorting(), [[0, 1, 2], [3, 4], [5, 6], [7, 8, 9]])
    '''

    '''
    def test_node_depth(self):
        g = self.exemple_td8()
        self.assertEqual(node_depth(g.get_node_by_id(0)),0)
        self.assertEqual(node_depth(g.get_node_by_id(4)),1)
        self.assertEqual(node_depth(g.get_node_by_id(5)),2)
        self.assertEqual(node_depth(g.get_node_by_id(7)),3)
    '''

    '''
    def test_graph_depth(self):
        g = self.exemple_td8()
        self.assertEqual(g.graph_depth(),4)
    '''

    '''
    def test_longest_path(self):
        g = self.exemple_td8()
        chemin, distance = g.longest_path(g.get_node_by_id(0),g.get_node_by_id(7))
        self.assertEqual(chemin,[g.get_node_by_id(0),g.get_node_by_id(3),g.get_node_by_id(5),g.get_node_by_id(7)])
        self.assertEqual(distance, 4)
    '''

class BoolCircTest(unittest.TestCase):
    '''TEST TD6'''
    def exemples_de_graphe(self):
        '''
        on crée deux graph exemples qu'on réutilisera pour les tests
        return le quadruplet (g,h,i,j)
        avec g un graph logique cohérant
        h incohérant et cyclique
        i cyclique et cohérant
        et j non-cyclique et incohérant
        '''
        node1 = odgraph.node(0,'',[],[1, 3])
        node2 = odgraph.node(1,'&',[0,2],[])
        node3 = odgraph.node(2,'',[],[1, 3])
        node4 = odgraph.node(3,'|',[0,2],[4])
        node5 = odgraph.node(4,'~',[3],[])
        nodelist = [node1,node2,node3,node4,node5]
        g = odgraph.open_digraph([0,2], [1,4], nodelist)

        node6 = odgraph.node(5,'&',[6, 8],[6])
        node7 = odgraph.node(6,'~',[5],[5,7])
        node8 = odgraph.node(7,'&',[6],[])
        node9 = odgraph.node(8,'',[],[5])
        nodelist2 = [node6,node7,node8,node9]
        h = odgraph.open_digraph([5,5,6],[5,7], nodelist2)

        node10 = odgraph.node(1,'',[],[2])
        node11 = odgraph.node(2,'&',[1,4],[4])
        node12 = odgraph.node(3,'',[],[4])
        node13 = odgraph.node(4,'|',[2,3],[2])
        nodelist3 = [node10,node11,node12,node13]
        i = odgraph.open_digraph([1,3],[],nodelist3)

        node14 = odgraph.node(1,'',[],[2])
        node15 = odgraph.node(2,'&',[1],[3,4])
        node16 = odgraph.node(3,'|',[2],[4])
        node17 = odgraph.node(4,'~',[2,3],[5])
        node18 = odgraph.node(5,'',[4,4],[])
        nodelist4 = [node14,node15,node16,node17,node18]
        j = odgraph.open_digraph([],[],nodelist4)
        return (g,h,i,j)
    '''
    def test_init(self):
        node1 = odgraph.node(0,'',[],[1, 3])
        node2 = odgraph.node(1,'&',[0,2],[])
        node3 = odgraph.node(2,'',[],[1, 3])
        node4 = odgraph.node(3,'|',[0,2],[4])
        node5 = odgraph.node(4,'~',[3],[])
        nodelist = [node1,node2,node3,node4,node5]
        g = odgraph.open_digraph([0,2], [1,4], nodelist)
        b1 = bool_circ(g, check=False)

        self.assertEqual(b1.get_input_ids(), [0,2])
        self.assertEqual(b1.get_output_ids(), [1,4])
        self.assertEqual(b1.get_nodes(), nodelist)

        node6 = odgraph.node(5,'&',[6, 8],[6])
        node7 = odgraph.node(6,'~',[5],[5,7])
        node8 = odgraph.node(7,'&',[6],[])
        node9 = odgraph.node(8,'',[],[5])
        nodelist2 = [node6,node7,node8,node9]
        h = odgraph.open_digraph([5,5,6],[5,7], nodelist2)
        b2 = bool_circ(h, check=False)

        self.assertEqual(b2.get_input_ids(), [5,5,6])
        self.assertEqual(b2.get_output_ids(), [5,7])
        self.assertEqual(b2.get_nodes(), nodelist2)
    '''

    '''
    def test_to_graph(self):
        #creation of an open_digraph
        (g1,g2,g3,g4) = self.exemples_de_graphe()

        #creation of the bool_circ from the open_digraphs
        b1 = odgraph.bool_circ(g1)
        b2 = odgraph.bool_circ(g2)
        b3 = odgraph.bool_circ(g3)
        b4 = odgraph.bool_circ(g4)
        #convertion of the bool_circs into open_digraphs
        b1.to_graph()
        b2.to_graph()
        b3.to_graph()
        b4.to_graph()
        #test the equalities
        self.assertEqual(b1,g1)
        self.assertEqual(b2, g2)
        self.assertEqual(b3, g3)
        self.assertEqual(b4, g4)
    '''

    '''
    def test_is_well_formed(self):
        (g1,g2,g3,g4) = self.exemples_de_graphe()

        # On teste si l'appel de bool_circ print un message d'erreur ou non (il faudra
        # remplacer par des Raise)

        b1 = odgraph.bool_circ(g1) # On n'a pas de message d'erreur
        b2 = odgraph.bool_circ(g2) # On a bien un message d'erreur
        b3 = odgraph.bool_circ(g3) # On a bien un message d'erreur
        b4 = odgraph.bool_circ(g4) # On a bien un message d'erreur

    '''
if __name__ == '__main__':  # the following code is called only when
    unittest.main()         # precisely this file is run
