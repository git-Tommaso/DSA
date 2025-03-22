from Node import Node  # Import the Node class to create stack nodes

class Stack:
   def __init__(self, value):
      # Initialize the stack with a single node
      new_node = Node(value)  # Create a new node with the given value
      self.top = new_node  # Set the top of the stack to the new node
      self.height = 1  # Initialize the height of the stack to 1

   def print_stack(self):
      # Print all the values in the stack
      temp = self.top  # Start from the top of the stack
      while temp is not None:  # Traverse until the end of the stack
         print(temp.value)  # Print the value of the current node
         temp = temp.next  # Move to the next node

   def push(self, value):
      # Add a new node with the given value to the top of the stack
      new_node = Node(value)  # Create a new node
      if self.height == 0:  # If the stack is empty
         self.top = new_node  # Set the new node as the top
      else:
         new_node.next = self.top  # Link the new node to the current top
         self.top = new_node  # Update the top to the new node
      self.height += 1  # Increment the height of the stack

   def pop(self):
      # Remove and return the top node of the stack
      if self.height == 0:  # If the stack is empty
         return None  # Return None
      temp = self.top  # Store the current top node
      self.top = self.top.next  # Update the top to the next node
      temp.next = None  # Disconnect the removed node
      self.height -= 1  # Decrement the height of the stack
      return temp  # Return the removed node