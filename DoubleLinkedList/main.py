from DLL import DoublyLinkedList

# Create a new Doubly Linked List with an initial node containing value 1
# This initializes the list with one node, setting both head and tail to this node
my_doubly_linked_list = DoublyLinkedList(1)

# Add nodes to the list using different methods
my_doubly_linked_list.append(2)  # Add node with value 2 to the end of the list
my_doubly_linked_list.append(3)  # Add node with value 3 to the end of the list
my_doubly_linked_list.prepend(0)  # Add node with value 0 to the beginning of the list

# Remove the first node from the list using pop_first()
# This operation returns the removed node and updates the head pointer
my_doubly_linked_list.pop_first()

# Access and print nodes at specific indices
# The get() method returns the node at the specified index
print(my_doubly_linked_list.get(0))  # Get and print the node at index 0 (first node)
print(my_doubly_linked_list.get(1))  # Get and print the node at index 1 (second node)

# Attempt to set a value at an invalid index
# This should return False since index 4 is out of bounds
print(my_doubly_linked_list.set_value(4, 90))  # Try to set value 90 at index 4

# Print the entire list from head to tail
# This demonstrates the current state of the list after all operations
my_doubly_linked_list.print_list()
