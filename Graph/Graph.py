class Graph:
   def __init__(self):
      #create an empty dictionary to store the adjacency list
      self.adj_list = {}

   def print_graph(self):
      #print the adjacency list
      for vertex in self.adj_list:
         print(vertex, ":", self.adj_list[vertex])

   def add_vertex(self, vertex):
      if vertex not in self.adj_list.keys():
         self.adj_list[vertex] = []
         return True
      return False