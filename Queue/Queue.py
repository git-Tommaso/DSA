from Node import Node  # Import the Node class to create queue nodes

class Queue:
    """
    Implements a Queue data structure using a linked list.
    A Queue follows the First-In-First-Out (FIFO) principle where:
    - Elements are added (enqueued) at the rear (last)
    - Elements are removed (dequeued) from the front (first)
    """
    
    def __init__(self, value):
        """
        Initializes the Queue with a single node.
        Args:
            value: The value to be stored in the first node
        """
        # Create a new node with the given value
        new_node = Node(value)
        # Set both first and last to the new node since it's the only node
        self.first = new_node
        self.last = new_node
        # Initialize the length of the queue to 1
        self.length = 1

    def print_queue(self):
        """
        Prints all the values in the queue from first to last.
        Time Complexity: O(n) where n is the number of nodes
        """
        # Start from the first node
        temp = self.first
        # Traverse the queue and print each node's value
        while temp:
            print(temp.value)
            temp = temp.next

    def Enqueue(self, value):
        """
        Adds a new node with the given value to the end of the queue.
        Args:
            value: The value to be added
        Time Complexity: O(1)
        """
        # Create a new node with the given value
        new_node = Node(value)
        # If the queue is empty, set both first and last to the new node
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            # Link the current last node to the new node
            self.last.next = new_node
            # Update the last node to the new node
            self.last = new_node
        # Increment the length of the queue
        self.length += 1

    def Dequeue(self):
        """
        Removes and returns the first node from the queue.
        Returns:
            Node: The removed node, or None if the queue is empty
        Time Complexity: O(1)
        """
        # If the queue is empty, return None
        if self.length == 0:
            return None
        # Store the current first node
        temp = self.first
        # If the queue has only one node, reset first and last to None
        if self.length == 1:
            self.last = None
            self.first = None
        else:
            # Update the first node to the next node
            self.first = self.first.next
            # Disconnect the removed node from the queue
            temp.next = None
        # Decrement the length of the queue
        self.length -= 1
        return temp