def Selection_Sort(my_list):
    """
    Sorts a list using the Selection Sort algorithm.
    Selection Sort divides the list into a sorted and unsorted part.
    It repeatedly finds the minimum element from the unsorted part and
    moves it to the beginning of the sorted part.
    
    Args:
        my_list (list): The list to be sorted
    Returns:
        list: The sorted list
    Time Complexity:
        - Best Case: O(n²)
        - Average Case: O(n²)
        - Worst Case: O(n²)
    Space Complexity: O(1) - sorts in place
    """
    # Outer loop: controls the sorted portion of the list
    for i in range(len(my_list)-1):
        # Assume the current position has the minimum value
        min_index = i
        # Inner loop: find the minimum value in the unsorted portion
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        # Swap the minimum value with the current position if different
        if min_index != i:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

# Test the selection sort with a sample list
print(Selection_Sort([5, 2, 9, 1, 5, 6]))  # Output: [1, 2, 5, 5, 6, 9]

"""
Selection Sort Characteristics:
- Simple to understand and implement
- Inefficient for large lists
- Not stable (may change relative order of equal elements)
- Performs the same number of comparisons regardless of input order
- Makes fewer swaps than Bubble Sort
"""