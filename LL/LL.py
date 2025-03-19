from Node import Node

class LinkedList:
    def _is_out_of_bounds_(self, index):
        return index < 0 or index >= self.length
    
    # Constructor
    def __init__(self, value):
        # Create a new node instance and assign it as both head and tail
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Print the list
    def print_list(self):
        temp = self.head  # Start from the head
        while temp is not None:  # Traverse until the end of the list
            print(temp.value)  # Print the value of the current node
            temp = temp.next  # Move to the next node

    # Append a new node to the end of the list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link the current tail to the new node
            self.tail = new_node  # Update the tail to the new node
        self.length += 1
        return True

    # Remove the last node from the list
    def pop(self):
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
        return temp.value  # Return the value of the removed node

    # Prepend a new node to the beginning of the list
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # Link the new node to the current head
            self.head = new_node  # Update the head to the new node
        self.length += 1
        return True

    # Remove the first node from the list
    def pop_first(self):
        if self.length == 0:  # If the list is empty
            return None
        temp = self.head  # Store the current head
        self.head = self.head.next  # Update the head to the next node
        temp.next = None  # Remove the reference to the next node
        self.length -= 1
        if self.length == 0:  # If the list is now empty
            self.tail = None
        return temp.value  # Return the value of the removed node

    # Get the value of a node at a specific index
    def get(self, index):
        if self._is_out_of_bounds_(index):  # Check for out-of-bounds index
            return None
        temp = self.head
        for _ in range(index):  # Traverse to the desired index
            temp = temp.next
        return temp  # Return the value of the node

    # Set the value of a node at a specific index
    def set_value(self, index, value):
        temp = self.get(index)  # Reuse the get method to find the node
        if temp:  # If the node exists
            temp.value = value  # Update the value
            return True
        return False
    
   # Insert a new node at a specific index
    def instert(self, index ,value):
      if self._is_out_of_bounds_(index):
         return False
      if index == 0:
         return self.prepend(value)
      if index == self.length:
         return self.append(value)

      new_node = Node(value)
      temp = self.get(index-1)
      new_node.next = temp.next
      temp.next = new_node
      self.length += 1
      return True    
    
    # Remove a node at a specific index
    def remove(self,index):
      if self._is_out_of_bounds_(index):
            return None
      if index == 0:
            return self.pop_first()
      if index == self.length - 1:
         return self.pop()
      prev = self.get(index - 1)
      temp = prev.next
      prev.next = temp.next
      temp.next = None
      self.length -= 1
      return temp
    # Reverse the linked list
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after        
