from modules.open_digraph import *

class bool_circ(open_digraph):
    def __init__(self, *args, check=True):
        '''
        **TYPE** boolean
        g: open_digraph or string
        returns True if the graph g is a boolean circuit,
        and creates the instance
        '''

        g = args[0]
        # If g is a string, we create it by parsing
        if isinstance(g, str):
            # Question 4
            if (len(args) > 1):
                self = bool_circ(args.pop(0))
                self.iparallel(bool_circ(args[0]).to_graph())
            else:
                graph = super().__init__([], [], [node(0, '', [], [])])
                current_node = 0
                s2 = ""
                for char in g:
                    if (char == '('):
                        node = graph.get_node_by_id(current_node)
                        node.set_label(node.get_label() + s2)
                        id = graph.add_node()
                        node.add_parent_id(id)
                        current_node = id
                        s2 = ""
                    elif (char == ')'):
                        node = graph.get_node_by_id(current_node)
                        node.set_label(node.get_label() + s2)
                        current_node = node.get_children_ids()[0].get_id()
                        s2 = ""
                    else:
                        s2 += char
                # Question 4
                input_labels = []
                # Question 3
                for node in graph:
                    utils.remove_all(graph, node)
                    for second_node in graph:
                        if (node.get_label() == second_node.get_label()):
                            self.node_fusion(node.get_id(),
                                             second_node.get_id())
                            # we note the label
                            input_labels.append(node.get_label)
                for node in graph:
                    node.set_label("")

                g = graph

        self.inputs = g.get_input_ids()
        self.outputs = g.get_output_ids()
        self.nodes = g.get_id_node_map()
        # We check that the boolean circuit is well formed,
        # to know if we can actually create it
        if (check and not self.is_well_formed()):
            print("Attention votre circuit n'est pas bien formé : ", g)

    def to_graph(self):
        '''
        **TYPE** open_digraph
        That fonction converts a bool_circ into a open_digraph and return it
        '''
        return open_digraph(self.get_input_ids(),
                            self.get_output_ids(),
                            self.get_nodes())

    def is_well_formed(self):
        if not super().is_well_formed():
            return False

        for node in self.get_nodes():
            label = node.get_label()
            if ( label == "&" or
                 label == "^" or
                 label == "|" ):
                if (self.outdegree(node) != 1):
                    return False
            elif (label == "0" or label == "1"):
                if (self.indegree(node) > 0):
                    return False
            elif (label == "~"):
                if (self.indegree(node) != 1 or self.outdegree(node) != 1):
                    return False
            elif (label == ""):
                if (self.indegree(node) != 1):
                    return False
            else:
                if (self.outdegree(node) != 1 or self.indegree(node) != 1):
                    return False
        if self.is_cyclic():
            return False

        return True

    def random_bool_circ(node_number, inputs, outputs):
        '''
        **TYPE** bool_circ
        inputs : int list
        outputs : int list
        That function returns a random bool_circ with
        a number node_number of nodes
        a number inputs > 0 of inputs
        and a number outputs > 0 of outputs
        '''
        # create a random graph
        graph = open_digraph.random_graph(node_number, 1, [], [], "DAG")
        # to have indegree and maxdegree > 0S
        for node_anonymous in graph.get_nodes():
            # reset the label
            node_anonymous.set_label("")
            # make node input if it has no parent
            if not node_anonymous.get_parent_ids():
                if not node_anonymous.get_id() in graph.get_input_ids():
                    graph.add_input_id(node_anonymous.get_id())
            # make node output if it has no child
            if not node_anonymous.get_children_ids():
                graph.add_output_id(node_anonymous.get_id())

        # create a list of potential node input
        possible_node_input = graph.get_node_ids()
        for input in graph.get_input_ids():
            possible_node_input.remove(input)

        # we want to have the good number of input
        while len(graph.get_input_ids()) < inputs:
            # take a random non-input node
            choice = random.choice(possible_node_input)
            possible_node_input.remove(choice)
            # create the input
            graph.add_input_id(choice)

        while len(graph.get_input_ids()) > inputs:
            # take 2 input nodes and remove them from the inputs
            choice1 = random.choice(graph.get_input_ids())
            graph.del_input_id(choice1)
            choice2 = random.choice(graph.get_input_ids())
            graph.del_input_id(choice2)

            # create a new node which is parent of the 2 choices
            new_node_id = graph.add_node("", [], [choice1, choice2])
            # add the input
            graph.add_input_id(new_node_id)

        # create a list of potential node output
        possible_node_output = graph.get_node_ids()
        for output in graph.get_output_ids():
            possible_node_output.remove(output)

        # we want to have the good number of output
        while len(graph.get_output_ids()) < outputs:
            # take a random non-output node
            choice = random.choice(possible_node_output)
            possible_node_output.remove(choice)
            # create the output
            graph.add_output_id(choice)

        while len(graph.get_output_ids()) > outputs:
            # take 2 output nodes and remove them from the outputs
            choice1 = random.choice(graph.get_output_ids())
            graph.del_output_id(choice1)
            choice2 = random.choice(graph.get_output_ids())
            graph.del_output_id(choice2)

            # create a new node which is parent of the 2 choices
            new_node_id = graph.add_node("", [choice1, choice2], [])
            # add the input
            graph.add_output_id(new_node_id)

        # we will change all of the labels
        for node_anonymous in graph.get_nodes():
            if (graph.indegree(node_anonymous) == 1 and
                (graph.outdegree(node_anonymous) == 1):
                # we make a not node
                node_anonymous.set_label("~")
            elif (graph.indegree(node_anonymous) == 1 and
                (graph.outdegree(node_anonymous) > 1):
                # we make a copy node
                pass
            elif (graph.indegree(node_anonymous) > 1 and
                (graph.outdegree(node_anonymous) == 1):
                # we make a or or and node
                node_anonymous.set_label(random.choice(["&", "|"]))
            elif (graph.indegree(node_anonymous) > 1 and
                (graph.outdegree(node_anonymous) > 1):
                # take the parents of the node
                nodeParents = node_anonymous.get_parent_ids().copy()
                # create an intermediar node
                new_node_id = graph.add_node(random.choice(["&", "|"]),
                                             node_anonymous.get_parent_ids(),
                                             [node_anonymous.get_id()])
                # remove the parents from the node parents
                for parentId in nodeParents:
                    graph.remove_edge(parentId, node_anonymous.get_id())
                # transform the input if we have to
                if node_anonymous.get_id() in graph.get_input_ids():
                    graph.del_input_id(node_anonymous.get_id())
                    graph.add_input_id(new_node_id)

            else:
                print("There is a problem, this message shouldn't be printed")

        return bool_circ(graph)

    def registre(n, size=8):
        '''
        **TYPE** bool_circ
        n : int
        size : int
        return the graph which correspond to the number in binary
        '''
        # create the binary number
        binary_form = bin(n)[2:]
        if(len(binary_form) > size):
            print("the number is too big")
            return bool_circ(open_digraph.empty())
        binary_form = "0"*(size-len(binary_form)) + binary_form
        # create a bool_circ
        circ = bool_circ(open_digraph.empty())
        for char in binary_form:
            # add the node 0 or 1
            id = circ.add_node(label=char)
            circ.add_output_id(id)
        return circ

    def binary_from_registre(circ):
        '''
        **TYPE** int
        circ : bool_circ
        transform the register into a int
        '''
        result = 0
        for i, node in enumerate(reversed(circ.get_nodes())):
            if node.get_label() == "1":
                result += 2**i
        return result

    def apply_copy_rule(self, data_node_id, cp_node_id):
        # Copy rule :
        # On copie simplement la valeur du parent (normalement un noeud copy
        # ne peut donc avoir qu'un parent)
        self.get_node_by_id(cp_node_id).set_label(self.get_node_by_id(data_node_id).get_label())
        self.remove_edge(data_node_id, cp_node_id)

    def apply_not_rule(self, data_node_id, not_node_id):
        # Not rule :
        # On inverse la valeur du parent (normalement un noeud not
        # ne peut donc avoir qu'un parent)
        if self.get_node_by_id(data_node_id).get_label() == '0':
            self.get_node_by_id(not_node_id).set_label('1')
        else:
            self.get_node_by_id(not_node_id).set_label('0')
        self.remove_edge(data_node_id, not_node_id)

    def apply_and_rule(self, data_node_id, and_node_id):
        # And rule :
        # On vérifie que tous les parents valent 1, si on en trouve un 0
        # c'est que notre valeur vaut zéro
        if (self.get_node_by_id(data_node_id).get_label() == "1"):
            self.remove_edge(data_node_id, and_node_id)
            return
        self.get_node_by_id(and_node_id).set_label('0')
        for parent in self.get_node_by_id(and_node_id).get_parent_ids().copy():
            self.remove_edge(parent, and_node_id)

    def apply_or_rule(self, data_node_id, or_node_id):
        # Or rule :
        # On vérifie que tous les parents valent 0, si on en trouve un 1
        # c'est que notre valeur vaut un
        if (self.get_node_by_id(data_node_id).get_label() == "0"):
            self.remove_edge(data_node_id, or_node_id)
            return

        self.get_node_by_id(or_node_id).set_label('1')
        parents = self.get_node_by_id(or_node_id).get_parent_ids().copy()
        for parent in parents:
            self.remove_edge(parent, or_node_id)

    def apply_xor_rule(self, data_node_id, xor_node_id):
        # Xor rule :
        # Si on trouve un élément qui vaut 1, on inverse la valeur globale
        if (self.get_node_by_id(data_node_id).get_label() == "0"):
            self.remove_edge(data_node_id, xor_node_id)
            return

        new_id = self.add_node('~', [], [])
        if (xor_node_id in self.get_output_ids()):
            self.add_edge(xor_node_id, new_id)
            self.del_output_id(xor_node_id)
            self.add_output_id(new_id)
            self.remove_edge(data_node_id, xor_node_id)
            return

        xor_children = self.get_node_by_id(xor_node_id).get_children_ids()
        for child in xor_children:
            self.remove_edge(xor_node_id, child)
            self.add_edge(new_id, child)

        self.get_node_by_id(new_id).set_parent_ids([xor_node_id])
        self.get_node_by_id(xor_node_id).set_children_ids([new_id])

        self.remove_edge(data_node_id, xor_node_id)

    def apply_neutral_rule(self, neutral_node_id):
        # Neutral rule :
        # Si on devait comparer à de la récursivité, c'est le cas de base
        # Par exemple si on a un | (ou) dont les parents ne sont que des zéros
        # On va les retirer petit à petit, jusqu'à ce qu'il n'y en ait plus,
        # à ce moment là on comprend donc que ce n'étaient que des zéros
        # et donc le OU vaut 0 (faux)
        data = self.get_node_by_id(neutral_node_id).get_label()
        if (data == "|" or data == "^"):
            self.get_node_by_id(neutral_node_id).set_label("0")
        elif (data == "&"):
            self.get_node_by_id(neutral_node_id).set_label("1")

    def reduce_eval(self):
        # Une cofeuille c'est un noeud qui n'a pas de parents, mais des enfants
        cofeuilles = [node for node in self.get_nodes()
                      if (self.indegree(node) == 0 and self.outdegree(node) > 0)]
        # Tant qu'il y a des cofeuilles, c'est qu'on peut réduire
        while (cofeuilles):
            # print(cofeuilles)
            # print(self)
            # print("\n\n\n")
            feuille_id = cofeuilles[0].get_id()
            # Case de base
            if (cofeuilles[0].get_label() not in ["0","1"]):
                self.apply_neutral_rule(feuille_id)
            # Autres cas
            elif len(cofeuilles[0].get_children_ids()) > 0:
                operation_id = cofeuilles[0].get_children_ids()[0]
                operation = self.get_node_by_id(operation_id).get_label()
                if (operation == ""):
                    self.apply_copy_rule(feuille_id, operation_id)
                if (operation == "&"):
                    self.apply_and_rule(feuille_id, operation_id)
                if (operation == "|"):
                    self.apply_or_rule(feuille_id, operation_id)
                if (operation == "^"):
                    self.apply_xor_rule(feuille_id, operation_id)
                if (operation == "~"):
                    self.apply_not_rule(feuille_id, operation_id)

                if (self.indegree(self.get_node_by_id(operation_id)) == 0):
                    cofeuilles.append(self.get_node_by_id(operation_id))

                for node in self.get_nodes():
                    if (self.outdegree(node) == 0):
                        self.remove_node_by_id(node.get_id())

            if (len(cofeuilles[0].get_children_ids()) == 0):
                cofeuilles.pop(0)
        #    time.sleep(5)

    def adder_basic(registre1, registre2, retenue):
        '''
        **TYPE** bool_circ
        registre1 : bool_circ
        registre2 : bool_circ
        retenue : bool_circ
        Fonction qui est le cas initial quand les registres sont egaux a 1
        '''
        if( len(registre1.get_nodes()) != len(registre2.get_nodes()) ):
            print("the two registers don't have the same size")
            return bool_circ.empty()

        if (len(registre1.get_nodes()) == 1):
            # create the bool_circ
            node1 = node(3, "" , []    , [5, 8] )
            node2 = node(4, "" , []    , [5, 8] )
            node3 = node(5, "^", [3, 4], [6]    )
            node4 = node(6, "" , [5]   , [9, 11])
            node5 = node(7, "" , []    , [9, 11])
            node6 = node(8, "&", [3, 4], [10]   )
            node7 = node(9, "&", [6, 7], [10]   )
            node8 = node(10, "|", [8, 9], []    )
            node9 = node(11, "^", [6, 7], []    )
            node_list = [node1, node2, node3,
                         node4, node5, node6,
                         node7, node8, node9]
            graphe_initial = bool_circ(open_digraph([3,4,7], [10,11], node_list))
            registre1.iparallel(registre2)
            registre1.iparallel(retenue)
            registre1.icompose(graphe_initial)
            nodes = registre1.get_id_node_map()
            sorted_list = dict(sorted(nodes.items(), key=lambda item: item[0]))
            registre1.nodes = sorted_list
            registre1.reduce_eval()
            return registre1

        else:
            print("problem")
            return bool_circ(open_digraph.empty())

    def adder(registre1, registre2, retenue):
        '''
        **TYPE** bool_circ
        registre1 : bool_circ
        registre2 : bool_circ
        retenue : bool_circ
        Fonction qui fait recursivement adder et prend le cas
        initial quand len = 1 avec adder_basic
        '''

        # On va chercher à découper le registre en deux parts égales
        full_nodes_1 = registre1.get_nodes()
        full_nodes_2 = registre2.get_nodes()

        # On récupère la première moitié
        first_nodes_1 = full_nodes_1[:(int)(len(full_nodes_1)/2)]
        first_ids_1 = [node.get_id() for node in first_nodes_1]
        first_nodes_2 = full_nodes_2[:(int)(len(full_nodes_2)/2)]
        first_ids_2 = [node.get_id() for node in first_nodes_2]

        # Et la seconde moitié
        scd_nodes_1 = full_nodes_1[(int)(len(full_nodes_1)/2):]
        scd_ids_1 = [node.get_id() for node in scd_nodes_1]
        scd_nodes_2 = full_nodes_2[(int)(len(full_nodes_2)/2):]
        scd_ids_2 = [node.get_id() for node in scd_nodes_2]

        # On crée des sous registres qui ne contiennent que la seconde partie
        second_half1 = bool_circ(open_digraph([], scd_ids_1, scd_nodes_1))
        second_half2 = bool_circ(open_digraph([], scd_ids_2, scd_nodes_2))
        # Et pour la première partie
        first_half1 = bool_circ(open_digraph([], first_ids_1, first_nodes_1))
        first_half2 = bool_circ(open_digraph([], first_ids_2, first_nodes_2))

        if (len(second_half1.get_nodes()) == 1):
            result = bool_circ.adder_basic(second_half1, second_half2, retenue)
        else:
            result = bool_circ.adder(second_half1, second_half2, retenue)

        # On récupère la nouvelle retenue à appliquer
        retenue2 = bool_circ(open_digraph([], [result.get_nodes()[0].get_id()], [result.get_nodes()[0]]))

        if (len(first_half1.get_nodes()) == 1):
            result2 = bool_circ.adder_basic(first_half1, first_half2, retenue2)
        else:
            result2 = bool_circ.adder(first_half1, first_half2, retenue2)

        # On enlève le premier élément de result, car il a été utilisé dans la retenue
        key_list = list(result.get_id_node_map())
        result.get_id_node_map().pop(key_list[0])

        id = result2.max_id()
        r2 = result2.get_nodes()
        r1 = result.get_nodes()

        for node in r1:
            if node.get_id() in result2.get_node_ids():
                id += 1
                while id in result.get_node_ids():
                    id += 1
                node.set_id(id)


        registre = r2 + r1
        ids = [node.get_id() for node in registre]
        return bool_circ(open_digraph([], ids, registre))

    def half_adder(registre1, registre2):
        '''
        **TYPE** bool_circ
        registre1 : bool_circ
        registre2 : bool_circ
        return the register which is the sum of the two registers
        '''
        return bool_circ.adder(registre1, registre2, bool_circ.registre(0, 1))
