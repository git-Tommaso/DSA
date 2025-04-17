from LL import LinkedList  # Import the LinkedList class

# ---------------------MAIN----------------------#

# Create a new Linked List with an initial node (value 0)
my_linked_list = LinkedList(0)

# Add nodes to the list
my_linked_list.append(1)  # Add 1 to the end
my_linked_list.append(2)  # Add 2 to the end
my_linked_list.append(3)  # Add 3 to the end

# Update a node's value and print the list
my_linked_list.set_value(1, 4)  # Change the value at index 1 to 4
my_linked_list.insert(2, 5)  # Insert 5 at index 2
my_linked_list.remove(3)  # Remove the node at index 3
my_linked_list.print_list()  # Print the current list
print()

# Reverse the list and print it
my_linked_list.reverse()  # Reverse the order of the list
my_linked_list.print_list()  # Print the reversed list