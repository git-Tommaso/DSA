class Node:
    """
    A class representing a single node in a linked list.
    Each node contains a value and a pointer to the next node.
    This is the basic building block for the linked list implementation of a stack.
    """
    def __init__(self, value):
        # The value/data stored in this node
        self.value = value
        # Pointer to the next node in the stack (None if this is the top node)
        self.next = None