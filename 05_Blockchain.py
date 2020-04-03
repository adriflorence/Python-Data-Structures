# Create a blockchain implementation with linked lists and hashing

import hashlib

# information hash
def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

# the information to be stored in the block chain is
# transaction time, data, and the previous chain

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

# The task is to link all of this together in a block chain by implementing it in a linked list