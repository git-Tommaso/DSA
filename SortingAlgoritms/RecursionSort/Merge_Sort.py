def merge(list1, list2):
    """
    Merges two sorted lists into a single sorted list.
    
    Args:
        list1 (list): First sorted list
        list2 (list): Second sorted list
    Returns:
        list: Combined sorted list
    Time Complexity: O(n) where n is the total length of both lists
    Space Complexity: O(n) for the combined list
    """
    combined = []
    i = 0  # Pointer for list1
    j = 0  # Pointer for list2
    
    # Compare elements from both lists and add the smaller one
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    # Add remaining elements from list1 if any
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    # Add remaining elements from list2 if any
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    
    return combined

def merge_sort(my_list):
    """
    Sorts a list using the Merge Sort algorithm.
    Merge Sort is a divide-and-conquer algorithm that recursively
    splits the list into halves, sorts them, and then merges them.
    
    Args:
        my_list (list): The list to be sorted
    Returns:
        list: The sorted list
    Time Complexity:
        - Best Case: O(n log n)
        - Average Case: O(n log n)
        - Worst Case: O(n log n)
    Space Complexity: O(n) for the auxiliary space
    """
    # Base case: list of length 1 is already sorted
    if len(my_list) == 1:
        return my_list
    
    # Split the list into two halves
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])  # Sort left half
    right = merge_sort(my_list[mid_index:])  # Sort right half

    # Merge the sorted halves
    return merge(left, right)

# Test the merge sort with a sample list
original_list = [3, 1, 4, 2]
sorted_list = merge_sort(original_list)

print("Original list: ", original_list)
print("\nSorted list:  ", sorted_list)

"""
Merge Sort Characteristics:
- Stable sort (maintains relative order of equal elements)
- Not adaptive (performance is the same regardless of input order)
- Well-suited for large datasets
- Requires additional space for merging
- Good for external sorting (sorting data on disk)
- Parallelizable (can be implemented to run on multiple processors)
"""