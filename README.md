# HashPass 🔐

A Python CLI authentication system demonstrating secure password storage, credential verification, database management, and input validation.

This project implements secure password storage using **PBKDF2-HMAC-SHA256** with a unique random salt generated for every user. Instead of storing plaintext passwords, the application stores password hashes and salts in a **SQLite database** and verifies users by hashing entered credentials and comparing the generated hash with the stored value.

The project demonstrates core cybersecurity concepts including password hashing, salting, secure authentication workflows, SQL parameterized queries, and defensive input validation.

---

# Features

* Account creation and user authentication
* Password hashing using PBKDF2-HMAC-SHA256
* Unique random salt generation for every user
* Secure password verification
* Password complexity validation
* Regex-based email validation
* SQLite database storage
* Parameterized SQL queries to prevent SQL injection
* Hidden password input using Python's `getpass` module
* Limited login attempts to reduce brute-force attacks

---

# Technologies Used

* Python
* SQLite3
* hashlib
* secrets
* getpass
* Regular Expressions (Regex)

---

# Security Concepts

## Password Hashing

Hashing converts input data into a fixed-length output called a hash using a cryptographic algorithm. Unlike encryption, hashing is a one-way process, meaning the original data cannot be directly recovered from the hash.

Applications should never store plaintext passwords. Instead, they store password hashes and verify users by hashing the password entered during login and comparing it against the stored hash.

---

# Evolution of Hashing Algorithms

An earlier version of this project used **MD5 (Message Digest Algorithm 5)** because it was introduced during coursework. However, after researching modern password storage practices, the project was upgraded to use **PBKDF2-HMAC-SHA256**, which provides stronger protection against password cracking attacks.

MD5 generates a 128-bit hash but is considered insecure for password storage due to collision vulnerabilities and its fast computation speed, which allows attackers to perform brute-force attacks more efficiently.

PBKDF2-HMAC-SHA256 improves security by:

* Combining the password with a unique random salt
* Applying SHA256 hashing repeatedly for a configured number of iterations
* Increasing the computational cost of password guessing attacks

The salt ensures that identical passwords produce different hashes and helps protect against precomputed attacks such as rainbow tables.

---

# Database Security

User authentication data is stored in a SQLite database with the following structure:

| Column | Description                               |
| ------ | ----------------------------------------- |
| email  | User identifier                           |
| salt   | Unique random salt generated for the user |
| hash   | PBKDF2-HMAC-SHA256 password hash          |

The application uses parameterized SQL queries:

```python
cursor.execute(
    "SELECT * FROM user WHERE email=?",
    (email,)
)
```

Parameterized queries separate user input from SQL commands, reducing the risk of SQL injection attacks.

---

# Example Hash Output

The following demonstrates the difference between traditional hashing algorithms:

```python
db = {
    'keyMD5': '202cb962ac59075b964b07152d234b70',
    'keySHA': 'a665a45920422f9d4174867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'
}
```

---

# Authentication Flow

## Account Creation

1. User enters an email address and password.
2. Email format is validated using regular expressions.
3. Password complexity requirements are checked.
4. A unique random salt is generated.
5. The password and salt are processed using PBKDF2-HMAC-SHA256.
6. The email, salt, and password hash are stored in SQLite.

---

## Login

1. User enters email and password.
2. The application retrieves the stored salt and password hash.
3. The entered password is hashed using the stored salt.
4. The generated hash is compared with the stored password hash.
5. Access is granted if the hashes match.

---

# Future Improvements

* Implement account lockout timers using database timestamps
* Add security event logging
* Implement multi-factor authentication (MFA)
* Add password reset functionality

---

