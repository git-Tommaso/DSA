"""
Binary Search Tree (BST) - Under the Hood
This file demonstrates the basic structure of a BST using Python dictionaries.
It shows how nodes are connected and explains key BST concepts.
"""

# A simple root node with no children
# This represents the most basic form of a BST - just a single node
root = {
   "value": 4,      # The data stored in this node
   "left": None,    # Pointer to left child (smaller values)
   "right": None    # Pointer to right child (larger values)
}

# A more complex BST structure with multiple levels
# This example shows a complete BST with all levels filled
ROOT = {  # This is the PARENT node (root of the entire tree)
   "value": 4,  # The value stored in the root node
   "left": {    # LEFT CHILD (contains values less than parent)
      "value": 3,  # Value of left child
      "left": None,  # This is a LEAF node (no children)
      "right": None  # This is a LEAF node (no children)
   },
   "right": {   # RIGHT CHILD (contains values greater than parent)
      "value": 23,  # Value of right child
      "left": None,  # This is a LEAF node (no children)
      "right": None  # This is a LEAF node (no children)
   }
}

"""
Tree Properties Explained:
1. Full Tree: Every node has either 0 or 2 children
2. Perfect Tree: All leaf nodes are at the same level
3. Complete Tree: All levels are completely filled except possibly the last level,
   and the last level has all nodes as far left as possible

This example demonstrates a tree that is:
- Full: Each non-leaf node has exactly 2 children
- Perfect: All leaves are at the same level (level 2)
- Complete: All levels are completely filled

Time Complexity Analysis:
- Insertion: O(log n) - We traverse the tree height, which is log n in balanced trees
- Search: O(log n) - We traverse the tree height, which is log n in balanced trees
- Deletion: O(log n) - We traverse the tree height, which is log n in balanced trees

Note: These time complexities assume a balanced tree. In worst case (unbalanced tree),
the time complexity can degrade to O(n).
"""

#this is a full tree because every element has two children
#and is also a perfect tree because all the leaves are at the same level
#and is complete, because all the levels are full (with no gaps)

#big 0 notation
#insertion: O(log n)
#search: O(log n)
#deletion: O(log n)