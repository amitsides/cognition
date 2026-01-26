class DAG:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node_id, node_data):
        if node_id not in self.nodes:
            self.nodes[node_id] = node_data
            self.edges[node_id] = []
        else:
            raise ValueError(f"Node {node_id} already exists.")

    def add_edge(self, from_node, to_node):
        if from_node in self.nodes and to_node in self.nodes:
            self.edges[from_node].append(to_node)
        else:
            raise ValueError("One or both nodes not found in the DAG.")

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def topological_sort_util(self, node, visited, stack):
        visited.add(node)
        for neighbor in self.edges[node]:
            if neighbor not in visited:
                self.topological_sort_util(neighbor, visited, stack)
        stack.append(node)

    def topological_sort(self):
        visited = set()
        stack = []
        for node in self.nodes:
            if node not in visited:
                self.topological_sort_util(node, visited, stack)
        return stack[::-1]  # Return reversed stack for correct order

    def __repr__(self):
        return f"DAG(nodes={self.nodes}, edges={self.edges})"