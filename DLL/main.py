from DLL import DoublyLinkedList

# Create a new Doubly Linked List with an initial node (value 1)
my_doubly_linked_list = DoublyLinkedList(1)

# Add nodes to the list
my_doubly_linked_list.append(2)  # Add 2 to the end
my_doubly_linked_list.append(3)  # Add 3 to the end
my_doubly_linked_list.prepend(0)  # Add 0 to the beginning

# Remove the first node
my_doubly_linked_list.pop_first()

# Access and print values at specific indices
print(my_doubly_linked_list.get(0))  # Get the value at index 0
print(my_doubly_linked_list.get(1))  # Get the value at index 1

# Attempt to set a value at an invalid index and print the result
print(my_doubly_linked_list.set_value(4, 90))  # Should return False

# Print the entire list
my_doubly_linked_list.print_list()
