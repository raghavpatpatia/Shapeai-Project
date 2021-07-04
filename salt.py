import hashlib
import os

s = input("Enter String: ")
s = s.encode()
salt = os.urandom(16)
output = hashlib.pbkdf2_hmac('sha256', s, salt, 100000).hex()
print("Result after adding salt and iterations to hash:", output)