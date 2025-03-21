from DLL import DoublyLinkedList

my_doubly_linked_list = DoublyLinkedList(1)

my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.prepend(0)

my_doubly_linked_list.pop_first()

print(my_doubly_linked_list.get(0))
print(my_doubly_linked_list.get(1))

print(my_doubly_linked_list.set_value(4,90))
my_doubly_linked_list.print_list()
