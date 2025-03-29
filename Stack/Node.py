class Node:
    """
    A class representing a single node in a linked list.
    Each node contains a value and a pointer to the next node.
    """
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.next = None  # Pointer to the next node (initially None)