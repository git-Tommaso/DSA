class Graph:
    """
    Graph Class Implementation using Adjacency List
    This class implements an undirected graph using an adjacency list representation.
    Each vertex is stored as a key in a dictionary, and its connected vertices are stored as values.
    """
    
    def __init__(self):
        """
        Initialize an empty graph
        Time Complexity: O(1)
        """
        # Dictionary to store the adjacency list
        # Key: vertex
        # Value: list of connected vertices
        self.adj_list = {}

    def print_graph(self):
        """
        Print the graph's adjacency list representation
        Time Complexity: O(V + E) where V is vertices and E is edges
        """
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        """
        Add a new vertex to the graph
        
        Args:
            vertex: The vertex to be added
            
        Returns:
            bool: True if vertex was added, False if it already exists
            
        Time Complexity: O(1)
        """
        if vertex not in self.adj_list.keys():
            # Initialize an empty list to store connected vertices
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        """
        Add an undirected edge between two vertices
        
        Args:
            v1: First vertex
            v2: Second vertex
            
        Returns:
            bool: True if edge was added, False if vertices don't exist
            
        Time Complexity: O(1)
        """
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            # Add v2 to v1's adjacency list
            self.adj_list[v1].append(v2)
            # Add v1 to v2's adjacency list (undirected graph)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        """
        Remove an edge between two vertices
        
        Args:
            v1: First vertex
            v2: Second vertex
            
        Returns:
            bool: True if edge was removed, False if vertices don't exist
            
        Time Complexity: O(V) where V is the number of vertices in the adjacency list
        """
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                # Remove v2 from v1's adjacency list
                self.adj_list[v1].remove(v2)
                # Remove v1 from v2's adjacency list
                self.adj_list[v2].remove(v1)
            except ValueError:
                # Edge doesn't exist, ignore the error
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        """
        Remove a vertex and all its edges from the graph
        
        Args:
            vertex: The vertex to be removed
            
        Returns:
            bool: True if vertex was removed, False if it doesn't exist
            
        Time Complexity: O(V + E) where V is vertices and E is edges
        """
        if vertex in self.adj_list.keys():
            # Remove the vertex from all adjacent vertices' lists
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            # Delete the vertex from the graph
            del self.adj_list[vertex]
            return True
        return False