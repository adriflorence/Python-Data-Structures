import sys
import queue


class Huffman_Node(object):
    def __init__(self, left = None, right = None, frequency = None, value = None):
        self.left = left
        self.right = right
        self.frequency = frequency
        self.value = value

    # Compare two Huffman_Nodes
    def __lt__(self, other):
        return self.frequency < other.frequency
    
    # override stringify
    def __str__(self):
        return str(self.frequency) + " " + str(self.value)


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
    frequencies = zip(char_dict.values(), char_dict.keys())
    return frequencies


# 3. Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters.
def create_huffman_tree(frequencies):
    if frequencies:
        priority_queue = queue.PriorityQueue()

        if len(frequencies) == 1:
            node = Huffman_Node(None, None, 0, None) # left, right, frequency, value
            priority_queue.put(node)
        
        # 4. Replace sorted tuples with Huffman_Nodes
        for element in frequencies:
            node = Huffman_Node(frequency = element[0], value = element[1])
            # print(Huffman_Node.__str__(node))
            priority_queue.put(node)

        while priority_queue.qsize() > 1:
            # get the two most frequently used items = highest priority
            hp1 = priority_queue.get() # left
            hp2 = priority_queue.get() # right
            parent = Huffman_Node(hp1, hp2, hp1.frequency + hp2.frequency)
            priority_queue.put(parent)

        tree = priority_queue.get()
        del priority_queue
        return tree



def build_codes(node, code = None, codes = {}):
    if not node:
        return False

    if code is None:
        code = ""
        
    if node.value:
        codes[node.value] = code
        # print('node value: ', node.value, 'code: ', code)
    build_codes(node.left, code + "0", codes)
    build_codes(node.right, code + "1", codes)
    return codes


# 5. Encode the text into its compressed form
def encode(text, codes):
    output = ""
    for char in text:
        output += codes[char]
    return output


def huffman_encoding(text):
    frequencies = get_frequencies(text)
    tree = create_huffman_tree(frequencies)
    codes = build_codes(tree)
    bitcode = encode(text, codes)
    # print(bitcode)
    return bitcode, tree


# 6. Decode the text from its compressed form
def huffman_decoding(encoded_text, root):

    node = root
    output = ""
    # Iterate through each char in encoded text
    for char in encoded_text:
        # if current_node is a leaf, add character to output string
        if (node.left is None and node.right is None):
            output += node.value
            node = root
        if char == "0":
            node = node.left
        if char == "1":
            node = node.right
    output += node.value
    return output


if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    huffman_encoding(a_great_sentence)

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree) # tree = root node

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))