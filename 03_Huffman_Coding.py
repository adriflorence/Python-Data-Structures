import sys
import queue

# Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
# Trim the Huffman Tree (remove the frequencies from the previously built tree).

class Huffman_Node(object):
    def __init__(self, left = None, right = None, value = None, frequency = None):
        self.left = None
        self.right = None
        self.value = value
        self.frequency = frequency

    # Compare two Huffman_Nodes
    def __lt__(self, other):
        return self.frequency < other.frequency
    
    # override stringify
    def __str__(self):
        return str(self.value) + " " + str(self.frequency)


# 1. Take a string and determine the relevant frequencies of the characters.
def get_frequencies(data):
    if not isinstance(data, str):
        return False

    char_dict = {}
    for char in data:
        if char not in char_dict:
            char_dict[char] = 1
        else: 
            char_dict[char] += 1
    # 2. Build and sort a list of tuples from lowest to highest frequencies.
    frequencies = sorted(zip(char_dict.values(), char_dict.keys()))
    print(frequencies)
    return frequencies



def create_huffman_tree(frequencies):
    priority_queue = queue.PriorityQueue()

    if len(frequencies) == 1:
        node = Huffman_Node(None, None, None, 0) # left, right, value, frequency
        priority_queue.put(node)
    
    # 3. Replace sorted tuples with Huffman_Nodes
    for value in frequencies:
        node = Huffman_Node(frequency = value[0], element = value[1])
        print(Huffman_Node.__str__(node))
        priority_queue.put(node)




# 5. Encode the text into its compressed form
def huffman_encoding(data):
    frequencies = get_frequencies(data)
    tree = create_huffman_tree(frequencies)
    pass


# 6. Decode the text from its compressed form
def huffman_decoding(data,tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    huffman_encoding(a_great_sentence)