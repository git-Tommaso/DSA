from Graph import Graph  # Import the Graph class

# Create a new graph
my_graph = Graph()

# Add vertices to the graph
my_graph.add_vertex('A')  # Add vertex A
my_graph.add_vertex('B')  # Add vertex B
my_graph.add_vertex('C')  # Add vertex C
my_graph.add_vertex('D')  # Add vertex D

# Add edges between vertices
my_graph.add_edge('A', 'B')  # Connect A and B
my_graph.add_edge('A', 'C')  # Connect A and C
my_graph.add_edge('A', 'D')  # Connect A and D
my_graph.add_edge('B', 'D')  # Connect B and D
my_graph.add_edge('C', 'D')  # Connect C and D

# Remove a vertex and its edges
my_graph.remove_vertex('D')  # Remove vertex D and its connections

# Print the graph
my_graph.print_graph()  # Output the adjacency list