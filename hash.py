import hashlib

s = input("Enter String: ")
algo1 = hashlib.sha224(s.encode()).hexdigest()
algo2 = hashlib.new('sha512_256', s.encode()).hexdigest()
algo3 = hashlib.blake2b(s.encode()).hexdigest()
print("Result from algorithm-1 using SHA224:", algo1)
print("Result from algorithm-2 using new and SHA512/256:", algo2)
print("Result from algorithm-3 using blake2b:", algo3)