class Graph:
   def __init__(self):
      # Create an empty dictionary to store the adjacency list
      self.adj_list = {}

   def print_graph(self):
      # Print the adjacency list
      for vertex in self.adj_list:
         print(vertex, ":", self.adj_list[vertex])

   def add_vertex(self, vertex):
      # Add a vertex to the graph if it doesn't already exist
      if vertex not in self.adj_list.keys():
         self.adj_list[vertex] = []  # Initialize an empty list for the vertex
         return True
      return False

   def add_edge(self, v1, v2):
      # Add an edge between two vertices if both exist in the graph
      if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
         self.adj_list[v1].append(v2)  # Add v2 to v1's adjacency list
         self.adj_list[v2].append(v1)  # Add v1 to v2's adjacency list
         return True
      return False

   def remove_edge(self, v1, v2):
      # Remove an edge between two vertices if both exist in the graph
      if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
         try:
            self.adj_list[v1].remove(v2)  # Remove v2 from v1's adjacency list
            self.adj_list[v2].remove(v1)  # Remove v1 from v2's adjacency list
         except ValueError:
            pass  # Ignore if the edge doesn't exist
         return True
      return False

   def remove_vertex(self, vertex):
      # Remove a vertex and all its edges from the graph
      if vertex in self.adj_list.keys():
         for other_vertex in self.adj_list[vertex]:  # Iterate through adjacent vertices
            self.adj_list[other_vertex].remove(vertex)  # Remove the vertex from their lists
         del self.adj_list[vertex]  # Delete the vertex from the graph
         return True
      return False