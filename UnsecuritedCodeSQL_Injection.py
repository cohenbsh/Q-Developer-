# Showing sql injection and credential issue. 
aws_access_key_id=324153454123423;
aws_secret_access_key=324153454123423;

from django.db import connection
from input_validation import is_all_digits

def find_user(username):
    with connection.cursor() as cur:
        cur.execute(f"""select username from USERS where name = '%s'""" % username)
        output = cur.fetchone()
    return output

def execute_query_noncompliant(request):
    import sqlite3
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    with sqlite3.connect("example.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

# New function that uses digit validation for user ID lookups
def find_user_by_id_secure(user_id):
    """
    Securely find a user by ID by validating that the ID contains only digits.
    
    Args:
        user_id (str): The user ID to look up
        
    Returns:
        The user data or None if validation fails
    """
    # First validate that the user_id contains only digits
    if not is_all_digits(user_id):
        print("Error: User ID must contain only digits")
        return None
    
    # Now we can safely use the ID in a query
    # Note: Even with digit validation, using parameterized queries is still best practice
    import sqlite3
    with sqlite3.connect("example.db") as connection:
        cursor = connection.cursor()
        # Using parameterized query for additional security
        cursor.execute("SELECT * FROM Users WHERE id = ?", (user_id,))
        return cursor.fetchone()
