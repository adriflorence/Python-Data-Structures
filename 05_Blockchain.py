import hashlib
import datetime

# Create a blockchain implementation with linked lists and hashing
# The information to be stored in the block chain is
# transaction time, data, and the previous block

# Node
class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = None
        self.hash = self.calc_hash()


    def calc_hash(self):
        sha = hashlib.sha256() # Secure Hash Algorithm 2
        hash_str = (str(self.timestamp).encode('utf-8') + 
                 str(self.data).encode('utf-8') + 
                 str(self.previous_hash).encode('utf-8'))
        sha.update(hash_str)
        return sha.hexdigest()


# LinkedList
class Chain:

    def __init__(self, previous):
        self.head = None

    # append a block to the chain
    def append(self, data, previous_hash):
        if self.head is None:
            self.head = Block(data, previous_hash)
            return
        node = self.head
        while node.next:
            node = node.next

        node.next = Block(data, previous_hash)

    def to_list(self):
        output = []
        node = self.head
        while node:
            output.append(node.value)
            node = node.next
        return output