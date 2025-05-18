# Python Utilities Repository

This repository contains various Python utilities and examples, including:

1. Text Encryption System
2. Custom Sorting Algorithms
3. Security Vulnerability Examples

## Text Encryption System

The `text_encryption.py` module implements a simple text encryption system using a substitution cipher.

### Features:
- Creates a random substitution cipher mapping each letter to a different letter
- Encrypts messages using the generated cipher
- Decrypts encrypted messages
- Preserves non-alphabetic characters
- Handles both uppercase and lowercase letters

### Usage:

```python
from text_encryption import create_cipher, encrypt, decrypt

# Create a cipher
cipher, inverse_cipher = create_cipher()

# Encrypt a message
message = "Hello, World!"
encrypted = encrypt(message, cipher)
print(f"Encrypted: {encrypted}")

# Decrypt the message
decrypted = decrypt(encrypted, inverse_cipher)
print(f"Decrypted: {decrypted}")
```

## Custom Sorting Algorithms

The `custom_sorting.py` module implements custom sorting algorithms without using Python's built-in sort functions.

### Features:
- Bubble Sort implementation
- Insertion Sort implementation
- Handles both numeric and alphabetical sorting
- Includes error handling for invalid inputs
- Shows step-by-step sorting process

### Usage:

```python
from custom_sorting import custom_sort

# Sort a list of numbers using bubble sort
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = custom_sort(numbers, "bubble")
print(f"Sorted numbers: {sorted_numbers}")

# Sort a list of strings using insertion sort
words = ["banana", "apple", "cherry", "date"]
sorted_words = custom_sort(words, "insertion")
print(f"Sorted words: {sorted_words}")
```

## Testing

Unit tests are provided for both the text encryption system and custom sorting algorithms:

- `test_text_encryption.py`: Tests for the text encryption system
- `test_custom_sorting.py`: Tests for the custom sorting algorithms

To run the tests:

```bash
python -m unittest test_text_encryption.py
python -m unittest test_custom_sorting.py
```

## Security Vulnerability Examples

The repository also includes examples of common security vulnerabilities:

- `UnsecuritedCodeHardCoded_Cred.py`: Example of hardcoded credentials
- `UnsecuritedCodeMissingValidationOnInput.py`: Example of missing input validation
- `UnsecuritedCodeSQL_Injection.py`: Example of SQL injection vulnerability

These files are provided for educational purposes to demonstrate common security issues in code.