class Node:
    # This is the constructor method. It is called automatically
    # when a new instance of the Node class is created.
    def __init__(self, value):
        # Assign the given value to the Node's 'value' property.
        self.value = value
        
        # Initialize the 'left' child of the Node to None.
        # This means the node does not have a left child yet.
        self.left = None
        
        # Initialize the 'right' child of the Node to None.
        # This means the node does not have a right child yet.
        self.right = None