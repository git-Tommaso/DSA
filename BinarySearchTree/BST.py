from Node import Node

class BinarySearchTree:
    """
    Binary Search Tree (BST) Implementation
    A BST is a binary tree where for each node:
    - All values in the left subtree are less than the node's value
    - All values in the right subtree are greater than the node's value
    - No duplicate values are allowed
    """
    
    def __init__(self):
        """
        Initialize an empty BST with no root node
        Time Complexity: O(1)
        """
        self.root = None

    def insert(self, value):
        """
        Insert a new value into the BST while maintaining the BST property
        Time Complexity: O(log n) average case, O(n) worst case (unbalanced tree)
        
        Args:
            value: The value to be inserted into the BST
            
        Returns:
            bool: True if insertion was successful, False if value already exists
        """
        # Create a new Node instance with the given value
        new_node = Node(value)
        
        # If the tree is empty, make the new node the root
        if self.root is None:
            self.root = new_node
            return True
        
        # Start traversing from the root to find the correct position
        temp = self.root

        # Loop until we find the appropriate position for the new node
        while True:
            # Check for duplicate values (BSTs don't allow duplicates)
            if new_node.value == temp.value:
                return False
            
            # If the new value is less than current node's value, go left
            if new_node.value < temp.value:
                # If left child is empty, insert here
                if temp.left is None:
                    temp.left = new_node
                    return True
                # Otherwise, continue searching in the left subtree
                temp = temp.left
            
            # If the new value is greater than current node's value, go right
            else:
                # If right child is empty, insert here
                if temp.right is None:
                    temp.right = new_node
                    return True
                # Otherwise, continue searching in the right subtree
                temp = temp.right

    def contains(self, value):
        """
        Check if a value exists in the BST
        Time Complexity: O(log n) average case, O(n) worst case (unbalanced tree)
        
        Args:
            value: The value to search for in the BST
            
        Returns:
            bool: True if value is found, False otherwise
        """
        # Start searching from the root
        temp = self.root
        
        # Traverse the tree until we find the value or reach a leaf node
        while temp:
            # If value is less than current node, search left subtree
            if value < temp.value:
                temp = temp.left
            # If value is greater than current node, search right subtree
            elif value > temp.value:
                temp = temp.right
            # If value matches current node, we found it
            else:
                return True
        
        # If we reach here, the value was not found
        return False
    

    def BFS(self):
        """
        Breadth First Search (BFS) traversal of the BST
        Visits nodes level by level, from left to right
        Time Complexity: O(n) - visits every node exactly once
        
        Returns:
            list: Values of nodes in BFS order
        """
        # Initialize with root node
        current_node = self.root
        queue = []  # Queue to keep track of nodes to visit
        result = []  # List to store the traversal result
        queue.append(current_node)

        # Process nodes until queue is empty
        while len(queue) > 0:
            # Get the next node from the front of the queue
            current_node = queue.pop(0)
            # Add its value to the result
            result.append(current_node.value)
            # Add left child to queue if it exists
            if current_node.left:
                queue.append(current_node.left)
            # Add right child to queue if it exists
            if current_node.right:
                queue.append(current_node.right)
        return result

    def dfs_pre_order(self):
        """
        Depth First Search (DFS) Pre-order traversal
        Visits nodes in the order: Root -> Left -> Right
        Time Complexity: O(n) - visits every node exactly once
        
        Returns:
            list: Values of nodes in pre-order
        """
        result = []
        
        def traverse(current_node):
            """
            Helper function for recursive traversal
            Args:
                current_node: The current node being visited
            """
            # Visit the current node first
            result.append(current_node.value)
            # Then traverse left subtree
            if current_node.left:
                traverse(current_node.left)
            # Finally traverse right subtree
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root) 
        return result

    def dfs_post_order(self):
        """
        Depth First Search (DFS) Post-order traversal
        Visits nodes in the order: Left -> Right -> Root
        Time Complexity: O(n) - visits every node exactly once
        
        Returns:
            list: Values of nodes in post-order
        """
        result = []
        
        def traverse(current_node):
            """
            Helper function for recursive traversal
            Args:
                current_node: The current node being visited
            """
            # First traverse left subtree
            if current_node.left:
                traverse(current_node.left)
            # Then traverse right subtree
            if current_node.right:
                traverse(current_node.right)
            # Finally visit the current node
            result.append(current_node.value)

        traverse(self.root) 
        return result

    def dfs_in_order(self):
        """
        Depth First Search (DFS) In-order traversal
        Visits nodes in the order: Left -> Root -> Right
        Time Complexity: O(n) - visits every node exactly once
        
        Returns:
            list: Values of nodes in in-order (sorted order for BST)
        """
        result = []
        
        def traverse(current_node):
            """
            Helper function for recursive traversal
            Args:
                current_node: The current node being visited
            """
            # First traverse left subtree
            if current_node.left:
                traverse(current_node.left)
            # Then visit the current node
            result.append(current_node.value)
            # Finally traverse right subtree
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root) 
        return result
