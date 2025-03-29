#adjactency list
vertex = {
      'A': ['B', 'C'],
      'B': ['A', 'C'],
      'C': ['A', 'B', 'D'],
      'D': ['C']
}

#adjacency matrix
matrix = [
      #A  B  C  D
      [0, 1, 1, 0],
      [1, 0, 1, 0],
      [1, 1, 0, 1],
      [0, 0, 1, 0]
]
#adjacency matrix is a 2D array where the rows and columns represent the vertices of the graph
#1 if there is an edge between the vertices, 0 if there is not
