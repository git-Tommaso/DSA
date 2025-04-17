class HashTable:
   # Constructor to initialize the hash table with a default size of 7
   def __init__(self, size = 7):
      # Create a list with 'size' number of None values
      self.data_map = [None] * size

   # Private method to generate a hash for a given key
   def __hash(self, key):
      my_hash = 0
      for letter in key:
         # Calculate hash using ASCII value of letters and a prime multiplier
         my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
      return my_hash  # Return the hash index
   
   # Method to print the entire hash table
   def print_table(self):
      for i, val in enumerate(self.data_map):
         # Print the index and its corresponding value
         print(i, ": ", val)

   # Method to add a key-value pair to the hash table
   def set_item(self, key, value):
      index = self.__hash(key)  # Generate hash index for the key
      if self.data_map[index] == None:
         self.data_map[index]  = []  # Initialize a list at the index if empty
      self.data_map[index].append([key, value])  # Append the key-value pair

   # Method to retrieve the value associated with a key
   def get_item(self, key):
      index = self.__hash(key)  # Generate hash index for the key
      if self.data_map[index] is not None:
         for i in range(len(self.data_map[index])):
            # Check if the key matches and return its value
            if self.data_map[index][i][0] == key:
               return self.data_map[index][i][1]
      return None  # Return None if the key is not found

   # Method to retrieve all keys in the hash table
   def keys(self):
      all_keys = []
      for i in range(len(self.data_map)):
         if self.data_map[i] is not None:
            for j in range(len(self.data_map[i])):
               all_keys.append(self.data_map[i][j][0])  # Append each key
      return all_keys
