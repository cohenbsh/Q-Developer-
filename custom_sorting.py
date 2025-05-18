"""
Custom Sorting Algorithms

This module implements custom sorting algorithms without using Python's built-in
sort() or sorted() functions. It includes implementations of bubble sort and
insertion sort algorithms that can handle both numeric and alphabetical sorting.
"""

def validate_input(items):
    """
    Validates that the input is a list and contains only numbers or strings.
    
    Args:
        items: The input to validate
        
    Returns:
        bool: True if input is valid, False otherwise
        str: Error message if input is invalid, None otherwise
    """
    # Check if input is a list
    if not isinstance(items, list):
        return False, "Input must be a list"
    
    # Check if list is empty
    if len(items) == 0:
        return True, None
    
    # Check if all elements are of the same type (numbers or strings)
    first_item_type = type(items[0])
    
    if first_item_type not in (int, float, str):
        return False, "List elements must be numbers or strings"
    
    for item in items:
        if not isinstance(item, (int, float, str)):
            return False, "List elements must be numbers or strings"
        
        # If mixing strings and numbers, return error
        if isinstance(item, (int, float)) and first_item_type == str:
            return False, "Cannot mix strings and numbers in the same list"
        if isinstance(item, str) and first_item_type in (int, float):
            return False, "Cannot mix strings and numbers in the same list"
    
    return True, None

def bubble_sort(items):
    """
    Implements the bubble sort algorithm.
    
    Time Complexity: O(n²) - where n is the number of items
    
    Args:
        items (list): List of numbers or strings to sort
        
    Returns:
        list: Sorted list in ascending order
        list: List of steps showing the sorting process
    """
    # Validate input
    is_valid, error_msg = validate_input(items)
    if not is_valid:
        raise ValueError(error_msg)
    
    # Create a copy of the list to avoid modifying the original
    items_copy = items.copy()
    steps = [f"Initial list: {items_copy}"]
    
    n = len(items_copy)
    
    # If list is empty or has only one element, it's already sorted
    if n <= 1:
        steps.append("List is already sorted")
        return items_copy, steps
    
    # Bubble sort algorithm
    for i in range(n):
        # Flag to optimize if no swaps are made in a pass
        swapped = False
        
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if items_copy[j] > items_copy[j + 1]:
                # Swap elements
                items_copy[j], items_copy[j + 1] = items_copy[j + 1], items_copy[j]
                swapped = True
                steps.append(f"Swap {items_copy[j]} and {items_copy[j+1]}: {items_copy}")
        
        # If no swaps were made in this pass, the list is sorted
        if not swapped:
            steps.append("No swaps needed, list is sorted")
            break
    
    steps.append(f"Final sorted list: {items_copy}")
    return items_copy, steps

def insertion_sort(items):
    """
    Implements the insertion sort algorithm.
    
    Time Complexity: O(n²) - where n is the number of items
    
    Args:
        items (list): List of numbers or strings to sort
        
    Returns:
        list: Sorted list in ascending order
        list: List of steps showing the sorting process
    """
    # Validate input
    is_valid, error_msg = validate_input(items)
    if not is_valid:
        raise ValueError(error_msg)
    
    # Create a copy of the list to avoid modifying the original
    items_copy = items.copy()
    steps = [f"Initial list: {items_copy}"]
    
    n = len(items_copy)
    
    # If list is empty or has only one element, it's already sorted
    if n <= 1:
        steps.append("List is already sorted")
        return items_copy, steps
    
    # Insertion sort algorithm
    for i in range(1, n):
        key = items_copy[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and items_copy[j] > key:
            items_copy[j + 1] = items_copy[j]
            j -= 1
        
        # Insert the key at the correct position
        if j + 1 != i:  # Only record step if an actual insertion happened
            items_copy[j + 1] = key
            steps.append(f"Insert {key} at position {j+1}: {items_copy}")
    
    steps.append(f"Final sorted list: {items_copy}")
    return items_copy, steps

def custom_sort(items, algorithm="bubble"):
    """
    Sorts a list using the specified algorithm.
    
    Args:
        items (list): List of numbers or strings to sort
        algorithm (str): The sorting algorithm to use ("bubble" or "insertion")
        
    Returns:
        list: Sorted list in ascending order
    """
    if algorithm.lower() == "bubble":
        sorted_items, steps = bubble_sort(items)
    elif algorithm.lower() == "insertion":
        sorted_items, steps = insertion_sort(items)
    else:
        raise ValueError("Unsupported algorithm. Choose 'bubble' or 'insertion'")
    
    # Print the steps
    for step in steps:
        print(step)
    
    return sorted_items

# Example usage
if __name__ == "__main__":
    print("Example 1: Sorting numbers with Bubble Sort")
    numbers = [64, 34, 25, 12, 22, 11, 90]
    sorted_numbers = custom_sort(numbers, "bubble")
    print(f"Original list: {numbers}")
    print(f"Sorted list: {sorted_numbers}")
    print("\n" + "-"*50 + "\n")
    
    print("Example 2: Sorting strings with Insertion Sort")
    words = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_words = custom_sort(words, "insertion")
    print(f"Original list: {words}")
    print(f"Sorted list: {sorted_words}")
    print("\n" + "-"*50 + "\n")
    
    # Error handling examples
    try:
        print("Example 3: Error handling - Mixed types")
        mixed = [1, 2, "apple", 4]
        custom_sort(mixed)
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        print("\nExample 4: Error handling - Invalid input type")
        not_a_list = "not a list"
        custom_sort(not_a_list)
    except ValueError as e:
        print(f"Error: {e}")