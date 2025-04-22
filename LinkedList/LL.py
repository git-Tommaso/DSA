from Node import Node  # Import the Node class to create linked list nodes

class LinkedList:
    """
    Implements a Singly Linked List data structure.
    Provides methods to manipulate the list, such as adding, removing, updating, and reversing nodes.
    
    Attributes:
        head: Reference to the first node in the list
        tail: Reference to the last node in the list
        length: Number of nodes in the list
        
    Time Complexities:
        - Append: O(1)
        - Prepend: O(1)
        - Pop: O(n)
        - Pop First: O(1)
        - Get: O(n)
        - Set: O(n)
        - Insert: O(n)
        - Remove: O(n)
        - Reverse: O(n)
    Space Complexity:
        - O(n) where n is the number of nodes
    """

    def _is_out_of_bounds_(self, index):
        """
        Helper method to check if an index is valid.
        
        Args:
            index (int): The index to check
        Returns:
            bool: True if index is out of bounds, False otherwise
        """
        return index < 0 or index >= self.length

    def __init__(self, value):
        """
        Initializes the Linked List with a single node.
        
        Args:
            value: The value to store in the first node
        """
        new_node = Node(value)  # Create a new node
        self.head = new_node  # Set the new node as the head
        self.tail = new_node  # Set the new node as the tail
        self.length = 1  # Initialize the length of the list to 1

    def print_list(self):
        """
        Prints all the values in the Linked List.
        Time Complexity: O(n)
        """
        temp = self.head  # Start from the head
        while temp is not None:  # Traverse the list until the end
            print(temp.value)  # Print the value of the current node
            temp = temp.next  # Move to the next node

    def append(self, value):
        """
        Adds a new node with the given value to the end of the list.
        
        Args:
            value: The value to append
        Returns:
            bool: True if successful
        Time Complexity: O(1)
        """
        new_node = Node(value)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set the new node as the head
            self.tail = new_node  # Set the new node as the tail
        else:
            self.tail.next = new_node  # Link the current tail to the new node
            self.tail = new_node  # Update the tail to the new node
        self.length += 1  # Increment the length of the list
        return True

    def pop(self):
        """
        Removes the last node from the list and returns its value.
        
        Returns:
            The value of the removed node, or None if the list is empty
        Time Complexity: O(n)
        """
        if self.length == 0:  # If the list is empty
            return None
        temp = self.head
        pre = self.head
        while temp.next:  # Traverse to the last node
            pre = temp
            temp = temp.next
        self.tail = pre  # Update the tail to the second-to-last node
        self.tail.next = None  # Remove the reference to the last node
        self.length -= 1
        if self.length == 0:  # If the list is now empty
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        """
        Adds a new node with the given value to the beginning of the list.
        
        Args:
            value: The value to prepend
        Returns:
            bool: True if successful
        Time Complexity: O(1)
        """
        new_node = Node(value)
        if self.length == 0:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # Link the new node to the current head
            self.head = new_node  # Update the head to the new node
        self.length += 1
        return True

    def pop_first(self):
        """
        Removes the first node from the list and returns its value.
        
        Returns:
            The value of the removed node, or None if the list is empty
        Time Complexity: O(1)
        """
        if self.length == 0:  # If the list is empty
            return None
        temp = self.head  # Store the current head
        self.head = self.head.next  # Update the head to the next node
        temp.next = None  # Remove the reference to the next node
        self.length -= 1
        if self.length == 0:  # If the list is now empty
            self.tail = None
        return temp.value

    def get(self, index):
        """
        Returns the node at the specified index.
        
        Args:
            index (int): The index of the node to retrieve
        Returns:
            Node: The node at the specified index, or None if index is invalid
        Time Complexity: O(n)
        """
        if self._is_out_of_bounds_(index):  # Check if the index is valid
            return None
        temp = self.head
        for _ in range(index):  # Traverse to the desired index
            temp = temp.next
        return temp

    def set_value(self, index, value):
        """
        Updates the value of the node at the specified index.
        
        Args:
            index (int): The index of the node to update
            value: The new value to set
        Returns:
            bool: True if successful, False if index is invalid
        Time Complexity: O(n)
        """
        temp = self.get(index)  # Get the node at the index
        if temp:  # If the node exists
            temp.value = value  # Update the value
            return True
        return False

    def insert(self, index, value):
        """
        Inserts a new node with the given value at the specified index.
        
        Args:
            index (int): The position to insert the new node
            value: The value to insert
        Returns:
            bool: True if successful, False if index is invalid
        Time Complexity: O(n)
        """
        if self._is_out_of_bounds_(index):
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)  # Get the node before the insertion point
        new_node.next = temp.next  # Link the new node to the next node
        temp.next = new_node  # Link the previous node to the new node
        self.length += 1
        return True

    def remove(self, index):
        """
        Removes the node at the specified index and returns it.
        
        Args:
            index (int): The index of the node to remove
        Returns:
            Node: The removed node, or None if index is invalid
        Time Complexity: O(n)
        """
        if self._is_out_of_bounds_(index):
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)  # Get the node before the one to remove
        temp = prev.next  # Node to remove
        prev.next = temp.next  # Skip the node to remove
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        """
        Reverses the order of the Linked List.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        temp = self.head  # Start from the head
        self.head = self.tail  # Swap the head and tail
        self.tail = temp  # Update the tail to the original head
        after = temp.next  # Store the next node
        before = None  # Initialize the previous node as None
        for _ in range(self.length):  # Traverse the list
            after = temp.next  # Store the next node
            temp.next = before  # Reverse the link
            before = temp  # Move the previous pointer forward
            temp = after  # Move the current pointer forward