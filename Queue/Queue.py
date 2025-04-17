from Node import Node  # Import the Node class to create queue nodes

class Queue:
   def __init__(self, value):
      # Initialize the queue with a single node
      new_node = Node(value)  # Create a new node with the given value
      self.first = new_node  # Set the first node of the queue
      self.last = new_node  # Set the last node of the queue
      self.length = 1  # Initialize the length of the queue to 1

   def print_queue(self):
      # Print all the values in the queue
      temp = self.first  # Start from the first node
      while temp:  # Traverse until the end of the queue
         print(temp.value)  # Print the value of the current node
         temp = temp.next  # Move to the next node

   def Enqueue(self, value):
      # Add a new node with the given value to the end of the queue
      new_node = Node(value)  # Create a new node
      if self.first is None:  # If the queue is empty
         self.first = new_node  # Set the new node as the first
         self.last = new_node  # Set the new node as the last
      else:
         self.last.next = new_node  # Link the current last node to the new node
         self.last = new_node  # Update the last node to the new node
      self.length += 1  # Increment the length of the queue

   def Dequeue(self):
      # Remove and return the first node of the queue
      if self.length == 0:  # If the queue is empty
         return None  # Return None
      temp = self.first  # Store the current first node
      if self.length == 1:  # If the queue has only one node
         self.last = None  # Set the last node to None
         self.first = None  # Set the first node to None
      else:
         self.first = self.first.next  # Update the first node to the next node
         temp.next = None  # Disconnect the removed node
      self.length -= 1  # Decrement the length of the queue
      return temp  # Return the removed node