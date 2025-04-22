"""
Graph Operations Demonstration
This file demonstrates how to create and manipulate a graph using the Graph class.
It shows basic operations like adding vertices, adding edges, and removing vertices.
"""

from Graph import Graph  # Import the Graph class implementation

# Create a new empty graph
my_graph = Graph()

# Add vertices to the graph
# Each vertex is added individually
my_graph.add_vertex('A')  # Add vertex A to the graph
my_graph.add_vertex('B')  # Add vertex B to the graph
my_graph.add_vertex('C')  # Add vertex C to the graph
my_graph.add_vertex('D')  # Add vertex D to the graph

# Add edges between vertices
# Each edge connects two vertices and is bidirectional (undirected graph)
my_graph.add_edge('A', 'B')  # Create edge between A and B
my_graph.add_edge('A', 'C')  # Create edge between A and C
my_graph.add_edge('A', 'D')  # Create edge between A and D
my_graph.add_edge('B', 'D')  # Create edge between B and D
my_graph.add_edge('C', 'D')  # Create edge between C and D

"""
Current Graph Structure:
    A
   /|\
  B C D
   \|/
    D
"""

# Remove a vertex and all its edges
# This will remove vertex D and all edges connected to it
my_graph.remove_vertex('D')  # Remove vertex D and its connections

"""
Graph Structure after removing D:
    A
   / \
  B   C
"""

# Print the graph's adjacency list representation
# This will show the current state of the graph
my_graph.print_graph()  # Output the adjacency list

"""
Expected Output:
A : ['B', 'C']
B : ['A']
C : ['A']
"""