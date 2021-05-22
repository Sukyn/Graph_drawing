import sys
import unittest
import data
from modules.bool_circ import *
from modules.utils import *
sys.path.append('../')  # allows us to fetch files from the project root

class BoolCircTest(unittest.TestCase):

    # Test of boolean circuit initialization
    def test_init_bool_birc(self):
        # A boolean circuit is a graph
        # with some particularities
        # '' are input nodes
        # '&' are AND nodes
        # '|' are OR nodes
        # '~'' are NOT nodes
        # It allows us to make logical phrases'

        # Nodes initialization
        node1 = node(0, '',  [],     [1, 3])
        node2 = node(1, '&', [0, 2], [])
        node3 = node(2, '',  [],     [1, 3])
        node4 = node(3, '|', [0, 2], [4])
        node5 = node(4, '~', [3],    [])
        nodelist = [node1, node2, node3, node4, node5]
        # Graph initialization
        g = open_digraph([0, 2], [1, 4], nodelist)
        # Boolean circuit conversion
        b1 = bool_circ(g)

        # Checking values
        self.assertEqual(b1.get_input_ids(), [0, 2])
        self.assertEqual(b1.get_output_ids(), [1, 4])
        self.assertEqual(b1.get_nodes(), nodelist)

        # here is another example...
        node6 = node(5, '&', [6, 8], [6])
        node7 = node(6, '~', [5],    [5, 7])
        node8 = node(7, '&', [6],    [])
        node9 = node(8, '',  [],     [5])
        nodelist2 = [node6, node7, node8, node9]
        h = open_digraph([5, 5, 6], [5, 7], nodelist2)
        # But this one is **not** a valid boolean circuit
        # If we want to force its creation, we can put the check argument
        # as false, it will create it but it should not be
        # manipulated afterwards !!
        b2 = bool_circ(h, check=False)

        # Checking values
        self.assertEqual(b2.get_input_ids(), [5, 5, 6])
        self.assertEqual(b2.get_output_ids(), [5, 7])
        self.assertEqual(b2.get_nodes(), nodelist2)

    # Test of graph convertion management
    def test_to_graph(self):

        # Loading graph examples
        g1 = data.boolean_graph()
        g2 = data.cyclic_not_well_formed()
        g3 = data.cyclic_graph()
        g4 = data.not_well_formed()

        # Conversion to boolean circuit
        # Note : we set the check argument to false
        # so it forces the creation of the boolean circuit
        # even if it it not well formed and shouldn't manipulated
        b1 = bool_circ(g1, check=False)
        b2 = bool_circ(g2, check=False)
        b3 = bool_circ(g3, check=False)
        b4 = bool_circ(g4, check=False)
        # Convertion of the boolean circuits into open digraphs
        # Even if the boolean circuits are not valid, we can convert
        # them into graphs
        b1.to_graph()
        b2.to_graph()
        b3.to_graph()
        b4.to_graph()
        # We check that the reverse conversion returns the same thing
        # as the original graph
        self.assertEqual(b1, g1)
        self.assertEqual(b2, g2)
        self.assertEqual(b3, g3)
        self.assertEqual(b4, g4)

    # Test of circuit's validity checking
    def test_is_well_formed(self):

        # Creation of open_digraphs
        g1 = data.boolean_graph()
        g2 = data.cyclic_not_well_formed()
        g3 = data.cyclic_graph()
        g4 = data.not_well_formed()

        # On teste si l'appel de bool_circ
        # print un message d'erreur ou non (il faudra
        # remplacer par des Raise)
        b1 = bool_circ(g1)  # On n'a pas de message d'erreur
        # print("We'll have 3 error messages : ")
        # b2 = bool_circ(g2)  # On a bien un message d'erreur
        # b3 = bool_circ(g3)  # On a bien un message d'erreur
        # b4 = bool_circ(g4)  # On a bien un message d'erreur
        '''
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        # TO DO : REMPLACER LES PRINT PAR DES RAISE
        '''

    '''
    # TO DO -----
    # TO DO -----
    # TO DO -----
    # TO DO -----
    # TO DO -----
    # TO DO -----
    # TO DO -----
    # TO DO -----
    # TO DO -----
    '''
    '''Test TD10'''
    def test_random_bool_circ(self):
        # creation of 5 random bool_circ
        rand_bool1 = bool_circ.random_bool_circ(5,  1, 1)
        rand_bool2 = bool_circ.random_bool_circ(20, 4, 9)
        rand_bool3 = bool_circ.random_bool_circ(3,  1, 2)
        rand_bool4 = bool_circ.random_bool_circ(10, 3, 2)
        rand_bool5 = bool_circ.random_bool_circ(10, 3, 2)

        # on vérifie qu'il y a le bon nombre d'input et de output
        # pour vérifier si le graph est bien formé on regarde
        # s'il y a un message d'erreur
        self.assertEqual(len(rand_bool1.get_input_ids()),  1)
        self.assertEqual(len(rand_bool1.get_output_ids()), 1)
        self.assertEqual(len(rand_bool2.get_input_ids()),  4)
        self.assertEqual(len(rand_bool2.get_output_ids()), 9)
        self.assertEqual(len(rand_bool3.get_input_ids()),  1)
        self.assertEqual(len(rand_bool3.get_output_ids()), 2)
        self.assertEqual(len(rand_bool4.get_input_ids()),  3)
        self.assertEqual(len(rand_bool4.get_output_ids()), 2)
        self.assertEqual(len(rand_bool5.get_input_ids()),  3)
        self.assertEqual(len(rand_bool5.get_output_ids()), 2)

    def test_11_05(self):
        for x in range(20):
            for y in range(20):
                for z in range(2):
                    registre1 = bool_circ.registre(x)
                    self.assertEqual(bool_circ.binary_from_registre(registre1), x)
                    registre2 = bool_circ.registre(y)
                    self.assertEqual(bool_circ.binary_from_registre(registre2), y)
                    retenue = bool_circ.registre(z, 1)
                    self.assertEqual(bool_circ.binary_from_registre(retenue), z)

                    final_adder = bool_circ.adder(registre1, registre2, retenue)
                    final_half_adder = bool_circ.half_adder(registre1, registre2)
                    self.assertEqual(bool_circ.binary_from_registre(final_adder), x+y+z)
                    self.assertEqual(bool_circ.binary_from_registre(final_half_adder), x+y)

if __name__ == '__main__':  # the following code is called only when
    unittest.main()         # precisely this file is run
