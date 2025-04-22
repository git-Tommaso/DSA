from MaxHeap import MaxHeap

# Create a new Max Heap
myheap = MaxHeap()

# Insert values into the heap
# The heap will automatically maintain the max heap property
myheap.insert(99)  # Insert 99 (becomes root)
myheap.insert(72)  # Insert 72 (becomes left child of 99)
myheap.insert(61)  # Insert 61 (becomes right child of 99)
myheap.insert(58)  # Insert 58 (becomes left child of 72)

# Print the current state of the heap
# The heap should be: [99, 72, 61, 58]
print(myheap.heap)  

# Insert a larger value (100)
# This will bubble up to become the new root
myheap.insert(100)
print(myheap.heap)  # Expected: [100, 99, 61, 58, 72]

# Insert another value (75)
# This will be placed appropriately in the heap
myheap.insert(75)
print(myheap.heap)  # Expected: [100, 99, 75, 58, 72, 61]

"""
   EXPECTED OUTPUT:
   ----------------------
   [99, 72, 61, 58]
   [100, 99, 61, 58, 72]
   [100, 99, 75, 58, 72, 61]
"""

print()

# Remove the maximum value (root) from the heap
# The last element will be moved to the root and sunk down
myheap.remove()
print(myheap.heap)  # Expected: [99, 72, 75, 58, 61]

# Remove the maximum value again
myheap.remove()
print(myheap.heap)  # Expected: [75, 72, 61, 58]

"""
   EXPECTED OUTPUT:
   ----------------------
   [99, 72, 75, 58, 61]
   [75, 72, 61, 58]
"""