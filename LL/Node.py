class Node:
    """
    Represents a single node in a Linked List.
    Each node contains a value and a reference to the next node.
    """
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.next = None  # Pointer to the next node (initially None)