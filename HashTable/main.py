from HashTable import HashTable  # Import the HashTable class

# Create a new hash table with the default size of 7
# The size is chosen as a prime number to reduce collisions
my_hash_table = HashTable()

# Add key-value pairs to the hash table
# Each key is hashed to determine its storage location
my_hash_table.set_item('bolts', 1400)    # Store quantity of bolts
my_hash_table.set_item('washers', 50)    # Store quantity of washers
my_hash_table.set_item('lumber', 70)     # Store quantity of lumber

# Retrieve and print values associated with specific keys
# The get_item method uses the same hash function to locate the values
print(my_hash_table.get_item('bolts'))    # Output: 1400
print(my_hash_table.get_item('washers'))  # Output: 50
print(my_hash_table.get_item('lumber'))   # Output: 70

# Print the entire hash table structure
# This shows how the key-value pairs are distributed across the table
my_hash_table.print_table()

# Print all keys in the hash table
# The keys method collects all keys from all buckets
print()
print(my_hash_table.keys())  # Output: ['bolts', 'washers', 'lumber']