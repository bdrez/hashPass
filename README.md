# hashPass
Building a Python CLI authentication system demonstrating password storage and hashing, credential verification, and input validation. This project uses PBKDF2-HMAC-SHA256 with salt for every user to securely hash their password and store their credentials using presistenet file based storage. Users can create account or log in by enetering their email and password, which are verified against stored hashed credentials. 

# Features:
- Account creation and login
- Password hashing with salt and PBDKF2-HMAC-SHA256
- Random salt generating per user
- Credential verification
- Regex email validation
- Persistent file based storage
- Hidden password input using getpass
- Limited login attempts

# Security concepts
Hashing is the process of converting data into fixed size values (a hash) using a hash function. Even small changes to the input will produce a different hash. This helps us to detect data tampering when we compare the previous and current hashes. Hashing is commonly used for password storage and data integrity verification. 

One common hashing algorithm is **MD5 (Message Digest Algorithm 5)**, which generates a 128-bit hash value. However, MD5 has limited unique values, which can lead to collisions (when two different inputs produce the same hash). Because of these vulnerabilities, it is not recommended for security critical applications.  I originally started out using MD5 [hashPashMD5](hashPashMD5) Verision 1/hashPassMD5.py in my code because thats what i learned in class, but i looked more into the hashlib (https://docs.python.org/3/library/hashlib.html) and chose a safer version. 

A stronger and more secure algorithm is **PBKDF2-HMAC-SHA256**, this combinds a password with a salt and hashes it using SHA256 hundreds of thousands of times. The **SHA256** generates a 256-bit hash value. The longer hash digest increases security and makes it much harder to produce collisions, enhancing the overall strength of the hash.  

# Example Hash Output
To illustrate the difference I pasted my test case dictionary below. Both values are the hashed version of '123'. The first value used the MD5 algorithm and the second value used the SHA256.

db={'keyMD5': '202cb962ac59075b964b07152d234b70', 'keySHA':'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'}

# Current Database Storage Format

The current database format stores:
- the user's email
- a randomly generated salt
- the PBKDF2-HMAC-SHA256 password hash generated using the password and salt

Example:

email              salt                              hash

b@gmail.com              b31b8737a83b3aaffab511ae58c281d7 2f2627c998d2b6e341b29bbf4d1b936e774b5e6d0b45724b582bc435391f1346
