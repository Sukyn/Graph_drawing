import sys
sys.path.append('../') # allows us to fetch files from the project root
import unittest
from modules.utils import *

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
        #print(list1)
        matrix1 = random_matrix(3, 2, oriented=True)
        for line in matrix1:
            print(line)

        g = graph_from_adjacency_matrix(matrix1)
        print(g)

if __name__ == '__main__':  # the following code is called only when
    unittest.main()         # precisely this file is run
