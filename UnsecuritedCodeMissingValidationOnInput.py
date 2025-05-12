# Example of input validation for commands
import subprocess
from input_validation import is_all_digits

def run_command_with_validation():
    """
    Demonstrates how to use input validation before executing commands.
    This example shows validation for a numeric input scenario.
    """
    # Example: User is only allowed to enter a numeric ID to look up
    user_id = input('Enter user ID (numbers only): ')
    
    # Validate that the input contains only digits
    if not is_all_digits(user_id):
        print("Error: User ID must contain only digits.")
        return
    
    # Now we can safely use the validated input
    # For example, to look up a user by ID in a database
    print(f"Looking up user with ID: {user_id}")
    
    # This is still not completely secure for arbitrary commands,
    # but demonstrates the use of the validation function
    # In a real application, you would use parameterized queries or other secure methods

# Example of the original vulnerable code (commented out)
# cmd = input('Enter a command to run: ')
# subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE)

if __name__ == "__main__":
    run_command_with_validation()