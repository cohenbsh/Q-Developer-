# Secure implementation with parameterized queries and no hardcoded credentials
import os
from django.db import connection
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# AWS credentials should be stored in environment variables or AWS credential providers
# Example of how to access them (but not hardcoded):
# aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
# aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

def find_user(username):
    """
    Securely find a user by username using parameterized queries.
    
    Args:
        username (str): The username to search for
        
    Returns:
        The user record or None if not found
    """
    with connection.cursor() as cur:
        # Use parameterized query to prevent SQL injection
        cur.execute("SELECT username FROM USERS WHERE name = %s", [username])
        output = cur.fetchone()
    return output

def execute_query(request):
    """
    Securely execute a query using parameterized queries.
    
    Args:
        request: The HTTP request object containing the name parameter
        
    Returns:
        Query results
    """
    import sqlite3
    
    # Get the name parameter from the request
    name = request.GET.get("name")
    
    # Input validation
    if not name or not isinstance(name, str):
        return {"error": "Invalid name parameter"}
    
    try:
        with sqlite3.connect("example.db") as connection:
            cursor = connection.cursor()
            
            # Use parameterized query to prevent SQL injection
            query = "SELECT * FROM Users WHERE name = ?;"
            cursor.execute(query, (name,))
            
            # Fetch results
            results = cursor.fetchall()
            return results
            
    except sqlite3.Error as e:
        # Log the error (in a production environment)
        print(f"Database error: {e}")
        return {"error": "Database error occurred"}
    except Exception as e:
        # Log the error (in a production environment)
        print(f"Unexpected error: {e}")
        return {"error": "An unexpected error occurred"}

# Keep the old function for backward compatibility but mark it as deprecated
def execute_query_noncompliant(request):
    """
    DEPRECATED: This function is insecure and should not be used.
    Use execute_query() instead.
    """
    import warnings
    warnings.warn(
        "execute_query_noncompliant() contains SQL injection vulnerabilities. "
        "Use execute_query() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    return execute_query(request)
