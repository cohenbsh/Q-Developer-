"""
Password Validator Module

This module provides functions to validate password structure,
specifically checking if passwords consist only of numeric characters.
"""

def validate_numeric_password(password):
    """
    Validates that a password consists only of numeric characters.
    
    Args:
        password (str): The password to validate
        
    Returns:
        bool: True if the password contains only numeric characters, False otherwise
    """
    if not password:
        return False
    
    return password.isdigit()

def validate_password_with_feedback(password):
    """
    Validates a password and provides feedback on why it failed validation.
    
    Args:
        password (str): The password to validate
        
    Returns:
        tuple: (bool, str) - (is_valid, feedback_message)
    """
    if not password:
        return False, "Password cannot be empty"
    
    if not password.isdigit():
        return False, "Password must contain only numeric characters"
    
    return True, "Password is valid"

if __name__ == "__main__":
    # Example usage
    test_passwords = [
        "123456",
        "password123",
        "",
        "abc",
        "123abc",
        "0"
    ]
    
    print("Password Validation Results:")
    print("-" * 40)
    for pwd in test_passwords:
        is_valid, message = validate_password_with_feedback(pwd)
        status = "VALID" if is_valid else "INVALID"
        print(f"Password: '{pwd}' - {status} - {message}")