# hashPass
Building a Python CLI authentication system demonstrating secure password storage, credential verification, and input validation.

This project implements password hashing using PBKDF2-HMAC-SHA256 with a unique random salt for each  user. User credentials are stored using persistent file based storage, allowing users to create accounts and securely authenticate by verifying entered credentials against stored password hashes.  

## Features:
- Account creation and user authentication
- Password hashing using PBKDF2-HMAC-SHA256
- Unique random salt generation for every user
- Secure password verification
- Password complexity validation
- Regex based email validation
- Persistent file based storage
- Hidden password input using getpass module
- Limited login attempts


# Security concepts

## Password hashing
Hashing is the process of converting data into a fixed-size output called a hash using a cryptographic hash function. Changing even one character in an input will produce a completely different hash. Unlike encryption, hashing is a one-way process, meaning the original data cannot be directly recovered from the hash.

Hashing is commonly used for password storage because applications should not store users' plaintext passwords. Instead, they store a hash and compare newly generated hashes during authentication.

## Evolution of Hashing Algorithms 

One common hashing algorithm is **MD5 (Message Digest Algorithm 5)**, which generates a 128-bit hash value. However, MD5 has limited unique values, which can lead to collisions (when two different inputs produce the same hash). Because of these vulnerabilities, it is not recommended for security critical applications.  I originally started out using MD5 [hashPassMD5](Verision%1/hashPassMD5.py) in my code because thats what i learned in class, but i looked more into the hashlib (https://docs.python.org/3/library/hashlib.html) and chose a safer version. 

A stronger and more secure approach is **PBKDF2-HMAC-SHA256**. PBKDF2 combines a password with a unique salt and repeatedly applies SHA256 hashing for a configured number of iterations to create a derived key. The repeated hashing process increases the computational cost of password guessing attacks, making brute-force attacks more difficult.

The salt prevents identical passwords from producing identical hashes and increases resistance against precomputed attacks such as rainbow tables.

# Example Hash Output
The following demonstrates the difference between MD5 and SHA256 hashing.

Both values represent the hashed version of `"123"`:

```python
db={
'keyMD5': '202cb962ac59075b964b07152d234b70',
'keySHA':'a665a45920422f9d4174867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'
}
```

# Authentication Flow

## Account Creation

1. User enters email and password.
2. Password is checked against password complexity requirements.
3. A random salt is generated.
4. The password and salt are passed through PBKDF2-HMAC-SHA256.
5. The salt and generated hash are stored.

## Login

1. User enters email and password.
2. The stored salt is retrieved.
3. The entered password is hashed using the stored salt.
4. The generated hash is compared with the stored password hash.
5. Access is granted if the hashes match.

# Future Improvements

- Migrate file-based storage to SQLite database (In Progress)
- Add security event logging
- Implement account lockout timers
- Implement multi-factor authentication (MFA)
