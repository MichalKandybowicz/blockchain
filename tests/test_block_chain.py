from unittest import TestCase
import hashlib
import json

from blockchain import Blockchain


class BlockchainTestCase(TestCase):

    def setUp(self):
        self.blockchain = Blockchain()

    def create_block(self, proof=123, previous_hash='abc'):
        self.blockchain.new_block(proof, previous_hash)


class TestBlocks(BlockchainTestCase):

    def test_block_creation(self):
        self.create_block()

        latest_block = self.blockchain.get_last_block

        # The genesis block is create at initialization, so the length should be 2
        assert len(self.blockchain.chain) == 2
        assert latest_block['index'] == 2
        assert latest_block['proof'] == 123
        assert latest_block['previous_hash'] == 'abc'

    def test_return_last_block(self):
        self.create_block()

        created_block = self.blockchain.get_last_block

        assert len(self.blockchain.chain) == 2
        assert created_block is self.blockchain.chain[-1]


class TestHashingAndProofs(BlockchainTestCase):

    def test_hash_is_correct(self):
        self.create_block()

        new_block = self.blockchain.get_last_block
        new_block_json = json.dumps(self.blockchain.get_last_block, sort_keys=True).encode()
        new_hash = hashlib.sha256(new_block_json).hexdigest()

        assert len(new_hash) == 64
        assert new_hash == self.blockchain.hash(new_block)