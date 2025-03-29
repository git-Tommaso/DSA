class Node:
    """
    Represents a single node in a Doubly Linked List.
    Each node contains a value, a reference to the next node, and a reference to the previous node.
    """
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.next = None  # Pointer to the next node (initially None)
        self.prev = None  # Pointer to the previous node (initially None)