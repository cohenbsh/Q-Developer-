"""
Text Encryption System

This module implements a simple text encryption system using a substitution cipher.
It randomly maps each letter of the alphabet to a different letter and provides
functions for encryption and decryption.
"""

import random
import string

def create_cipher():
    """
    Creates a substitution cipher by randomly mapping each letter of the alphabet
    to a different letter.
    
    Returns:
        dict: A dictionary mapping each letter to its substitution
        dict: The inverse mapping for decryption
    """
    # Get all lowercase and uppercase letters
    all_letters = string.ascii_lowercase + string.ascii_uppercase
    
    # Create a list of all letters and shuffle it
    substitution_letters = list(all_letters)
    random.shuffle(substitution_letters)
    
    # Create the cipher mapping
    cipher = {}
    for i, letter in enumerate(all_letters):
        cipher[letter] = substitution_letters[i]
    
    # Create the inverse mapping for decryption
    inverse_cipher = {v: k for k, v in cipher.items()}
    
    return cipher, inverse_cipher

def encrypt(message, cipher):
    """
    Encrypts a message using the provided cipher.
    
    Args:
        message (str): The plain text message to encrypt
        cipher (dict): The substitution cipher mapping
        
    Returns:
        str: The encrypted message
    """
    encrypted_message = ""
    
    for char in message:
        # Replace only alphabetic characters, leave others unchanged
        if char in cipher:
            encrypted_message += cipher[char]
        else:
            encrypted_message += char
            
    return encrypted_message

def decrypt(encrypted_message, inverse_cipher):
    """
    Decrypts an encrypted message using the provided inverse cipher.
    
    Args:
        encrypted_message (str): The encrypted message
        inverse_cipher (dict): The inverse of the substitution cipher mapping
        
    Returns:
        str: The decrypted message
    """
    decrypted_message = ""
    
    for char in encrypted_message:
        # Replace only alphabetic characters, leave others unchanged
        if char in inverse_cipher:
            decrypted_message += inverse_cipher[char]
        else:
            decrypted_message += char
            
    return decrypted_message

# Example usage
if __name__ == "__main__":
    # Create a cipher
    cipher, inverse_cipher = create_cipher()
    
    # Display the cipher mapping for demonstration
    print("Cipher Mapping:")
    for original, substitution in sorted(cipher.items()):
        print(f"{original} -> {substitution}")
    
    # Example message
    original_message = "Hello, World! This is a secret message."
    print(f"\nOriginal message: {original_message}")
    
    # Encrypt the message
    encrypted = encrypt(original_message, cipher)
    print(f"Encrypted message: {encrypted}")
    
    # Decrypt the message
    decrypted = decrypt(encrypted, inverse_cipher)
    print(f"Decrypted message: {decrypted}")
    
    # Verify the decryption worked correctly
    assert original_message == decrypted, "Decryption failed!"
    print("Encryption and decryption successful!")