class MaxHeap:
    """
    Implements a Max Heap data structure.
    A Max Heap is a complete binary tree where each parent node is greater than or equal to its children.
    This implementation uses a list to represent the heap structure.
    """
    
    def __init__(self):
        """
        Initializes an empty Max Heap.
        The heap is represented as a list where:
        - For any node at index i:
          - Left child is at 2*i + 1
          - Right child is at 2*i + 2
          - Parent is at (i-1)//2
        """
        self.heap = []
   
    # helper methods
    def _left_child(self, index):
        """
        Returns the index of the left child of the node at the given index.
        Args:
            index (int): The index of the parent node
        Returns:
            int: The index of the left child
        """
        return 2 * index + 1
   
    def _right_child(self, index):
        """
        Returns the index of the right child of the node at the given index.
        Args:
            index (int): The index of the parent node
        Returns:
            int: The index of the right child
        """
        return 2 * index + 2
   
    def _parent(self, index):
        """
        Returns the index of the parent of the node at the given index.
        Args:
            index (int): The index of the child node
        Returns:
            int: The index of the parent node
        """
        return (index - 1) // 2
   
    def _swap(self, index1, index2):
        """
        Swaps the values at two indices in the heap.
        Args:
            index1 (int): First index to swap
            index2 (int): Second index to swap
        """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index):
        """
        Maintains the heap property by moving a node down the heap until it's in the correct position.
        This is used after removing the root to restore the heap property.
        Args:
            index (int): The index of the node to sink down
        """
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            # Compare with left child
            if (left_index < len(self.heap) and 
                self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            # Compare with right child
            if (right_index < len(self.heap) and 
                self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            # If the current node is not the maximum, swap and continue
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
         
    # methods
    def insert(self, value):
        """
        Inserts a new value into the heap while maintaining the heap property.
        The new value is added at the end and then bubbled up to its correct position.
        Args:
            value: The value to be inserted
        """
        # Add the new value at the end of the heap
        self.heap.append(value)
        current = len(self.heap) - 1

        # Bubble up the new value until it's in the correct position
        while (current > 0 and 
               self.heap[current] > self.heap[self._parent(current)]):
            self._swap(current, self._parent(current))
            current = self._parent(current)
   
    def remove(self):
        """
        Removes and returns the maximum value (root) from the heap.
        The last element is moved to the root and then sunk down to maintain the heap property.
        Returns:
            The maximum value in the heap, or None if the heap is empty
        """
        if len(self.heap) == 0:
            return None
      
        if len(self.heap) == 1:
            return self.heap.pop()
      
        # Store the maximum value (root)
        max_value = self.heap[0]
        # Move the last element to the root
        self.heap[0] = self.heap.pop()
        # Restore the heap property
        self._sink_down(0)

        return max_value
