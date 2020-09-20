from hashlib import sha256
import json


class Block:
    def __init__(self, key, transactions, timestamp, previous_hash, nonce=0):
        """
        :param key: Unique ID for the block
        :param transactions: list of transactions
        :param timestamp: time of generation of block
        :param previous_hash: hash value of the previous block
        """
        self.key = key
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        json_str = json.dumps(self.__dict__, sort_keys=True)
        return sha256(json_str.encode()).hexdigest()
