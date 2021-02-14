import sys
sys.path.append('../') # allows us to fetch files from the project root
import unittest
from modules.utils import *
import modules.open_digraph as odgraph

class FunctionTest(unittest.TestCase):
    def remove_all_test(self):
        list1 = []
        list2 = [1, 2, 3]
        list3 = [1, 1, 2, 1]
        assertEqual(list1, remove_all(list1, 3))
        assertEqual(list2, remove_all(list2, 4))
        assertEqual([1, 3], remove_all(list2, 2))
        assertEqual([2], remove_all(list3, 1))

    def count_occurence_test(self):
        list1 = []
        list2 = [1, 2, 3]
        list3 = [1, 1, 2, 1]
        assertEqual(count_occurence(list1, 2), 0)
        assertEqual(count_occurence(list2, 2), 1)
        assertEqual(count_occurence(list3, 4), 0)
        assertEqual(count_occurence(list3, 1), 3)


    def test_random_list(self):
        list1 = random_int_list(20, 3)
        print("\nrandom list :")
        print(list1)


    def test_matrix(self):
        matrix1 = random_matrix(3, 9)
        print("\nnormal matrix :")
        for line in matrix1:
            print(line)

        matrix2 = random_matrix(3, 9, null_diag = True)
        print("\nmatrix with a zero diagonal :")
        for line in matrix2:
            print(line)
        #assertEqual(matrix2[0][0], 0)
        #assertEqual(matrix2[1][1], 0)
        #assertEqual(matrix2[2][2], 0)

        matrix3 = random_matrix(3, 9, symetric = True)
        print("\nsymetrix matrix :")
        for line in matrix3:
            print(line)
        #assertEqual(matrix3[0][1], matrix3[2][1])
        #assertEqual(matrix3[0][2], matrix3[3][1])
        #assertEqual(matrix3[1][2], matrix3[3][2])

        matrix4 = random_matrix(3, 9, oriented = True)
        print("\noriented matrix :")
        for line in matrix4:
            print(line)
        '''if(matrix4[0][1] != 0):
            assertEqual(matrix4[2][1],0)
        if(matrix4[0][2] != 0):
            assertEqual(matrix4[3][1],0)
        if(matrix4[1][2] != 0):
            assertEqual(matrix4[3][2],0)'''

        matrix5 = random_matrix(3, 9, triangular = True)
        print("\ntriangular matrix :")
        for line in matrix5:
            print(line)
        #assertEqual(matrix5[1][0],0)
        #assertEqual(matrix5[2][0],0)
        #assertEqual(matrix5[2][1],0)

    def test_graph_from_adjancy_matrix(self):
        m = random_matrix(3,1)
        print("\nmatrice :")
        for line in m:
            print(line)
        g = graph_from_adjacency_matrix(m)
        print("\ngraphe :")
        print(g)


    def test_random_graph(self):
        node1 = odgraph.node(1,"first node",[],[])
        node2 = odgraph.node(2,"second node",[],[])
        graph = random_graph(3, 1, [node1], [node2])

        print("\n")
        print(graph)



if __name__ == '__main__':  # the following code is called only when
    unittest.main()         # precisely this file is run
