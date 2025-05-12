# Secure command execution with input validation
import subprocess
import shlex
import re
import sys

def validate_command(cmd):
    """
    Validates if the command is in the allowed list of safe commands.
    Returns True if command is allowed, False otherwise.
    """
    # Define a list of allowed commands
    allowed_commands = ['ls', 'dir', 'echo', 'pwd', 'whoami', 'date', 'time']
    
    # Extract the base command (first word before any arguments)
    base_cmd = cmd.strip().split()[0] if cmd.strip() else ""
    
    # Check if the base command is in the allowed list
    return base_cmd in allowed_commands

def run_command_safely():
    """
    Safely runs a command after validation.
    """
    print("Enter a command to run (allowed: ls, dir, echo, pwd, whoami, date, time):")
    cmd = input('> ')
    
    if not cmd.strip():
        print("No command entered.")
        return
    
    if validate_command(cmd):
        try:
            # Use shlex.split to properly handle command arguments
            args = shlex.split(cmd)
            
            # Use subprocess.run with shell=False for security
            result = subprocess.run(
                args,
                shell=False,
                text=True,
                capture_output=True,
                timeout=5  # Set a timeout for safety
            )
            
            # Print command output
            print("\nCommand Output:")
            print(result.stdout)
            
            # Print any errors
            if result.stderr:
                print("\nErrors:")
                print(result.stderr)
                
        except subprocess.TimeoutExpired:
            print("Command execution timed out.")
        except subprocess.SubprocessError as e:
            print(f"Error executing command: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    else:
        print(f"Command not allowed for security reasons. Allowed commands: ls, dir, echo, pwd, whoami, date, time")

if __name__ == "__main__":
    run_command_safely()