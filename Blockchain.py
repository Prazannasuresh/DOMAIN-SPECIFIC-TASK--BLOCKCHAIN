import hashlib
import datetime as date
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.nonce = 0
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        hash_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(hash_string.encode()).hexdigest()
##Mine function is specifically required for showing how the blockchain follows the PoW algorithm
    def mine_block(self, difficulty):
        while self.hash[0:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calc_hash()
        print("Block is successfully mined:", self.hash)
        
class Blockchain:
    def __init__(self):
        self.chain = [self.genesis_block()]

    def genesis_block(self):
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    def latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.latest_block().hash
        new_block.hash = new_block.calc_hash()
        self.chain.append(new_block)

    def is_valid(self):    
        for i in range(1, len(self.chain)):
           current_block = self.chain[i]
           previous_block = self.chain[i-1]                   
           if current_block.hash != current_block.calc_hash() or current_block.previous_hash != previous_block.hash:
                print("Blockchain corrupted!")
                print("Address of the corrupted block:",current_block.calc_hash())
                print(" ")
                return False
        return True
##Parts 1 and 2 can be executed using the above functions. To execute the third part,we set the difficulty to be equal to 4; and add the block to the blockchain using mine fucntion that was defined in the block class.
    def add_block2(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.mine_block(4)
        self.chain.append(new_block) 

##We are generating a blockchain containing 3 blocks, along with an initiated Genesis block.This is an example of 3 membered- P2P network.      
blockchain = Blockchain() 
blockchain.add_block(Block(1, date.datetime.now(), "Sender-Sanjay\nReceiver-Joe\nAmount-7BTC", ""))
blockchain.add_block(Block(2, date.datetime.now(), "Sender-Joe\nReceiver-Tanmay\nAmount-19BTC", ""))
blockchain.add_block(Block(3, date.datetime.now(), "Sender-Sanjay\nReceiver-Tanmay\nAmount-13BTC", ""))

for block in blockchain.chain:
     while blockchain.is_valid():
         print("Block #" + str(block.index))
         print("Timestamp: " + str(block.timestamp))
         print("Data: \n" + block.data)
         print("Hash: " + block.hash)
         print("Previous Hash: " + block.previous_hash)
         print(" ")
         break
##Here, we perform the same blockchain generation by calling the functions, but it is PoW scrutinized.
blockchain = Blockchain()
blockchain.add_block2(Block(1, date.datetime.now(), "Sender-Sanjay\nReceiver-Joe\nAmount-7BTC", ""))
blockchain.add_block2(Block(2, date.datetime.now(), "Sender-Joe\nReceiver-Tanmay\nAmount-19BTC", ""))
blockchain.add_block2(Block(3, date.datetime.now(), "Sender-Sanjay\nReceiver-Tanmay\nAmount-13BTC", ""))
         

          
        

