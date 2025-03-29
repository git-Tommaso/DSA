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