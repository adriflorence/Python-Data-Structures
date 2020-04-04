import sys

# Take a string and determine the relevant frequencies of the characters.
# Build and sort a list of tuples from lowest to highest frequencies.
# Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
# Trim the Huffman Tree (remove the frequencies from the previously built tree).

def get_frequencies(data):
    char_dict = {}
    for char in data:
        if char not in char_dict:
            char_dict[char] = 1
        else: 
            char_dict[char] += 1
    #create a sorted list key, freq tuple pairs
    sorted_frequencies = sorted(zip(char_dict.values(), char_dict.keys()))
    print(sorted_frequencies)

# Encode the text into its compressed form.
def huffman_encoding(data):
    get_frequencies(data)
    pass

# Decode the text from its compressed form.
def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))