# Input Validation Utilities

This repository contains examples of insecure code patterns and demonstrates how to improve security through proper input validation.

## New Features

### Digit Validation Function

A new function has been implemented to validate that all characters in a string are digits:

```python
from input_validation import is_all_digits

# Returns True if all characters are digits
is_all_digits("12345")  # True

# Returns False if any character is not a digit
is_all_digits("123a45")  # False

# Returns False for empty strings
is_all_digits("")  # False
```

## Usage Examples

### Validating User IDs

```python
from input_validation import is_all_digits

user_id = input("Enter user ID: ")
if not is_all_digits(user_id):
    print("Error: User ID must contain only digits")
else:
    # Proceed with using the validated input
    print(f"Looking up user with ID: {user_id}")
```

### Preventing SQL Injection

When dealing with numeric IDs in database queries, you can use the validation function to ensure that the input contains only digits:

```python
from input_validation import is_all_digits
import sqlite3

def find_user_by_id(user_id):
    if not is_all_digits(user_id):
        return None
    
    with sqlite3.connect("example.db") as connection:
        cursor = connection.cursor()
        # Even with validation, still use parameterized queries
        cursor.execute("SELECT * FROM Users WHERE id = ?", (user_id,))
        return cursor.fetchone()
```

## Testing

Run the tests to verify the functionality of the validation function:

```
python -m unittest test_input_validation.py
```

## Security Notes

- Input validation is just one layer of defense. Always use additional security measures like:
  - Parameterized queries for database operations
  - Proper error handling
  - Least privilege principles
  - Environment variables for credentials instead of hardcoding

- The `is_all_digits` function is particularly useful for validating:
  - User IDs
  - Phone numbers
  - Numeric codes
  - ZIP/Postal codes (numeric only)