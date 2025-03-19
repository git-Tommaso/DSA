from LL import LinkedList

# ---------------------MAIN----------------------#

# Test the linked list
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

# Update a value and print the list
my_linked_list.set_value(1, 4)
my_linked_list.instert(2,5)
my_linked_list.remove(3)
my_linked_list.print_list()
print()
my_linked_list.reverse()
my_linked_list.print_list()

# Uncomment the following sections to test other methods:

# Test the pop method
# print(my_linked_list.pop())  # (2) Items - Returns 2 Node
# print(my_linked_list.pop())  # (1) Items - Returns 1 Node
# print(my_linked_list.pop())  # (0) Items - Returns None

# Test the pop_first method
# print(my_linked_list.pop_first())  # (2) Items - Returns 2 Node
# print(my_linked_list.pop_first())  # (1) Items - Returns 1 Node
# print(my_linked_list.pop_first())  # (0) Items - Returns None