# Least Recently Used Cache

# Caching can be defined as the process of storing data into a temporary data storage
# to avoid recomputation or to avoid reading the data from a relatively slower part of memory again and again.
# Thus cachig serves as a fast "look-up" storage allowing programs to execute faster.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache(object):

    def __init__(self, capacity = 5):
        if capacity < 1:
            print('Capacity must be > 0')
            return None

        # Initialize class variables
        self.hash_map = {}
        self.head = None # head: Node with the most recently used key
        self.tail = None # tail: Node with the least recently used key
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        print(self.head.value, self.tail.value)


    def rearrange(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return
        # if node is head (most recent), nothing to do
        if node is self.head: return
        # if node was tail, set new tail
        if node is self.tail:
            self.tail = self.tail.next
        # and set new head
        node.prev = self.head
        self.head.next = node
        self.head = node


    # Retrieve item from provided key
    def get(self, key):
        if key in self.hash_map:
            self.rearrange(self.hash_map[key])
            return self.hash_map[key].value
        # Return -1 if nonexistent
        if key not in self.hash_map:
            return -1


    def set(self, key, value):
        # If key is present in the cache update node with new value
        if key in self.hash_map:
            self.rearrange(self.hash_map[key])
            self.hash_map[key].value = value
        else:
            # insert new node
            # If the cache is at capacity remove the oldest item
            if self.size == self.capacity:
                print('cache is full item to evict is:', self.tail.key, self.tail.value)
                del self.hash_map[self.tail.key]
                self.tail = self.tail.next
            if self.size < self.capacity:
                 self.size += 1
            node = Node(key, value)
            self.hash_map[key] = node
            self.rearrange(node)
        # self.__str__()


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);



print(our_cache.get(1))
# returns 1
print(our_cache.get(2))
# returns 2
print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
# 5 gets added, no eviction
our_cache.set(6, 6)
# evicts (3,3)
our_cache.set(7, 7)
# evicts (4,4)

print(our_cache.get(3))
# returns -1
print(our_cache.get(6))
# returns 6
print(our_cache.get(1))
# returns 1