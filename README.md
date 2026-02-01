# hashPass
Buiding a Python CLI authentication system demonstrating password hashing, credential verification, and input validation. The user will enter their email and password, the code will compare the enter passwords hash with the stored passwords hash to verify the user. It will also give the user an opportunity to create an account.

Features:
- Password hashing using MD5
- Credential verification for login
- Email format validation with regex
- Account creation for new users


Hashing is the process of converting data into fixed size values (a hash) using a hash function. Even small changes to the input will produce a different hash. This helps us to detect data tampering when we compare the previous and current hashes. Hashing is commonly used for password storage and data integrity verification. 

One common hashing algorithm is **MD5 (Message Digest Algorithm 5)**, which generates a 128-bit hash value. However, MD5 has limited unique values, which can lead to collisions (when two different inputs produce the same hash). Because of these vulnerabilities, it is not recommended for security critical applications.  I orginally started out using MD5 [hashPashMD5](hashPashMD5) in my code because thats what i learned in class, but i looked more into the hashlib (https://docs.python.org/3/library/hashlib.html) and chose a safe verision. 

A stronger and more secure algorithm is **SHA256 (Secure Hash Algorithm)**, which generates a 256-bit hash value. The longer hash digest increases security and makes it much harder to produce collisions, enhancing the overall strength of the hash.  

To illustrate the differnece bellow i pasted my test case dictionary. The first value used MD5 algorithm and the second used SHA256.

db={'b@gmail.com': '202cb962ac59075b964b07152d234b70','a@gmail.com': 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'}
