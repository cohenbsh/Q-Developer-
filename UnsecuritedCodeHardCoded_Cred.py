import mysql.connector

#Hardcoded Credentials Challenge

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

def connect_to_db_vulnerable():
    # Hardcoded credentials (Not Recommended)
    username = "dbuser"
    password = "password123"
    database = "my_database"

    connection = mysql.connector.connect(
        host="localhost",
        user=username,
        password=password,
        database=database
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users;")
    connection.close()

def connect_to_db_with_validation(username, password, database):
    """
    Connects to the database after validating that the password is numeric.
    
    Args:
        username (str): Database username
        password (str): Database password
        database (str): Database name
        
    Returns:
        bool: True if connection was successful, False if password validation failed
    """
    if not validate_numeric_password(password):
        print("Error: Password must contain only numeric characters")
        return False
    
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database=database
        )
        
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Users;")
        connection.close()
        return True
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return False