# Hash Table

This project implements a custom Hash Table data structure in Python.

## Description
The HashTable class uses a simple hashing function that sums the ASCII values of characters in a key.
It handles collisions by storing multiple key-value pairs in a nested dictionary at the same hashed index.

## Methods
- `add(key, value)`: Adds a key-value pair to the hash table
- `lookup(key)`: Returns the value for a given key, or None if not found
- `remove(key)`: Removes a key-value pair from the hash table
- `hash(string)`: Internal hashing function

## How to Run
Run `main.py` to test the hash table functionality.
