# Smart_Blockchain.py

import hashlib
import json
import time
from urllib.parse import urlparse

class Smart_Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()

        # Genesis block
        self.new_block(previous_hash="1")

    def new_block(self, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'previous_hash': previous_hash,
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, amount, recipient):
        fees = 0.02
        transaction = {
            'sender': sender,
            'amount_send': amount,
            'bpsc': 'bpsc_wallet_address',
            'amount_bpsc': amount * fees,
            'recipient': recipient,
            'amount_receive': amount * (1 - fees),
        }
        self.current_transactions.append(transaction)
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    def hash(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def register_node(self, address):
        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')

    def smart_chain(self):
        response = requests.get(f'http://127.0.0.1:3000/chain')
        if response.status_code == 200:
            new_chain = response.json().get('chain')
            if new_chain and len(new_chain) > len(self.chain):
                self.chain = new_chain
                return True
        return False
