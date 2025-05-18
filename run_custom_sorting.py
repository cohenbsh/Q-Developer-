"""
Example usage of the custom sorting algorithms.
"""

from custom_sorting import custom_sort

def separator():
    print("\n" + "-"*50 + "\n")

# Example 1: Sorting numbers with Bubble Sort
print("Example 1: Sorting numbers with Bubble Sort")
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Original list: {numbers}")
sorted_numbers = custom_sort(numbers, "bubble")
print(f"Sorted list: {sorted_numbers}")
separator()

# Example 2: Sorting strings with Insertion Sort
print("Example 2: Sorting strings with Insertion Sort")
words = ["banana", "apple", "cherry", "date", "elderberry"]
print(f"Original list: {words}")
sorted_words = custom_sort(words, "insertion")
print(f"Sorted list: {sorted_words}")
separator()

# Example 3: Sorting a reverse-ordered list
print("Example 3: Sorting a reverse-ordered list with Bubble Sort")
reverse_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(f"Original list: {reverse_list}")
sorted_reverse = custom_sort(reverse_list, "bubble")
print(f"Sorted list: {sorted_reverse}")
separator()

# Example 4: Sorting an already sorted list
print("Example 4: Sorting an already sorted list with Insertion Sort")
sorted_list = [1, 2, 3, 4, 5]
print(f"Original list: {sorted_list}")
still_sorted = custom_sort(sorted_list, "insertion")
print(f"Sorted list: {still_sorted}")
separator()

# Error handling examples
try:
    print("Example 5: Error handling - Mixed types")
    mixed = [1, 2, "apple", 4]
    custom_sort(mixed)
except ValueError as e:
    print(f"Error: {e}")

try:
    print("\nExample 6: Error handling - Invalid input type")
    not_a_list = "not a list"
    custom_sort(not_a_list)
except ValueError as e:
    print(f"Error: {e}")