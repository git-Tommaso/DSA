from HashTable import HashTable

my_hash_table = HashTable() #size = 7

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('lumber'))

my_hash_table.print_table()