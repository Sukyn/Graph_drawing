class open_digraph_getters_setters:
    # ----- GETTERS -----
    # functions to get the attributes of the object
    # (encapsulation)
    def get_input_ids(self):
        return self.inputs

    def get_output_ids(self):
        return self.outputs

    def get_id_node_map(self):
        return self.nodes

    def get_nodes(self):
        return list(self.nodes.values())

    def get_node_ids(self):
        return sorted([i for i in self.nodes])

    def get_node_by_id(self, id):
        return self.nodes[id]

    def get_nodes_by_ids(self, idlist):
        return [self.nodes[i] for i in idlist]

    def get_length(self):
        return len(self.nodes)

    def multi_getter(self, id, args):
        '''
        This functions is a shortcut if you want to
        find either parents, children or both
        '''
        result = []
        if "parents" in args:
            result += self.get_nodes_by_ids(
                      (self.get_node_by_id(id)).get_parent_ids()
                      )
        if "children" in args:
            result += self.get_nodes_by_ids(
                      (self.get_node_by_id(id)).get_children_ids()
                      )
        return result

    def max_indegree(self):
        '''
        **TYPE** int
        returns the maximum indegree of the graph,
        i.e. the maximum of each node's indegree
        '''
        return max([self.indegree(node) for node in self.get_nodes()])

    def min_indegree(self):
        '''
        **TYPE** int
        returns the minimum indegree of the graph,
        i.e. the minimum of each node's indegree
        '''
        return min([self.indegree(node) for node in self.get_nodes()])

    def max_outdegree(self):
        '''
        **TYPE** int
        returns the maximum outdegree of the graph,
        i.e. the maximum of each node's outdegree
        '''
        return max([self.outdegree(node) for node in self.get_nodes()])

    def min_outdegree(self):
        '''
        **TYPE** int
        returns the minimum indegree of the graph,
        i.e. the minimum of each node's outdegree
        '''
        return min([self.outdegree(node) for node in self.get_nodes()])

    def min_id(self):
        '''
        **TYPE** int
        returns the min of all nodes id
        '''
        return min(self.get_node_ids())

    def max_id(self):
        '''
        **TYPE** int
        returns the max of all nodes id
        '''
        return max(self.get_node_ids())

    # ----- SETTERS -----
    # functions to modify the attributes of the object
    # (encapsulation)
    def set_input_ids(self, new_idlist):
        self.inputs = new_idlist

    def set_output_ids(self, new_idlist):
        self.outputs = new_idlist

    def add_input_id(self, new_id):
        self.inputs.append(new_id)

    def add_output_id(self, new_id):
        self.outputs.append(new_id)

    def del_input_id(self, old_id):
        self.inputs.remove(old_id)

    def del_output_id(self, old_id):
        self.outputs.remove(old_id)
