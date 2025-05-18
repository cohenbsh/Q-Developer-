"""
Unit tests for the custom sorting algorithms.
"""

import unittest
from custom_sorting import bubble_sort, insertion_sort, validate_input

class TestCustomSorting(unittest.TestCase):
    
    def test_validate_input(self):
        """Test input validation function."""
        # Valid inputs
        self.assertEqual(validate_input([1, 2, 3]), (True, None))
        self.assertEqual(validate_input([1.1, 2.2, 3.3]), (True, None))
        self.assertEqual(validate_input(["a", "b", "c"]), (True, None))
        self.assertEqual(validate_input([]), (True, None))
        
        # Invalid inputs
        self.assertEqual(validate_input("not a list"), (False, "Input must be a list"))
        self.assertEqual(validate_input([1, "a"]), (False, "Cannot mix strings and numbers in the same list"))
        self.assertEqual(validate_input([1, [2]]), (False, "List elements must be numbers or strings"))
    
    def test_bubble_sort_numbers(self):
        """Test bubble sort with numeric lists."""
        # Test with integers
        unsorted = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        sorted_list, _ = bubble_sort(unsorted)
        self.assertEqual(sorted_list, expected)
        
        # Test with floats
        unsorted = [3.3, 1.1, 2.2]
        expected = [1.1, 2.2, 3.3]
        sorted_list, _ = bubble_sort(unsorted)
        self.assertEqual(sorted_list, expected)
        
        # Test with negative numbers
        unsorted = [5, -10, 0, 3, -5]
        expected = [-10, -5, 0, 3, 5]
        sorted_list, _ = bubble_sort(unsorted)
        self.assertEqual(sorted_list, expected)
    
    def test_bubble_sort_strings(self):
        """Test bubble sort with string lists."""
        unsorted = ["banana", "apple", "cherry", "date"]
        expected = ["apple", "banana", "cherry", "date"]
        sorted_list, _ = bubble_sort(unsorted)
        self.assertEqual(sorted_list, expected)
        
        # Test with mixed case
        unsorted = ["Banana", "apple", "Cherry", "date"]
        expected = ["Banana", "Cherry", "apple", "date"]  # Capital letters come before lowercase in ASCII
        sorted_list, _ = bubble_sort(unsorted)
        self.assertEqual(sorted_list, expected)
    
    def test_insertion_sort_numbers(self):
        """Test insertion sort with numeric lists."""
        # Test with integers
        unsorted = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        sorted_list, _ = insertion_sort(unsorted)
        self.assertEqual(sorted_list, expected)
        
        # Test with floats
        unsorted = [3.3, 1.1, 2.2]
        expected = [1.1, 2.2, 3.3]
        sorted_list, _ = insertion_sort(unsorted)
        self.assertEqual(sorted_list, expected)
        
        # Test with negative numbers
        unsorted = [5, -10, 0, 3, -5]
        expected = [-10, -5, 0, 3, 5]
        sorted_list, _ = insertion_sort(unsorted)
        self.assertEqual(sorted_list, expected)
    
    def test_insertion_sort_strings(self):
        """Test insertion sort with string lists."""
        unsorted = ["banana", "apple", "cherry", "date"]
        expected = ["apple", "banana", "cherry", "date"]
        sorted_list, _ = insertion_sort(unsorted)
        self.assertEqual(sorted_list, expected)
        
        # Test with mixed case
        unsorted = ["Banana", "apple", "Cherry", "date"]
        expected = ["Banana", "Cherry", "apple", "date"]  # Capital letters come before lowercase in ASCII
        sorted_list, _ = insertion_sort(unsorted)
        self.assertEqual(sorted_list, expected)
    
    def test_edge_cases(self):
        """Test edge cases for both sorting algorithms."""
        # Empty list
        self.assertEqual(bubble_sort([]), ([], ["Initial list: []", "List is already sorted"]))
        self.assertEqual(insertion_sort([]), ([], ["Initial list: []", "List is already sorted"]))
        
        # Single element list
        self.assertEqual(bubble_sort([1])[0], [1])
        self.assertEqual(insertion_sort([1])[0], [1])
        
        # Already sorted list
        self.assertEqual(bubble_sort([1, 2, 3])[0], [1, 2, 3])
        self.assertEqual(insertion_sort([1, 2, 3])[0], [1, 2, 3])
        
        # Reverse sorted list
        self.assertEqual(bubble_sort([3, 2, 1])[0], [1, 2, 3])
        self.assertEqual(insertion_sort([3, 2, 1])[0], [1, 2, 3])
    
    def test_error_handling(self):
        """Test error handling for invalid inputs."""
        with self.assertRaises(ValueError):
            bubble_sort("not a list")
        
        with self.assertRaises(ValueError):
            insertion_sort([1, "a"])
        
        with self.assertRaises(ValueError):
            bubble_sort([1, [2]])
        
        with self.assertRaises(ValueError):
            insertion_sort([1, None])

if __name__ == "__main__":
    unittest.main()