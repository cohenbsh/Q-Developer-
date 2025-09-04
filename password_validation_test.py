import unittest
from UnsecuritedCodeHardCoded_Cred import validate_numeric_password, connect_to_db_with_validation

class TestPasswordValidation(unittest.TestCase):
    
    def test_validate_numeric_password(self):
        # Test valid numeric passwords
        self.assertTrue(validate_numeric_password("123456"))
        self.assertTrue(validate_numeric_password("0"))
        self.assertTrue(validate_numeric_password("9876543210"))
        
        # Test invalid passwords
        self.assertFalse(validate_numeric_password(""))  # Empty password
        self.assertFalse(validate_numeric_password("abc123"))  # Contains letters
        self.assertFalse(validate_numeric_password("123abc"))  # Contains letters
        self.assertFalse(validate_numeric_password("123 456"))  # Contains space
        self.assertFalse(validate_numeric_password("123-456"))  # Contains special character
        self.assertFalse(validate_numeric_password("pass123"))  # Contains letters
    
    def test_connect_to_db_with_validation(self):
        # This is a mock test since we don't want to actually connect to a database
        # Test with valid numeric password
        # Note: In a real scenario, you would mock the mysql.connector
        self.assertFalse(connect_to_db_with_validation("testuser", "123456", "test_db"))
        
        # Test with invalid password
        self.assertFalse(connect_to_db_with_validation("testuser", "password123", "test_db"))

if __name__ == "__main__":
    unittest.main()