"""
Input validation utility functions.

This module provides functions for validating user input to prevent security vulnerabilities.
"""

def is_all_digits(input_string):
    """
    Validates that all characters in the input string are digits.
    
    Args:
        input_string (str): The string to validate.
        
    Returns:
        bool: True if all characters are digits, False otherwise.
              Returns False for empty strings.
    
    Examples:
        >>> is_all_digits("12345")
        True
        >>> is_all_digits("123a45")
        False
        >>> is_all_digits("")
        False
    """
    if not input_string:  # Check for empty string
        return False
    
    return input_string.isdigit()