"""
Tests for input validation functions.
"""

import unittest
from input_validation import is_all_digits

class TestInputValidation(unittest.TestCase):
    
    def test_is_all_digits_with_digits(self):
        """Test is_all_digits with strings containing only digits."""
        self.assertTrue(is_all_digits("0"))
        self.assertTrue(is_all_digits("123"))
        self.assertTrue(is_all_digits("9876543210"))
    
    def test_is_all_digits_with_non_digits(self):
        """Test is_all_digits with strings containing non-digit characters."""
        self.assertFalse(is_all_digits("123a"))
        self.assertFalse(is_all_digits("a123"))
        self.assertFalse(is_all_digits("12 34"))
        self.assertFalse(is_all_digits("12.34"))
        self.assertFalse(is_all_digits("12-34"))
        self.assertFalse(is_all_digits("abc"))
    
    def test_is_all_digits_with_empty_string(self):
        """Test is_all_digits with an empty string."""
        self.assertFalse(is_all_digits(""))
    
    def test_is_all_digits_with_special_cases(self):
        """Test is_all_digits with special cases."""
        # Unicode digits should also work
        self.assertTrue(is_all_digits("١٢٣٤٥"))  # Arabic digits
        
        # Negative numbers (with minus sign) should return False
        self.assertFalse(is_all_digits("-123"))
        
        # Spaces only should return False
        self.assertFalse(is_all_digits(" "))

if __name__ == "__main__":
    unittest.main()