class Node:
    """
    Node class for Binary Search Tree (BST)
    
    Each node in a BST contains:
    - A value (the data stored in the node)
    - A reference to its left child (smaller values)
    - A reference to its right child (larger values)
    
    This class represents a single node in the BST data structure.
    """
    
    # This is the constructor method. It is called automatically
    # when a new instance of the Node class is created.
    def __init__(self, value):
        """
        Initialize a new Node with the given value
        
        Args:
            value: The data to be stored in this node
            
        Time Complexity: O(1)
        """
        # The value/data stored in this node
        self.value = value
        
        # Reference to the left child node (contains values less than this node's value)
        self.left = None
        
        # Reference to the right child node (contains values greater than this node's value)
        self.right = None