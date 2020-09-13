from block import Block
import time


class Blockchain:

    difficulty = 2
    # difficulty of PoW algorithm

    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block():
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block():
        return self.chain[-1]

    def proof_of_work(self, block):
        block.nonce = 0

    def add_block(block, proof):
        last_hash = self.last_block().hash
        if last_hash != block.previous_hash:
            return False
        if not is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(block, block_hash):
        return block_hash.startswith('0' * Blockchain.difficulty) and block_hash
        == block.compute_hash()
