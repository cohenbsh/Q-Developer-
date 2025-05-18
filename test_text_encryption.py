"""
Unit tests for the text encryption system.
"""

import unittest
from text_encryption import create_cipher, encrypt, decrypt

class TestTextEncryption(unittest.TestCase):
    
    def setUp(self):
        # Create a cipher for testing
        self.cipher, self.inverse_cipher = create_cipher()
    
    def test_cipher_creation(self):
        """Test that the cipher maps all letters correctly."""
        import string
        all_letters = string.ascii_lowercase + string.ascii_uppercase
        
        # Check that all letters are in the cipher
        for letter in all_letters:
            self.assertIn(letter, self.cipher)
        
        # Check that the cipher maps to all letters
        cipher_values = set(self.cipher.values())
        for letter in all_letters:
            self.assertIn(letter, cipher_values)
        
        # Check that the cipher is a one-to-one mapping
        self.assertEqual(len(self.cipher), len(set(self.cipher.values())))
    
    def test_inverse_cipher(self):
        """Test that the inverse cipher correctly reverses the original cipher."""
        for original, substitution in self.cipher.items():
            self.assertEqual(original, self.inverse_cipher[substitution])
    
    def test_encryption(self):
        """Test that encryption works correctly."""
        message = "Hello, World!"
        encrypted = encrypt(message, self.cipher)
        
        # Check that the encrypted message is the same length
        self.assertEqual(len(message), len(encrypted))
        
        # Check that alphabetic characters are changed
        for i, char in enumerate(message):
            if char.isalpha():
                self.assertNotEqual(char, encrypted[i])
            else:
                self.assertEqual(char, encrypted[i])
    
    def test_decryption(self):
        """Test that decryption correctly reverses encryption."""
        original_messages = [
            "Hello, World!",
            "This is a TEST message with MIXED case.",
            "Special characters: !@#$%^&*()_+-=[]{}|;':\",./<>?",
            "Numbers: 0123456789"
        ]
        
        for message in original_messages:
            encrypted = encrypt(message, self.cipher)
            decrypted = decrypt(encrypted, self.inverse_cipher)
            self.assertEqual(message, decrypted)
    
    def test_empty_message(self):
        """Test handling of empty messages."""
        empty = ""
        encrypted = encrypt(empty, self.cipher)
        self.assertEqual(empty, encrypted)
        
        decrypted = decrypt(encrypted, self.inverse_cipher)
        self.assertEqual(empty, decrypted)

if __name__ == "__main__":
    unittest.main()