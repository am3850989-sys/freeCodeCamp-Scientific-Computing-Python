class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum(ord(char) for char in string)

    def add(self, key, value):
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            self.collection[hashed_key][key] = value
        else:
            self.collection[hashed_key] = {key: value}

    def remove(self, key):
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]

    def lookup(self, key):
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            return self.collection[hashed_key].get(key)

        return None

# Test cases
ht = HashTable()
ht.add("name", "Ahmed")
ht.add("age", 25)
print(ht.lookup("name")) # Ahmed
ht.remove("age")
print(ht.lookup("age")) # None

اعملي `Commit changes` وابعتيلي رقم 8 `Tower-Of-Hanoi` نقفله 🔥
