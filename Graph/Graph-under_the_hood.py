"""
Graph Data Structure - Under the Hood
This file demonstrates two common ways to represent graphs:
1. Adjacency List: Using dictionaries to store connections
2. Adjacency Matrix: Using 2D arrays to represent connections
"""

# Adjacency List Representation
# This is a more space-efficient way to represent sparse graphs
# Each vertex (key) stores a list of its connected vertices (values)
vertex = {
      'A': ['B', 'C'],  # Vertex A has edges to B and C
      'B': ['A', 'C'],  # Vertex B has edges to A and C
      'C': ['A', 'B', 'D'],  # Vertex C has edges to A, B, and D
      'D': ['C']  # Vertex D has an edge only to C
}

"""
Adjacency List Properties:
- Space Complexity: O(V + E) where V is vertices and E is edges
- Time to check if two vertices are connected: O(V)
- Good for sparse graphs (few edges)
- Easy to add/remove vertices
"""

# Adjacency Matrix Representation
# This is a more time-efficient way to represent dense graphs
# Rows and columns represent vertices, values represent edges
matrix = [
      # A  B  C  D  # Column headers for clarity
      [0, 1, 1, 0],  # Row A: connections to A,B,C,D
      [1, 0, 1, 0],  # Row B: connections to A,B,C,D
      [1, 1, 0, 1],  # Row C: connections to A,B,C,D
      [0, 0, 1, 0]   # Row D: connections to A,B,C,D
]

"""
Adjacency Matrix Properties:
- Space Complexity: O(V²) where V is number of vertices
- Time to check if two vertices are connected: O(1)
- Good for dense graphs (many edges)
- Easy to check for edge existence
- Can represent weighted edges by using numbers instead of 0/1

Note: In this example:
- 1 indicates an edge between vertices
- 0 indicates no edge
- The matrix is symmetric because this is an undirected graph
"""
