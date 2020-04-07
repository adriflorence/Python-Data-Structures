# Problem 1: Least Recently Used Cache

For the first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit.

The task is to use an appropriate data structure(s) to implement the cache.

- In case of a cache hit, the get() operation should return the appropriate value.
- In case of a cache miss, the get() should return -1.
- While putting an element in the cache, the put() / set() operation must insert the element.
- If the cache is full, the least recently used entry must be removed first and then insert the element.

- All operations must take O(1) time.
- Consider the size of cache = 5.

# Problem 2: Finding Files

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Note: `os.walk()` is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use `os.walk()`.

# Problem 3: Huffman Coding

A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

Possible pseudocode:
- Take a string and determine the relevant frequencies of the characters.
- Build and sort a list of tuples from lowest to highest frequencies.
- Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
- Trim the Huffman Tree (remove the frequencies from the previously built tree).
- Encode the text into its compressed form.
- Decode the text from its compressed form.

# Problem 4: Active Directory

In Windows Active Directory, a group can consist of user(s) and group(s).
Write a function that provides an efficient look up of whether the user is in a group.

# Problem 5: Blockchain

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

The task is to implement blockchain as a linked list.