from HashTable import HashTable  # Import the HashTable class

# Create a new hash table with the default size of 7
my_hash_table = HashTable()

# Add key-value pairs to the hash table
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

# Retrieve and print values associated with specific keys
print(my_hash_table.get_item('bolts'))  # Output: 1400
print(my_hash_table.get_item('washers'))  # Output: 50
print(my_hash_table.get_item('lumber'))  # Output: 70

# Print the entire hash table
my_hash_table.print_table()

# Print all keys in the hash table
print()
print(my_hash_table.keys())  # Output: ['bolts', 'washers', 'lumber']