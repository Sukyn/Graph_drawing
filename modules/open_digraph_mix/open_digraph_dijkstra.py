class open_digraph_dijkstra:
    # dijkstra algorithm
    # paths (longest and shortest)
    # components
    def connected_components(self):
        '''
        **TYPE** (int, dictionary)
        counts the number of independant graph in self and creates a dictionary
        which assign all nodes ids to the id of the subgraph
        '''
        components = {}
        g = self.copy()
        id_connexe = 0

        while g.get_node_ids():
            # take a node
            nodes_list = [g.min_id()]
            while nodes_list:
                # remove the node with collecting the id
                node_id = nodes_list.pop(0)
                if node_id not in components:
                    # note the id
                    components[node_id] = id_connexe
                    node = g.get_node_by_id(node_id)
                    parents = node.get_parent_ids()
                    children = node.get_children_ids()
                    # remove the id
                    g.remove_node_by_id(node_id)
                    # taking the parents and the children
                    nodes_list += parents + children
            # change connexe
            id_connexe += 1
        return (id_connexe, components)

    ''' TO DO : Permutations (ajouter paramètre) + permutation inverse
    TO DO : Permutations (ajouter paramètre) + permutation inverse
    TO DO : Permutations (ajouter paramètre) + permutation inverse
    TO DO : Permutations (ajouter paramètre) + permutation inverse
    TO DO : Permutations (ajouter paramètre) + permutation inverse
    TO DO : Permutations (ajouter paramètre) + permutation inverse
    TO DO : Permutations (ajouter paramètre) + permutation inverse
    '''
    def graph_permutation(self):
        '''
        **TYPE** (open_digraph list, int list, int list)
        return the list of the component graphs,
        the inputs list and the ouputs list
        '''
        nb, compo_id = self.connected_components()
        components = []
        # for all the components
        for i in range(nb):
            # take the nodes
            node_ids = [key for (key, value) in compo_id.items() if value == i]
            nodes = self.get_nodes_by_ids(node_ids)
            # take the inputs
            inputs = [inp for inp in self.get_input_ids()
                      if inp in node_ids]
            # take the outputs
            outputs = [outp for outp in self.get_output_ids()
                       if outp in node_ids]
            # add the component to the graph list
            components.append(self.__class__(inputs, outputs, nodes))
        return (components, self.get_input_ids(), self.get_output_ids())

    def dijkstra(self, src, direction=None, tgt=None):
        '''
        **TYPE** (dictionary, dictionary)
        src : int; the id of the node source
        direction : 1 or -1;    - 1 -> take the parents
                                - -1 -> take the children
                                - None -> take both
        tgt : int; the id of the node target
        the dijkstra algorithm
        '''
        queue = [src]
        dist = {src: 0}
        prev = {}

        while queue:

            u = min(queue, key=lambda x: dist[x])
            queue.remove(u)
            node_u = self.get_node_by_id(u)
            children_u = self.get_nodes_by_ids(node_u.get_children_ids())
            parents_u = self.get_nodes_by_ids(node_u.get_parent_ids())
            if (direction == 1):
                neighbours = parents_u
            elif (direction == -1):
                neighbours = children_u
            else:
                neighbours = parents_u + children_u

            for neighbour in neighbours:
                if neighbour.get_id() not in dist:
                    queue.append(neighbour.get_id())
                if (neighbour.get_id() not in dist or
                        dist[neighbour.get_id()] > dist[u] + 1):
                    dist[neighbour.get_id()] = dist[u] + 1
                    prev[neighbour.get_id()] = u
                if neighbour.get_id() == tgt:
                    return (dist[neighbour.get_id()], prev)
        return (dist, prev)

    def shortest_path(self, nodeA, nodeB):
        '''
        **TYPE** int list
        nodeA : node
        nodeB : node
        return the shortest path to go from nodeA to nodeB by
        creating the id list of the nodes
        '''
        # test if nodeB is in graph
        if nodeB not in self.get_nodes():
            print("nodeB not in the graph")
            return None

        distance, previous = self.dijkstra(nodeA.get_id(), tgt=nodeB.get_id())
        path = [nodeB.get_id()]
        node = nodeB.get_id()
        # create the path
        while node != nodeA.get_id():
            node = previous[node]
            path.insert(0, node)
        return path

    def longest_path(self, u, v):
        '''
        **TYPE** (int list, int)
        u : node
        v : node
        return the longest path of node ids and the length of the path
        '''
        dist = {u.get_id(): 0}
        prev = {}

        if self.is_cyclic():
            raise ValueError("The graph isn't acyclic")
        else:
            sorted_list = self.topological_sorting()
            depth = self.node_depth(u)

            # For depths of more than k
            for i in range(depth, len(sorted_list)):

                for w in sorted_list[i]:
                    for parent in self.get_node_by_id(w).get_parent_ids():
                        # If one of the parents of
                        # node w is in the dist dictionary

                        if parent in dist:
                            # We take the parent of dist maximum
                            parent_max = max(dist, key=lambda x: dist[x])
                            # We give the value of parent_max to dist[w]
                            dist[w] = dist[parent] + 1
                            # We save the parent_max node in prev[w]
                            prev[w] = parent_max

        path = [v.get_id()]
        node = v.get_id()
        while node != u.get_id():
            node = prev[node]
            path.insert(0, node)
        return path, len(path)

    def every_parents(self, node):
        '''
        **TYPE** int list
        node : node
        return the parents id list
        '''
        result = node.get_parent_ids().copy()
        # take the parents
        for parent in result:
            # recursivity
            value = self.every_parents(self.get_node_by_id(parent))
            # add the parents to the result
            if value not in result:
                result += value
        return result

    def parents_distance(self, nodeA, nodeB):
        '''
        **TYPE** dictionary
        nodeA : node
        nodeB : node
        return the common parents with their distance
        to nodeA and nodeB by tuple
        '''
        result = {}
        for nodeA_parent in self.every_parents(nodeA):
            for nodeB_parent in self.every_parents(nodeB):
                if nodeA_parent == nodeB_parent:
                    # distance calculation
                    distA = self.dijkstra(nodeA.get_id(), tgt=nodeA_parent)[0]
                    distB = self.dijkstra(nodeB.get_id(), tgt=nodeB_parent)[0]
                    # add to the dictionary
                    result[nodeA_parent] = (distA, distB)
        return result
