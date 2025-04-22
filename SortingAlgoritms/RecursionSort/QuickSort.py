def swap(my_list, index1, index2):
    """
    Swaps two elements in a list.
    
    Args:
        my_list (list): The list containing elements to swap
        index1 (int): Index of first element
        index2 (int): Index of second element
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
    """
    Partitions the list around a pivot element.
    All elements less than the pivot are moved to its left,
    and all elements greater than the pivot are moved to its right.
    
    Args:
        my_list (list): The list to partition
        pivot_index (int): Index of the pivot element
        end_index (int): Last index of the sublist to consider
    Returns:
        int: The final index of the pivot element
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    swap_index = pivot_index

    # Traverse the list and move elements smaller than pivot to the left
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    # Move the pivot to its correct position
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    """
    Helper function for Quick Sort that recursively sorts sublists.
    
    Args:
        my_list (list): The list to sort
        left (int): Starting index of the sublist
        right (int): Ending index of the sublist
    Returns:
        list: The sorted list
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n) for recursion stack
    """
    if left < right:
        # Get the pivot index and sort the sublists
        pivot_index = pivot(my_list, left, right)
        # Sort the left sublist
        quick_sort_helper(my_list, left, pivot_index-1)
        # Sort the right sublist
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list

def quick_sort(my_list):
    """
    Sorts a list using the Quick Sort algorithm.
    Quick Sort is a divide-and-conquer algorithm that selects a 'pivot' element
    and partitions the list around the pivot, placing smaller elements to the left
    and larger elements to the right.
    
    Args:
        my_list (list): The list to be sorted
    Returns:
        list: The sorted list
    Time Complexity:
        - Best Case: O(n log n)
        - Average Case: O(n log n)
        - Worst Case: O(n²)
    Space Complexity: O(log n) for recursion stack
    """
    return quick_sort_helper(my_list, 0, len(my_list)-1)

# Test the quick sort with a sample list
my_list = [4, 6, 1, 7, 3, 2, 5]
print(quick_sort(my_list))  # Output: [1, 2, 3, 4, 5, 6, 7]

"""
Quick Sort Characteristics:
- Not stable (may change relative order of equal elements)
- In-place sorting (requires minimal additional space)
- Efficient for large datasets
- Performance depends on pivot selection
- Worst case occurs when pivot is smallest or largest element
- Often faster than Merge Sort in practice due to better cache performance
"""
