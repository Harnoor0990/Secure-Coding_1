import os
import pymysql
from urllib.request import urlopen

# VULNERABILITY 1: Hardcoded Credential
# OWASP Category: A07:2021 – Identification and Authentication Failures
# Issue: Database password is hardcoded in plain text, exposing credentials
# Fix: Use environment variables (e.g., os.getenv('DB_PASSWORD'))

db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}

def get_user_input():
    # VULNERABILITY 2: No Input Validation
    # OWASP Category: A03:2021 – Injection
    # Issue: No validation or sanitization of user input
    # Fix: Validate and sanitize input (e.g., check for allowed characters, length limits)
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    # VULNERABILITY 3: Command Injection
    # OWASP Category: A03:2021 – Injection
    # Issue: User input passed directly to system command without sanitization
    # Fix: Use subprocess module with argument lists, or email libraries like smtplib
    os.system(f'echo {body} | mail -s "{subject}" {to}')

def get_data():
    # VULNERABILITY 4: Insecure HTTP Connection
    # OWASP Category: A02:2021 – Cryptographic Failures
    # Issue: Using HTTP instead of HTTPS, data transmitted without encryption
    # Fix: Change to HTTPS URL to ensure encrypted communication
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    # VULNERABILITY 5: SQL Injection
    # OWASP Category: A03:2021 – Injection
    # Issue: User input directly concatenated into SQL query allowing SQL injection attacks
    # Fix: Use parameterized queries (e.g., cursor.execute("INSERT INTO mytable VALUES (%s, %s)", (data, 'Another Value')))
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
