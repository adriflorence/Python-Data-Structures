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

    def __init__(self, capacity):
        if capacity < 1:
            print('Capacity must be > 0')
            return None
        # Initialize class variables
        # tail: Node with the least recently used key
        # head: Node with the most recently used key
        self.hash_map = {}
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        for key in self.hash_map:
            print(key)
            for value in self.hash_map[key]:
                print(self.hash_map[key][value])
    
    def use(self, node):

        # head node is most recent, nothing to do
        if node is self.head: return



    # Retrieve item from provided key.
    def get(self, key):
        
        # Return -1 if nonexistent. 
        if key not in self.hash_map:
            return -1
        
        node = self.hash_map[key]
        # if self.head == node:
        #     return node.value

        return self.hash_map[key].value

    def set(self, key, value):
        # If key is present in the cache update node with new value
        if key in self.hash_map:
            self.hash_map[key].value = value
        else:
            node = Node(key, value)

            # if self.size < self.capacity:
            #     self.size += 1

            # # If the cache is at capacity remove the oldest item
            # elif self.size == self.capacity:
            #     current_tail_key = self.tail.key

            self.hash_map[key] = node


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

our_cache.__str__()


# our_cache.get(1)       # returns 1
# our_cache.get(2)       # returns 2
# our_cache.get(9)      # returns -1 because 9 is not present in the cache

# our_cache.set(5, 5) 
# our_cache.set(6, 6)

# our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
