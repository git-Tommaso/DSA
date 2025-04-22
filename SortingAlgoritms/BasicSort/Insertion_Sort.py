def Insertion_Sort(my_list):
    """
    Sorts a list using the Insertion Sort algorithm.
    Insertion Sort builds the final sorted list one item at a time.
    It takes each element and inserts it into its correct position
    in the already sorted part of the list.
    
    Args:
        my_list (list): The list to be sorted
    Returns:
        list: The sorted list
    Time Complexity:
        - Best Case: O(n) when list is already sorted
        - Average Case: O(n²)
        - Worst Case: O(n²)
    Space Complexity: O(1) - sorts in place
    """
    # Start from the second element (index 1)
    for i in range(1, len(my_list)):
        # Store the current element to be inserted
        temp = my_list[i]
        # Start comparing with the previous element
        j = i - 1
        # Shift elements greater than temp to the right
        while j > -1 and temp < my_list[j]:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

# Test the insertion sort with a sample list
print(Insertion_Sort([5, 2, 9, 1, 5, 6]))  # Output: [1, 2, 5, 5, 6, 9]

"""
Insertion Sort Characteristics:
- Simple to understand and implement
- Efficient for small lists
- Stable sort (maintains relative order of equal elements)
- Performs well on nearly sorted lists
- Adaptive: performs better when input is partially sorted
- Often used as the base case for more complex sorting algorithms
"""