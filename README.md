# Problem 1: Least Recently Used Cache

### For the first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit.

The task is to use an appropriate data structure(s) to implement the cache.

- In case of a cache hit, the get() operation should return the appropriate value.
- In case of a cache miss, the get() should return -1.
- While putting an element in the cache, the put() / set() operation must insert the element.
- If the cache is full, the least recently used entry must be removed first and then insert the element.

### All operations must take O(1) time.
### Consider the size of cache = 5.
