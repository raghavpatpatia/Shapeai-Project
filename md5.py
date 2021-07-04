import hashlib

s = input("Enter String: ")
# converts the string into bytes to be acceptable by hash function
output = hashlib.md5(s.encode())
# returns encoded data in byte format
print("Result in byte format:", output.digest())
# returns encoded data in hexadecimal format
print("Result in hexadecimal format:", output.hexdigest())