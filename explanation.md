# Problem 1: Least Recently Used Cache

My implementation of LRU cache was built by combining two data structures: a doubly linked list and a hash map.
The head of the linked list holds the most-recently used item, and the tail holds the least-recently used item.
This allows for accessing the LRU element in `O(1)` time by looking at the tail of the list (Source 1).

To access a specific item in the cache, I added a hash map that maps items to linked list nodes, allowing for accessing any element of the cache in `O(1)` time complexity (Source 1).

# Problem 2: Finding Files

In this problem I used a list to collect the files that meet the search criteria. As there is no lookups in the function, only addition, a plain python list was an appropriate choice as that was required to be the function's return type. To collect path names directly into a list from the beginning saves the O(n) conversion complexity that would have been needed to append the path names into a list at the end. 

The time complexith of the function is constant, defined by the sum of the number of folders and files in the folder structure. Could be marked as `O(d + f)`, where `d` is the total number of folders and subfolders (or directories), and `f` is the total number of files. 

# Problem 3: Huffman Coding

Time complexity of the methods used for the Huffman encoding/decoding task:

- `get_frequencies(data)`: both the character iteration on the input and the zip method have `O(n)` time complexity, which is the overall time complexity of the function
- `create_huffman_tree(frequencies)`: invoking queue.PriorityQueue(), as well as "maintaining the order by appending to the list and re-sorting also takes at least `O(n log n)` time." (Source 2)
- `build_codes(node, code = None, codes = {})`: time complexity is `O(d)` where d is the depth of the recursion
- `encode(text, codes)`: `O(l)` where l is the length of the input text
- `huffman_decoding(encoded_text, root)`: `O(n)` where n is the lenght of the encoded text that needs to be decoded

# Problem 4: Active Directory

For the Active Directory lookup a recursive algorithm was used, whose time complexity depends on the total number of groups and users in question. As in the original class definition Group has a list of groups and a list of users, I worked with two lists. 

The time complexity of this algorithm is dependant on the number of iterations, that depends on the number of recursions, that depends on the number of groups (that does not have the user in question directly inside), resulting in a `O(g * u)`, where `g` is the number of groups and `u` is the number of users in question.

# Problem 5: Blockchain

The blockchain was implemented with a Linked List and its methods had the following time complexity respectively:
The blockchain's append method in itself had a O(1) time complexity, it was the testing (to_list() method) that required O(n), resulting an overall time complexity of `O(n)`.

# Problem 6: Union and Intersection of Two Linked Lists

Although there are two linked lists specified in the task, in both functions (union and intersection) I decided to use sets in order to get rid of any duplicate values, as a set is a collection of distinct objects. 

When considering union, both the time and space complexity are `O(a + b)`, where a is the length of linked_list_1 and b is the length of linked_list_2.

When considering intersection, iterating through the first set (created from llist_1) requires time complexity of `O(n)` and within that iteration the `x in set` operation requires `O(m)` in worst case. Therefore, the intersection method has a O(n*m) time complexity where `n` and `m` are the length of the two linked lists respectively. 

# References:

1: https://www.interviewcake.com/concept/java/lru-cache
2: https://dbader.org/blog/priority-queues-in-python