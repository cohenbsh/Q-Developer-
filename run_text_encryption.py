"""
Example usage of the text encryption system.
"""

from text_encryption import create_cipher, encrypt, decrypt

# Create a cipher
cipher, inverse_cipher = create_cipher()

# Display the cipher mapping for demonstration
print("Cipher Mapping (first 10 letters):")
for i, (original, substitution) in enumerate(sorted(cipher.items())):
    print(f"{original} -> {substitution}")
    if i >= 9:
        print("...")
        break

# Example messages
messages = [
    "Hello, World!",
    "This is a SECRET message with MIXED case.",
    "Special characters: !@#$%^&*()_+-=[]{}|;':\",./<>?",
    "Numbers: 0123456789"
]

# Test each message
for i, message in enumerate(messages):
    print(f"\nTest {i+1}:")
    print(f"Original: {message}")
    
    # Encrypt the message
    encrypted = encrypt(message, cipher)
    print(f"Encrypted: {encrypted}")
    
    # Decrypt the message
    decrypted = decrypt(encrypted, inverse_cipher)
    print(f"Decrypted: {decrypted}")
    
    # Verify the decryption worked correctly
    assert message == decrypted, "Decryption failed!"
    print("✓ Encryption and decryption successful!")

print("\nAll tests passed successfully!")