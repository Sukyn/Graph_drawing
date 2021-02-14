import inspect
from modules.open_digraph import *

if __name__ == '__main__':
    print("methodes de la classe node:")
    print(dir(node))

    print("\nmethodes de la classe open_digraph:")
    print(dir(open_digraph))

    print("\ncode source de la méthode new_id():")
    print(inspect.getsource(open_digraph.new_id))

    print("doc de la méthode new_id():")
    print(inspect.getdoc(open_digraph.new_id))

    print("\nfichier dans lequel la méthode new_id() se trouve:")
    print(inspect.getfile(open_digraph.new_id))
