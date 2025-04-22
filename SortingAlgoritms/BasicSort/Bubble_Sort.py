def bubble_sort(my_list):
    """
    Sorts a list using the Bubble Sort algorithm.
    Bubble Sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order.
    
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
    # Outer loop: controls the number of passes
    # Start from the end and move towards the beginning
    for i in range(len(my_list)-1, 0, -1):
        # Inner loop: compares adjacent elements
        for j in range(i):
            # If current element is greater than next element, swap them
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

# Test the bubble sort with a sample list
print(bubble_sort([5, 2, 9, 1, 5, 6]))  # Output: [1, 2, 5, 5, 6, 9]

"""
Bubble Sort Characteristics:
- Simple to understand and implement
- Inefficient for large lists
- Stable sort (maintains relative order of equal elements)
- Performs well on nearly sorted lists
- Worst case occurs when list is in reverse order
"""