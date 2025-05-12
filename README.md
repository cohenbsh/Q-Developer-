# Secure Code Repository

This repository contains examples of secure coding practices that address common security vulnerabilities.

## Security Improvements

The following security improvements have been implemented:

### 1. Removed Hardcoded Credentials
- Replaced hardcoded database credentials with environment variables
- Removed hardcoded AWS credentials
- Added proper credential management using `.env` files and the `python-dotenv` package

### 2. Fixed Command Injection Vulnerability
- Implemented command whitelisting to restrict allowed commands
- Used `shlex.split()` to properly handle command arguments
- Set `shell=False` in subprocess calls to prevent shell injection
- Added proper error handling and timeout for command execution

### 3. Fixed SQL Injection Vulnerabilities
- Replaced string concatenation and formatting with parameterized queries
- Added input validation for query parameters
- Implemented proper error handling for database operations

## Setup Instructions

### Prerequisites
- Python 3.6+
- Required packages: `mysql-connector-python`, `django`, `python-dotenv`

### Installation
1. Clone this repository
2. Install required packages:
   ```
   pip install mysql-connector-python django python-dotenv
   ```

### Configuration
1. Copy the `.env.example` file to `.env`:
   ```
   cp .env.example .env
   ```
2. Edit the `.env` file and add your actual credentials:
   ```
   # Database Configuration
   DB_USERNAME=your_actual_username
   DB_PASSWORD=your_actual_password
   DB_NAME=your_actual_database
   DB_HOST=localhost
   
   # AWS Credentials
   AWS_ACCESS_KEY_ID=your_actual_aws_key
   AWS_SECRET_ACCESS_KEY=your_actual_aws_secret
   ```

## Usage

### Database Connection
```python
from UnsecuritedCodeHardCoded_Cred import connect_to_db

# Connect to the database using environment variables
results = connect_to_db()
```

### Command Execution
```python
from UnsecuritedCodeMissingValidationOnInput import run_command_safely

# Run a command safely with validation
run_command_safely()
```

### Database Queries
```python
from UnsecuritedCodeSQL_Injection import find_user, execute_query

# Find a user securely
user = find_user("john_doe")

# Execute a query securely
results = execute_query(request)
```

## Security Best Practices

1. **Never hardcode credentials** in your source code
2. **Always use environment variables** or secure credential stores
3. **Use parameterized queries** to prevent SQL injection
4. **Validate all user input** before processing
5. **Restrict command execution** to a whitelist of allowed commands
6. **Avoid using `shell=True`** in subprocess calls
7. **Implement proper error handling** to avoid leaking sensitive information
8. **Keep dependencies updated** to address security vulnerabilities
9. **Add `.env` files to `.gitignore`** to prevent accidental credential exposure

## Testing

To test the secure implementations:

1. Set up your environment variables in the `.env` file
2. Run the modules directly to test their functionality
3. Verify that security measures are working as expected