from BST import BinarySearchTree  # Importing the BinarySearchTree class from the BST module.

# Creating an instance of the BinarySearchTree class.
my_tree = BinarySearchTree()

# Inserting values into the binary search tree.
my_tree.insert(47)  # Insert the value 47 as the root of the tree (if the tree is empty).
my_tree.insert(21)  # Insert the value 21 into the left subtree of the root (since 21 < 47).
my_tree.insert(76)  # Insert the value 76 into the right subtree of the root (since 76 > 47).
my_tree.insert(18)  # Insert the value 18 into the left subtree of node 21 (since 18 < 21).
my_tree.insert(27)  # Insert the value 27 into the right subtree of node 21 (since 27 > 21).
my_tree.insert(52)  # Insert the value 52 into the left subtree of node 76 (since 52 < 76).
my_tree.insert(82)  # Insert the value 82 into the right subtree of node 76 (since 82 > 76).

# Printing the value of the root node.
print(my_tree.root.value)  # Output: 47 (root value).

# Printing the values of the left and right children of the root node.
print(my_tree.root.left.value)  # Output: 21 (left child of root).
print(my_tree.root.right.value)  # Output: 76 (right child of root).

# Checking if the tree contains specific values.
print(my_tree.contains(27))  # Output: True (value 27 is present in the tree).
print(my_tree.contains(17))  # Output: False (value 17 is not present in the tree).

#example of breadth first search

your_tree = BinarySearchTree()

your_tree.insert(47)
your_tree.insert(21)
your_tree.insert(76)
your_tree.insert(18)
your_tree.insert(27)
your_tree.insert(52)
your_tree.insert(82)

print(your_tree.BFS())  # Output: [47, 21, 76, 18, 27, 52, 82]

print(your_tree.dfs_pre_order())  # Output: [47, 21, 18, 27, 76, 52, 82]

print(your_tree.dfs_post_order())  # Output: [18, 21, 27, 47, 52, 76, 82]

print(your_tree.dfs_in_order())  # Output: [18, 21, 27, 47, 52, 76, 82]