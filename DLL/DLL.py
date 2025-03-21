from Node import Node

class DoublyLinkedList:
    """
    Implements a Doubly Linked List data structure.
    Provides methods to manipulate the list, such as adding, removing, updating, and traversing nodes.
    """

    def __init__(self, value):
        """
        Initializes the Doubly Linked List with a single node.
        """
        # Create a new node with the given value
        new_node = Node(value)
        # Set the head and tail to the new node
        self.head = new_node
        self.tail = new_node
        # Initialize the length of the list to 1
        self.length = 1

    def print_list(self):
        """
        Prints all the values in the Doubly Linked List.
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
        """
        # Create a new node with the given value
        new_node = Node(value)
        # If the list is empty, set head and tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Link the current tail to the new node
            self.tail.next = new_node
            new_node.prev = self.tail
            # Update the tail to the new node
            self.tail = new_node
        # Increment the length of the list
        self.length += 1
        return True

    def pop(self):
        """
        Removes the last node from the list and returns it.
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
            self.tail.next = None
            temp.prev = None
        # Decrement the length of the list
        self.length -= 1
        return temp

    def prepend(self, value):
        """
        Adds a new node with the given value to the beginning of the list.
        """
        # Create a new node with the given value
        new_node = Node(value)
        # If the list is empty, set head and tail to the new node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node to the current head
            new_node.next = self.head
            self.head.prev = new_node
            # Update the head to the new node
            self.head = new_node
        # Increment the length of the list
        self.length += 1
        return True

    def pop_first(self):
        """
        Removes the first node from the list and returns it.
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
            self.head.prev = None
            temp.next = None
        # Decrement the length of the list
        self.length -= 1
        return temp

    def get(self, index):
        """
        Returns the node at the specified index.
        """
        # Return None if the index is out of bounds
        if index < 0 or index >= self.length:
            return None
        # Decide whether to traverse from the head or tail
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
        """
        # Return None if the index is out of bounds
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

        # Update the links of the neighboring nodes
        temp.next.prev = temp.prev
        temp.prev.next = temp.next

        # Disconnect the node to be removed
        temp.next = None
        temp.prev = None

        # Decrement the length of the list
        self.length -= 1
        return temp