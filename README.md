# hashPass
Buiding a Python CLI authentication system demonstrating password hashing, credential verification, and input validation. The user will enter their email and password, the code will compare the enter passwords hash with the stored passwords hash to verify the user. It will also give the user an opportunity to create an account.

Features:
- Password hashing using MD5
- Credential verification for login
- Email format validation with regex
- Account creation for new users


Hashing is the process of converting data into fixed size values (a hash) using a hash function. Even small changes to the input will produce a different hash. This helps us to detect data tampering when we compare the previous and current hashes. Hashing is commonly used for password storage and data integrity verification. 

