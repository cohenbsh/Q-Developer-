import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def connect_to_db():
    """
    Connect to database using credentials from environment variables.
    Requires the following environment variables to be set:
    - DB_USERNAME: Database username
    - DB_PASSWORD: Database password
    - DB_NAME: Database name
    - DB_HOST: Database host (defaults to localhost if not set)
    """
    # Get credentials from environment variables
    username = os.environ.get("DB_USERNAME")
    password = os.environ.get("DB_PASSWORD")
    database = os.environ.get("DB_NAME")
    host = os.environ.get("DB_HOST", "localhost")
    
    # Check if required environment variables are set
    if not all([username, password, database]):
        raise EnvironmentError("Database credentials not properly configured. "
                              "Please set DB_USERNAME, DB_PASSWORD, and DB_NAME environment variables.")
    
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Users;")
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        raise
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# For backward compatibility (deprecated)
def connect_to_db_vulnerable():
    """
    DEPRECATED: This function is kept for backward compatibility.
    Please use connect_to_db() instead.
    """
    import warnings
    warnings.warn("Using connect_to_db_vulnerable() is deprecated and insecure. "
                 "Use connect_to_db() instead.", DeprecationWarning, stacklevel=2)
    return connect_to_db()