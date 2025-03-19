class Node:
    # Constructor
    def __init__(self, value):
        self.value = value  # Assign the value to the node
        self.next = None  # Set the next pointer to None, as there's no next node yet


class LinkedList:
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
        if index < 0 or index >= self.length:  # Check for out-of-bounds index
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
      if index < 0 or index >= self.length:
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


# ---------------------MAIN----------------------#

# Test the linked list
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

# Update a value and print the list
my_linked_list.set_value(1, 4)
my_linked_list.instert(2,5)
my_linked_list.print_list()

# Uncomment the following sections to test other methods:

# Test the pop method
# print(my_linked_list.pop())  # (2) Items - Returns 2 Node
# print(my_linked_list.pop())  # (1) Items - Returns 1 Node
# print(my_linked_list.pop())  # (0) Items - Returns None

# Test the pop_first method
# print(my_linked_list.pop_first())  # (2) Items - Returns 2 Node
# print(my_linked_list.pop_first())  # (1) Items - Returns 1 Node
# print(my_linked_list.pop_first())  # (0) Items - Returns None