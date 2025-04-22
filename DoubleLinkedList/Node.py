class Node:
    """
    Represents a single node in a Doubly Linked List.
    Each node contains a value, a reference to the next node, and a reference to the previous node.
    This bidirectional linking allows for traversal in both directions.
    """
    def __init__(self, value):
        # The value/data stored in this node
        self.value = value
        # Pointer to the next node in the list (None if this is the last node)
        self.next = None
        # Pointer to the previous node in the list (None if this is the first node)
        self.prev = None