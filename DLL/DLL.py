from Node import Node

class DoublyLinkedList:
   def __init__(self, value):
      new_node = Node(value)
      self.head = new_node
      self.tail = new_node
      self.length = 1
   
   def print_list(self):
      temp = self.head
      while temp:
         print(temp.value)
         temp = temp.next
      