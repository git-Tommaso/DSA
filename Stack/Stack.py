from Node import Node  # Import the Node class to create stack nodes

class Stack:
    """
    Implements a Stack data structure using a linked list.
    A Stack follows the Last-In-First-Out (LIFO) principle where:
    - Elements are added (pushed) to the top
    - Elements are removed (popped) from the top
    """
    
    def __init__(self, value):
        """
        Initializes the Stack with a single node.
        Args:
            value: The value to be stored in the first node
        """
        # Create a new node with the given value
        new_node = Node(value)
        # Set the top of the stack to the new node
        self.top = new_node
        # Initialize the height of the stack to 1
        self.height = 1

    def print_stack(self):
        """
        Prints all the values in the stack from top to bottom.
        Time Complexity: O(n) where n is the number of nodes
        """
        # Start from the top of the stack
        temp = self.top
        # Traverse the stack and print each node's value
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        """
        Adds a new node with the given value to the top of the stack.
        Args:
            value: The value to be added
        Time Complexity: O(1)
        """
        # Create a new node with the given value
        new_node = Node(value)
        # If the stack is empty, set the new node as the top
        if self.height == 0:
            self.top = new_node
        else:
            # Link the new node to the current top
            new_node.next = self.top
            # Update the top to the new node
            self.top = new_node
        # Increment the height of the stack
        self.height += 1

    def pop(self):
        """
        Removes and returns the top node from the stack.
        Returns:
            Node: The removed node, or None if the stack is empty
        Time Complexity: O(1)
        """
        # If the stack is empty, return None
        if self.height == 0:
            return None
        # Store the current top node
        temp = self.top
        # Update the top to the next node
        self.top = self.top.next
        # Disconnect the removed node from the stack
        temp.next = None
        # Decrement the height of the stack
        self.height -= 1
        return temp