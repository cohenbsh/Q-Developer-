import unittest
import os
import sys
from unittest.mock import patch, MagicMock
from io import StringIO

# Import the modules to test
import UnsecuritedCodeHardCoded_Cred as db_module
import UnsecuritedCodeMissingValidationOnInput as cmd_module
import UnsecuritedCodeSQL_Injection as sql_module

class TestSecurityImprovements(unittest.TestCase):
    """Test cases for security improvements in the codebase."""
    
    def setUp(self):
        """Set up test environment."""
        # Set up test environment variables
        os.environ["DB_USERNAME"] = "test_user"
        os.environ["DB_PASSWORD"] = "test_password"
        os.environ["DB_NAME"] = "test_db"
        os.environ["DB_HOST"] = "localhost"
        
        # Mock for database connection
        self.db_mock = MagicMock()
        self.cursor_mock = MagicMock()
        
        # Mock for HTTP request
        self.request_mock = MagicMock()
        self.request_mock.GET = {"name": "test_user"}
    
    def test_db_credentials_from_env(self):
        """Test that database credentials are retrieved from environment variables."""
        with patch('mysql.connector.connect') as mock_connect:
            mock_connect.return_value = self.db_mock
            self.db_mock.cursor.return_value = self.cursor_mock
            self.cursor_mock.fetchall.return_value = [("user1",), ("user2",)]
            
            # Call the function that should use environment variables
            try:
                db_module.connect_to_db()
                
                # Check that connect was called with the right parameters
                mock_connect.assert_called_with(
                    host="localhost",
                    user="test_user",
                    password="test_password",
                    database="test_db"
                )
            except Exception as e:
                self.fail(f"connect_to_db() raised {e} unexpectedly!")
    
    def test_command_validation(self):
        """Test that command validation works correctly."""
        # Test allowed commands
        self.assertTrue(cmd_module.validate_command("ls -la"))
        self.assertTrue(cmd_module.validate_command("echo hello"))
        self.assertTrue(cmd_module.validate_command("pwd"))
        
        # Test disallowed commands
        self.assertFalse(cmd_module.validate_command("rm -rf /"))
        self.assertFalse(cmd_module.validate_command("cat /etc/passwd"))
        self.assertFalse(cmd_module.validate_command("; rm -rf /"))
        self.assertFalse(cmd_module.validate_command("sudo reboot"))
    
    def test_sql_injection_prevention(self):
        """Test that SQL injection is prevented using parameterized queries."""
        with patch('django.db.connection') as mock_connection:
            mock_cursor = MagicMock()
            mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
            
            # Test with normal input
            sql_module.find_user("normal_user")
            mock_cursor.execute.assert_called_with(
                "SELECT username FROM USERS WHERE name = %s", 
                ["normal_user"]
            )
            
            # Test with malicious input (SQL injection attempt)
            sql_module.find_user("'; DROP TABLE users; --")
            mock_cursor.execute.assert_called_with(
                "SELECT username FROM USERS WHERE name = %s", 
                ["'; DROP TABLE users; --"]
            )
    
    def test_sqlite_parameterized_query(self):
        """Test that SQLite queries use parameterization."""
        with patch('sqlite3.connect') as mock_connect:
            mock_connection = MagicMock()
            mock_cursor = MagicMock()
            mock_connect.return_value.__enter__.return_value = mock_connection
            mock_connection.cursor.return_value = mock_cursor
            
            # Test with normal input
            sql_module.execute_query(self.request_mock)
            
            # Check that execute was called with parameterized query
            mock_cursor.execute.assert_called_with(
                "SELECT * FROM Users WHERE name = ?;", 
                ("test_user",)
            )
    
    def test_command_execution_safety(self):
        """Test that command execution is done safely."""
        test_input = "ls -la"
        
        # Mock input and subprocess.run
        with patch('builtins.input', return_value=test_input), \
             patch('subprocess.run') as mock_run, \
             patch('sys.stdout', new=StringIO()):
            
            mock_run.return_value = MagicMock(stdout="test output", stderr="")
            
            # Run the command safely function
            cmd_module.run_command_safely()
            
            # Check that subprocess.run was called with the right parameters
            mock_run.assert_called_with(
                ['ls', '-la'],  # Command should be split into args
                shell=False,    # shell should be False for security
                text=True,
                capture_output=True,
                timeout=5
            )

if __name__ == '__main__':
    unittest.main()