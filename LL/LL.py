class Node:
   # construttore
   def __init__(self, value):
      self.value = value  # prende il valore e lo mette in value
      self.next = None  # mette il puntatore successivo nullo, perché non c'è un altro nodo

class LinkedList:
   # il construttore
   def __init__(self, value):
      # creiamo una nuova variabile chiamata node (istanza), chiama la classe Node e gli passiamo il valore
      new_node = Node(value)
      self.head = new_node
      self.tail = new_node
      self.length = 1

   #print_list method
   def print_list(self):
      temp = self.head  # temp è uguale alla head (è un nodo, quindi ha un valore e un next)
      while temp is not None:  # finché temp non è nullo
         print(temp.value)  # stampa il valore di temp
         temp = temp.next  # temp diventa il prossimo nodo
   #append method
   def append(self, value):
      new_node = Node(value)
      if self.head is None:
         self.head = new_node
         self.tail = new_node
      else:
         self.tail.next = new_node  # corretto qui!
         self.tail = new_node
      self.length += 1
      return True
   #pop method
   def pop(self):
      if self.length == 0:
         return None
      temp = self.head
      pre = self.head
      while (temp.next):
         pre = temp
         temp = temp.next
      self.tail = pre
      self.tail.next = None
      self.length -= 1
      if self.length == 0:
         self.head = None
         self.tail = None
      #for test purpose
      return temp.value


#---------------------MAIN----------------------#

# Testare la lista collegata
my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop())
# (1) Items - Returns 1 Node
print(my_linked_list.pop())
# (0) Items - Returns None
print(my_linked_list.pop())