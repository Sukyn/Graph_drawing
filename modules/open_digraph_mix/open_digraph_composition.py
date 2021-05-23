class open_digraph_composition:
    # compositions of the graphs

    def shift_indices(self, n):
        '''
        **TYPE** void
        n: int
        change all the node's id by adding n
        '''
        node_ids = self.get_node_ids().copy()

        # if n is positive, we have to begin at the end
        if (n < 0):
            for id in node_ids:
                self.change_id(id, id + n)
        else:
            node_ids.reverse()
            for id in node_ids:
                self.change_id(id, id + n)

        # don't forget the inputs and outputs
        self.set_input_ids([id + n for id in self.get_input_ids()])
        self.set_output_ids([id + n for id in self.get_output_ids()])


    def iparallel(self, g, in_perm=None, out_perm=None):
        '''
        **TYPE** void
        g : graph; the graph to add with
        in_perm : int list; the new input list
        out_perm : int list; the new output list
        combine the two graphs in one by adding the nodes and
        the inputs/outputs from g to self
        '''
        # shift the ids
        shift = self.max_id() - g.min_id() + 1
        g.shift_indices(shift)

        # add the g nodes to self
        for node in g.get_nodes():
            self.get_id_node_map()[node.get_id()] = node
        # make the inputs
        if in_perm is None:
            for inp in g.get_input_ids():
                self.add_input_id(inp)
        else:
            self.set_input_ids(in_perm)
        # make the outputs
        if out_perm is None:
            for outp in g.get_output_ids():
                self.add_output_id(outp)
        else:
            self.set_output_ids(out_perm)

    def parallel(self, g, in_perm=None, out_perm=None):
        '''
        **TYPE** open_digraph
        g : graph; the graph to add with
        in_perm : int list; the new input list
        out_perm : int list; the new output list
        combine the two graphs like iparallel but return
        the new graphs without modify them
        '''
        result = self.copy()
        result.iparallel(g, in_perm, out_perm)
        return result

    def icompose(self, g):
        '''
        **TYPE** void
        g : graph; the graph to compose with
        modify self by adding the nodes from g and merging
        the self outputs with the g inputs
        '''
        # shift the ids
        g.shift_indices(self.max_id() - g.min_id() + 1)
        outputs = self.get_output_ids().copy()

        # test the equality of inputs and outputs
        inputs = g.get_input_ids().copy()
        if not len(inputs) == len(outputs):
            raise ValueError
        else:
            # combine the graphs
            self.iparallel(g)
            # merging the inputs/outputs
            for i in range(len(inputs)):
                self.add_edge(outputs[i], inputs[i])

            # create the fonction of list minus list
            def diff(first, second):
                second = set(second)
                return [item for item in first if item not in second]

            # take the final outputs
            sorted_output_list = diff(self.get_output_ids(), outputs)
            sorted_output_list.sort()
            # take the final inputs
            sorted_input_list = diff(self.get_input_ids(), inputs)
            sorted_input_list.sort()
            # setting the inputs/outputs
            self.set_output_ids(sorted_output_list)
            self.set_input_ids(sorted_input_list)

    def compose(self, g):
        '''
        **TYPE** open_digraph
        g : graph; the graph to compose with
        compose the graphs like icompose but without modify the graphs
        and return the created graph
        '''
        result = self.copy()
        result.icompose(g)
        return result
