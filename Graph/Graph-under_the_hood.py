# Adjacency list representation of a graph
vertex = {
      'A': ['B', 'C'],  # Vertex A is connected to B and C
      'B': ['A', 'C'],  # Vertex B is connected to A and C
      'C': ['A', 'B', 'D'],  # Vertex C is connected to A, B, and D
      'D': ['C']  # Vertex D is connected to C
}

# Adjacency matrix representation of the same graph
matrix = [
      # A  B  C  D
      [0, 1, 1, 0],  # Row for vertex A
      [1, 0, 1, 0],  # Row for vertex B
      [1, 1, 0, 1],  # Row for vertex C
      [0, 0, 1, 0]   # Row for vertex D
]
# Adjacency matrix is a 2D array where rows and columns represent vertices
# 1 indicates an edge between vertices, 0 indicates no edge
