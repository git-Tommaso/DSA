from Node import Node

class BinarySearchTree:
    # Constructor: initializes the tree with an empty root (i.e., no nodes yet).
    def __init__(self):
        self.root = None

    # Method to insert a new value into the binary search tree.
    def insert(self, value):
        # Create a new Node instance with the given value.
        new_node = Node(value)
        
        # If the tree is empty (root is None), set the root to the new node.
        if self.root is None:
            self.root = new_node
            return True
        
        # Start traversing the tree from the root.
        temp = self.root

        # Traverse the tree to find the correct position for the new node.
        while True:
            # If the value already exists in the tree, do not insert it.
            # Binary tree can't contain duplicates
            if new_node.value == temp.value:
                return False
            
            # If the new value is less than the current node's value:
            if new_node.value < temp.value:
                # If the left child is empty, place the new node there.
                if temp.left is None:
                    temp.left = new_node
                    return True
                # Otherwise, continue to the left child.
                temp = temp.left
            
            # If the new value is greater than the current node's value:
            else:
                # If the right child is empty, place the new node there.
                if temp.right is None:
                    temp.right = new_node
                    return True
                # Otherwise, continue to the right child.
                temp = temp.right

    # Method to check if a given value exists in the tree.
    def contains(self, value):
        # Start traversing the tree from the root.
        temp = self.root
        
        # Traverse until we find the value or reach a dead end (None).
        while temp:
            # If the value is smaller, go to the left subtree.
            if value < temp.value:
                temp = temp.left
            # If the value is larger, go to the right subtree.
            elif value > temp.value:
                temp = temp.right
            # If the value matches, return True (value is found).
            else:
                return True
        
        # If traversal ends and the value is not found, return False.
        return False
    

    #Traversal Tree
    #breadth first search
    def BFS(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result
    #depth first search:
    #pre-order
    def dfs_pre_order(self):
        result = []
        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root) 
        return result
    #Post-order
    def dfs_post_order(self):
        result = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            result.append(current_node.value)

        traverse(self.root) 
        return result
    #In-order
    def dfs_in_order(self):
        result = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root) 
        return result
