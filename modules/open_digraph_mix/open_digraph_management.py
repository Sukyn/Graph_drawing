class open_digraph_management:
    # nodes    managements
    # children managements
    # parents  managements
    def add_edge(self, src, tgt):
        '''
        **TYPE** void
        src: int; id of the source node
        tgt: int; id of the target node
        function to add edge
        '''
        self.get_node_by_id(src).add_child_id(tgt)
        self.get_node_by_id(tgt).add_parent_id(src)

    def add_edges(self, src_list, tgt_list):
        '''
        **TYPE** void
        src_list: int list; ids of the source nodes
        tgt_list: int list; ids of the target nodes
        fonction to add edges
        '''
        for src, tgt in zip(src_list, tgt_list):
            self.add_edge(src, tgt)

    def remove_edge(self, src, tgt):
        '''
        **TYPE** void
        src: int; id of the source node
        tgt : int; id of the target node
        function to remove edge
        '''
        self.get_node_by_id(src).children.remove(tgt)
        self.get_node_by_id(tgt).parents.remove(src)

    def remove_node_by_id(self, id):
        '''
        **TYPE** void
        id: int; id of the node to remove
        remove the node with the id
        '''
        node = self.get_node_by_id(id)
        for parent in node.get_parent_ids():
            parent_node = self.get_node_by_id(parent)
            parent_node.remove_child_id_all(id)
        for child in node.get_children_ids():
            child_node = self.get_node_by_id(child)
            child_node.remove_parent_id_all(id)
        self.nodes.pop(id)

    def remove_edges(self, src_list, tgt_list):
        '''
        **TYPE** void
        src_list: int list; ids of the source nodes
        tgt_list: int list; ids of the target nodes
        fonction to remove edges
        '''
        for src, tgt in zip(src_list, tgt_list):
            try:
                while(True):
                    self.remove_edge(src, tgt)
            except ValueError:
                pass

    def remove_nodes_by_id(self, id_list):
        '''
        **TYPE** void
        id_list: int list; list of the nodes' ids
        remove the nodes with the ids
        '''
        for id in id_list:
            try:
                self.remove_node_by_id(id)
            except KeyError:
                pass

    def node_fusion(self, first_id, second_id, label=None):
        '''
        **TYPE** void
        first_id : int
        second_id : int
        label : string
        Function that fusion two nodes and call it label
        '''
        # We check if the nodes are in the graph
        node_ids = self.get_node_ids()
        # If not, we print an error
        # (n.b : we could just say "okay let's do nothing")
        if first_id not in node_ids or second_id not in node_ids:
            print("Il existe pas")

        # Getting nodes
        first_node = self.get_node_by_id(first_id)  # The one saved
        second_node = self.get_node_by_id(second_id)  # The one killed

        # Fusion of inputs & outputs
        for id in second_node.get_input_ids():
            first_node.add_input_id(id)
        for id in second_node.get_output_ids():
            first_node.add_output_id(id)
        # Fusion of parents & children
        for child_id in second_node.get_children_ids():
            first_node.add_child_id(child_id)
        for parent_id in second_node.get_children_ids():
            first_node.add_child_id(parent_id)

        # The user can set his own label to the fusion
        if label:
            first_node.set_label(label)

        # GO TO HELL WE DON'T NEED YOU ANYMORE (remove the node)
        self.remove_node_by_id(second_id)

    def change_id(self, node_id, new_id):
        '''
        **TYPE** void
        new_id: int; new id of the node
        node_id: int; actual id of the node
        change node_id by new_id
        '''
        if (new_id not in self.get_node_ids()):
            node_map = self.get_id_node_map()
            node = node_map.pop(node_id)
            # Our node map should have the node with another id
            node_map[new_id] = node
            # We change the id
            node.set_id(new_id)

            for child in node.get_children_ids():
                self.get_node_by_id(child).remove_parent_id(node_id)
                self.get_node_by_id(child).add_parent_id(new_id)

            for parent in node.get_parent_ids():
                self.get_node_by_id(parent).remove_child_id(node_id)
                self.get_node_by_id(parent).add_child_id(new_id)

    def change_ids(self, node_ids, new_ids):
        '''
        **TYPE** void
        new_ids: int list; new ids of the nodes
        node_ids: int list; actual ids of the nodes
        change all of the node_ids by new_ids
        '''
        list = sorted(zip(node_ids, new_ids), key=lambda x: x[0])
        for i in range(len(list)):
            self.change_id(list[i][0], list[i][1])
