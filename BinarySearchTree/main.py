"""
Binary Search Tree (BST) Demonstration
This file demonstrates various operations and traversal methods on a BST.
It shows how to create a BST, insert values, search for values, and perform different types of traversals.
"""

from BST import BinarySearchTree  # Import the BinarySearchTree class implementation

# Create a new empty BST
my_tree = BinarySearchTree()

# Insert values into the BST
# The values are inserted in a way that maintains the BST property:
# - Left child values are less than parent
# - Right child values are greater than parent
my_tree.insert(47)  # Root node
my_tree.insert(21)  # Left child of root (21 < 47)
my_tree.insert(76)  # Right child of root (76 > 47)
my_tree.insert(18)  # Left child of 21 (18 < 21)
my_tree.insert(27)  # Right child of 21 (27 > 21)
my_tree.insert(52)  # Left child of 76 (52 < 76)
my_tree.insert(82)  # Right child of 76 (82 > 76)

# Access and print node values
print(my_tree.root.value)        # Print root value (47)
print(my_tree.root.left.value)   # Print left child of root (21)
print(my_tree.root.right.value)  # Print right child of root (76)

# Search for values in the BST
print(my_tree.contains(27))  # True: 27 exists in the tree
print(my_tree.contains(17))  # False: 17 doesn't exist in the tree

# Create another BST to demonstrate different traversal methods
your_tree = BinarySearchTree()

# Insert the same values to create an identical tree structure
your_tree.insert(47)
your_tree.insert(21)
your_tree.insert(76)
your_tree.insert(18)
your_tree.insert(27)
your_tree.insert(52)
your_tree.insert(82)

"""
Traversal Methods Demonstration:

1. Breadth First Search (BFS):
   - Visits nodes level by level
   - Uses a queue to keep track of nodes to visit
   - Output: [47, 21, 76, 18, 27, 52, 82]
"""
print(your_tree.BFS())

"""
2. Depth First Search - Pre-order:
   - Visits nodes in order: Root -> Left -> Right
   - Useful for creating a copy of the tree
   - Output: [47, 21, 18, 27, 76, 52, 82]
"""
print(your_tree.dfs_pre_order())

"""
3. Depth First Search - Post-order:
   - Visits nodes in order: Left -> Right -> Root
   - Useful for deleting the tree
   - Output: [18, 27, 21, 52, 82, 76, 47]
"""
print(your_tree.dfs_post_order())

"""
4. Depth First Search - In-order:
   - Visits nodes in order: Left -> Root -> Right
   - Returns values in sorted order for BST
   - Output: [18, 21, 27, 47, 52, 76, 82]
"""
print(your_tree.dfs_in_order())