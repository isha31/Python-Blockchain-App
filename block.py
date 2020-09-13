from hashlib import sha256
import json


class Block:
    def __init__(self, key, transactions, timestamp, previous_hash):
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

    def compute_hash():
        json_str = json.dumps(self.__dict__, sortKeys=True)
        return sha256(json_str.encode()).hexdigest
