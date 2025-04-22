class Node:
    """
    Represents a single node in a Linked List.
    Each node contains a value and a reference to the next node.
    
    Attributes:
        value: The data stored in the node
        next: Reference to the next node in the list (None if this is the last node)
        
    Time Complexity:
        - Initialization: O(1)
    Space Complexity:
        - O(1) for each node
    """
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.next = None  # Pointer to the next node (initially None)