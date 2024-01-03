import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for seed in range(self.hash_count):
            print(mmh3.hash(item, seed))
            index = mmh3.hash(item, seed) % self.size
            self.bit_array[index] = 1

    def __contains__(self, item):
        for seed in range(self.hash_count):
            index = mmh3.hash(item, seed) % self.size
            if self.bit_array[index] == 0:
                return False
        return True

# Example usage
bf = BloomFilter(size=100, hash_count=3)

# Add elements to the Bloom filter
bf.add("xyz@gmail.com")
bf.add("abcd@gmail.com")
bf.add("xyz@gmail.com")

# Check for membership
print("xyz@gmail.com" in bf)
print("grape" in bf)
