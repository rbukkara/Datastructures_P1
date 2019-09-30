from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity):
        if capacity <= 0:
            print("Object initialization error")
            return

        self.capacity = capacity
        self.values = OrderedDict()

    def get(self, key):
        if self.values is None:
            print("Object initialization error")
            return

        if key in self.values:
            self.values.move_to_end(key)
            return self.values[key]

        return -1

    def set(self, key, value):

        if self.values is None:
            print("Object initialization error")
            return

        self.values[key] = value
        self.values.move_to_end(key)
        if self.capacity < len(self.values):
            self.values.popitem(False)

    def printkeys(self):

        if self.values is None:
            print("Object initialization error")
            return
        print(self.values)


our_cache = LRU_Cache(5)
our_cache.printkeys()

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print("added 1, 2, 3, 4")
our_cache.printkeys()

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)
# print("set 5,6")

our_cache.printkeys()

print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
#print("retrieved 3")

our_cache.printkeys()

our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1))
# should return 10
print(our_cache.get(2))

our_cache.set(4, 20)
print(our_cache.get(4))

our_cache.printkeys()

our_cache = LRU_Cache(0)
#our_cache.printkeys()

