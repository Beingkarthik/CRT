# Hashing defination : Hashing is a technique used to uniquely identify a specific object from a group of similar objects.
#  It is a process of converting an input (or 'message') into a fixed-size string of bytes, typically for security or data management purposes.
#  The output, known as a hash value or hash code, is usually a unique representation of the input data.
# Hashing Advantages:
# 1. Fast Data Retrieval: Hashing allows for quick data retrieval by using a hash function to compute the index of the data in a hash table, 
# enabling constant average time complexity for search
# Hahing mechanism:
# 1. Hash Function: A hash function takes an input (or 'key') and
# produces a fixed-size string of bytes, which is typically a hash code. 
# The hash function should be deterministic, meaning that the same input will always produce the same output.
# 2. Hash Table: A hash table is a data structure that uses a hash function to map keys to values. 
# It consists of an array of buckets or slots, where each bucket can hold one or more key-value pairs.
# Hash key: A hash key is the input to a hash function, which is used to compute the hash code.

# Example of Hashing in Python

# a = 10
# b = 'karthik'
# c = 3.454

# print(hash(a))
# print(hash(b))
# print(hash(c))

# size = 7
# table = [None] * size
# a = [10,20,30]
# for key in a:
#     hash_key = key%size
#     table[hash_key] = key
# print(table)

# Linear Probing: In linear probing, if a collision occurs (i.e., two keys hash to the same index), 
# the algorithm checks the next slot in the array for an empty slot.

# size = 7
# table = [None] * size
# a = [10, 20, 30]
# for key in a:
#     hash_key = key % size
#     while table[hash_key] is not None:
#         hash_key = (hash_key + 1) % size
#     table[hash_key] = key
# print(table)

