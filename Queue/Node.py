class Node:
    """
    Represents a single node in a Queue.
    Each node contains a value and a reference to the next node in the queue.
    This is the basic building block for the linked list implementation of a queue.
    """
    def __init__(self, value):
        # The value/data stored in this node
        self.value = value
        # Pointer to the next node in the queue (None if this is the last node)
        self.next = None