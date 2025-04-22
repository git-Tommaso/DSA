from Node import Node  # Import the Node class to create doubly linked list nodes

class DoublyLinkedList:
    """
    Implements a Doubly Linked List data structure.
    A doubly linked list is a linear data structure where each element (node) contains:
    - A value
    - A pointer to the next node
    - A pointer to the previous node
    This allows for efficient traversal in both directions.
    """

    def __init__(self, value):
        """
        Initializes the Doubly Linked List with a single node.
        Args:
            value: The value to be stored in the first node
        """
        # Create a new node with the given value
        new_node = Node(value)
        # Set both head and tail to the new node since it's the only node
        self.head = new_node
        self.tail = new_node
        # Initialize the length of the list to 1
        self.length = 1

    def print_list(self):
        """
        Prints all the values in the Doubly Linked List from head to tail.
        Time Complexity: O(n) where n is the number of nodes
        """
        # Start from the head of the list
        temp = self.head
        # Traverse the list and print each node's value
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Adds a new node with the given value to the end of the list.
        Args:
            value: The value to be added
        Returns:
            bool: True if the operation was successful
        Time Complexity: O(1)
        """
        # Create a new node with the given value
        new_node = Node(value)
        # If the list is empty, set both head and tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Link the current tail to the new node
            self.tail.next = new_node
            # Link the new node back to the current tail
            new_node.prev = self.tail
            # Update the tail to the new node
            self.tail = new_node
        # Increment the length of the list
        self.length += 1
        return True

    def pop(self):
        """
        Removes and returns the last node from the list.
        Returns:
            Node: The removed node, or None if the list is empty
        Time Complexity: O(1)
        """
        # If the list is empty, return None
        if self.length == 0:
            return None
        # Store the current tail in a temporary variable
        temp = self.tail
        # If the list has only one node, reset head and tail to None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # Update the tail to the previous node
            self.tail = temp.prev
            # Remove the link from the new tail to the removed node
            self.tail.next = None
            # Remove the link from the removed node to the new tail
            temp.prev = None
        # Decrement the length of the list
        self.length -= 1
        return temp

    def prepend(self, value):
        """
        Adds a new node with the given value to the beginning of the list.
        Args:
            value: The value to be added
        Returns:
            bool: True if the operation was successful
        Time Complexity: O(1)
        """
        # Create a new node with the given value
        new_node = Node(value)
        # If the list is empty, set both head and tail to the new node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node to the current head
            new_node.next = self.head
            # Link the current head back to the new node
            self.head.prev = new_node
            # Update the head to the new node
            self.head = new_node
        # Increment the length of the list
        self.length += 1
        return True

    def pop_first(self):
        """
        Removes and returns the first node from the list.
        Returns:
            Node: The removed node, or None if the list is empty
        Time Complexity: O(1)
        """
        # If the list is empty, return None
        if self.length == 0:
            return None
        # Store the current head in a temporary variable
        temp = self.head
        # If the list has only one node, reset head and tail to None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # Update the head to the next node
            self.head = self.head.next
            # Remove the link from the new head to the removed node
            self.head.prev = None
            # Remove the link from the removed node to the new head
            temp.next = None
        # Decrement the length of the list
        self.length -= 1
        return temp

    def get(self, index):
        """
        Returns the node at the specified index.
        Args:
            index: The position of the node to retrieve (0-based)
        Returns:
            Node: The node at the specified index, or None if index is out of bounds
        Time Complexity: O(n), but optimized to O(n/2) by choosing the closer end
        """
        # Return None if the index is out of bounds
        if index < 0 or index >= self.length:
            return None
        # Decide whether to traverse from the head or tail based on index position
        temp = self.head
        if index < self.length / 2:
            # Traverse from the head for indices in the first half
            for _ in range(index):
                temp = temp.next
        else:
            # Traverse from the tail for indices in the second half
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        """
        Updates the value of the node at the specified index.
        Args:
            index: The position of the node to update (0-based)
            value: The new value to set
        Returns:
            bool: True if the update was successful, False otherwise
        Time Complexity: O(n)
        """
        # Get the node at the specified index
        temp = self.get(index)
        # If the node exists, update its value
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """
        Inserts a new node with the given value at the specified index.
        Args:
            index: The position where the new node should be inserted (0-based)
            value: The value to be inserted
        Returns:
            bool: True if the insertion was successful, False otherwise
        Time Complexity: O(n)
        """
        # Return False if the index is out of bounds
        if index < 0 or index > self.length:
            return False
        # If inserting at the beginning, use prepend
        if index == 0:
            return self.prepend(value)
        # If inserting at the end, use append
        if index == self.length:
            return self.append(value)

        # Create a new node with the given value
        new_node = Node(value)
        # Get the nodes before and after the insertion point
        before = self.get(index - 1)
        after = before.next

        # Link the new node with its neighbors
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        # Increment the length of the list
        self.length += 1
        return True

    def remove(self, index):
        """
        Removes the node at the specified index and returns it.
        Args:
            index: The position of the node to remove (0-based)
        Returns:
            Node: The removed node, or None if the index is out of bounds
        Time Complexity: O(n)
        """
        # Check if the index is out of bounds
        if index < 0 or index >= self.length:
            return None
        # If removing the first node, use pop_first
        if index == 0:
            return self.pop_first()
        # If removing the last node, use pop
        if index == self.length - 1:
            return self.pop()

        # Get the node to be removed
        temp = self.get(index)
        # Update the next node's previous pointer
        temp.next.prev = temp.prev
        # Update the previous node's next pointer
        temp.prev.next = temp.next
        # Disconnect the removed node's pointers
        temp.next = None
        temp.prev = None
        # Decrement the length of the list
        self.length -= 1
        return temp