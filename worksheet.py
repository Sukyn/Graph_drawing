import inspect
from modules.open_digraph import *

if __name__ == '__main__':
    n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
    g = open_digraph([1], [2], n0list)
    print(g)
    print(dir(open_digraph))
    print(inspect.getsourcefile(open_digraph)) #pas testé
