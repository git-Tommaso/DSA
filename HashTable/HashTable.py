class HashTable:
    """
    Implements a Hash Table data structure using separate chaining for collision resolution.
    The hash table uses a list of lists to store key-value pairs, where each index in the
    main list can contain multiple key-value pairs in case of collisions.
    """
    
    def __init__(self, size = 7):
        """
        Initializes the hash table with a specified size (default is 7).
        The size is typically chosen as a prime number to reduce collisions.
        Args:
            size (int): The initial size of the hash table
        """
        # Create a list with 'size' number of None values to represent empty buckets
        self.data_map = [None] * size

    def __hash(self, key):
        """
        Private method to generate a hash value for a given key.
        Uses a combination of ASCII values and a prime multiplier (23) to create
        a more uniform distribution of hash values.
        Args:
            key (str): The key to be hashed
        Returns:
            int: The hash index where the key-value pair should be stored
        """
        my_hash = 0
        for letter in key:
            # Calculate hash using ASCII value of letters and a prime multiplier
            # The modulo operation ensures the hash value is within the table size
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
   
    def print_table(self):
        """
        Prints the current state of the hash table.
        Shows each index and its corresponding key-value pairs.
        Useful for debugging and visualization.
        """
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        """
        Adds a key-value pair to the hash table.
        If a collision occurs, the new pair is added to the list at that index.
        Args:
            key (str): The key to be stored
            value: The value associated with the key
        """
        # Generate hash index for the key
        index = self.__hash(key)
        # If the bucket is empty, initialize it with an empty list
        if self.data_map[index] == None:
            self.data_map[index] = []
        # Append the key-value pair to the bucket
        self.data_map[index].append([key, value])

    def get_item(self, key):
        """
        Retrieves the value associated with a given key.
        Args:
            key (str): The key to search for
        Returns:
            The value associated with the key, or None if the key is not found
        """
        # Generate hash index for the key
        index = self.__hash(key)
        # If the bucket exists and is not empty
        if self.data_map[index] is not None:
            # Search through the bucket for the matching key
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        """
        Returns a list of all keys in the hash table.
        Returns:
            list: A list containing all keys in the hash table
        """
        all_keys = []
        # Iterate through all buckets
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                # Iterate through all key-value pairs in the bucket
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
