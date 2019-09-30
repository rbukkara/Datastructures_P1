import hashlib
import datetime

class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = datetime.datetime.utcnow()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.block = None
        self.block_index = dict()

    def print_blockchain(self):

        node = self.block
        out_string = ""

        if self.block is None:
            return "block chain is empty"

        while node is not None:
            out_string += "data is {0}; hash is {1}; timestamp is {2}".format(node.data, node.hash, node.timestamp)
            out_string += "\n"
            out_string += " - > "
            if node.previous_hash is None:
                node = None
            else:
                node = self.block_index[node.previous_hash]

        return out_string


    def add_block(self, block_data):

        if block_data is None:
            print("Unable to add block. data initialization error")
            return
        if len(block_data) == 0:
            print("Unable to add block. data initialization error")
            return

        new_block = Block(block_data, None)
        if self.block is None:
            self.block = new_block
            self.block_index[new_block.hash] = new_block
        else:
            new_block.previous_hash = self.block.hash
            self.block_index[new_block.hash] = new_block
            self.block = new_block

        print("'{0}' added".format(block_data))
        return


block_chain = BlockChain()

print(block_chain.print_blockchain())

block_chain.add_block("abc")
block_chain.add_block("")

block_chain.add_block("cde")
block_chain.add_block("def")
print(block_chain.print_blockchain())

block_chain.add_block(None)

print(block_chain.print_blockchain())


