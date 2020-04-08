import hashlib
import datetime

# Create a blockchain implementation with linked lists and hashing
# The information to be stored in the block chain is
# transaction time, data, and the previous block

# Node
class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()


    def calc_hash(self):
        sha = hashlib.sha256() # Secure Hash Algorithm 2
        hash_str = (str(self.timestamp).encode('utf-8') + 
                 str(self.data).encode('utf-8') + 
                 str(self.previous_hash).encode('utf-8'))
        sha.update(hash_str)
        return sha.hexdigest()


# LinkedList
class BlockChain(object):

    def __init__(self):
        self.tail = None

    # append a block to the chain
    def append(self, data):
        if self.tail is None:
            self.tail = Block(data, None)

        else:
            self.tail = Block(data, self.tail)

    # converts the LinkedList into a plain list
    def to_list(self):
        output = []
        block = self.tail
        while block:
            output.append([block.data, block.timestamp, block.hash])
            block = block.previous_hash
        return output


# TEST
block_chain = BlockChain()

block_chain.append("Genesis Block") # A genesis block is the first block of a blockchain
block_chain.append("Block 1")
block_chain.append("Block 2")

print(block_chain.to_list())