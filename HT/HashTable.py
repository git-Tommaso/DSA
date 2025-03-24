class HashTable:
   #if u don't pass any value to the constractor the default size will be 7 
   def __init__(self, size = 7):
      #create a table with size(7) empty(None) spaces 
      self.data_map = [None] * size

   def __hash(self, key):
      my_hash = 0
      for letter in key:
         #ord = ordinal (aschi number of every letter), *23 because is a prime number
         #len = lenght (default lenght = 7(prime number))
         my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
      #the number will be from 0 to 6 (after all the math)
      return my_hash
   
   def print_table(self):
      for i, val in enumerate(self.data_map):
         # i = index, val = value at that index
         print(i, ": ", val)

   def set_item(self, key, value):
      #by calling the method we will have the auto generated index
      index = self.__hash(key)
      if self.data_map[index] == None:
         self.data_map[index]  = []
      self.data_map[index].append([key, value])

   def get_item(self, key):
      index = self.__hash(key)
      if self.data_map[index] is not None:
         for i in range(len(self.data_map[index])):
            '''
            [index] is the index of the hash_map, [i] is the single dictionary in that index('key', value), and 0 because we are sercing for the key that is at index 0 of the dictionary ('key'[0], value[1])
            '''
            if self.data_map[index] [i] [0] == key:
               return self.data_map[index] [i] [1] #return the value 
         return None
