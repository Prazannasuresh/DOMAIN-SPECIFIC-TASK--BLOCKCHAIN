Here, we generate a blockchain using python.
We require to first generate a genesis block, which initiates the blockchain.
We define two classes; ONE for the block and the other for the blockchain.
The class for the block defines its features, such as the data contained or the transaction data, the time of addition, nonce, hash value and the previous hash value. For the genesis block, the previous hash value is defined to be 0.
Now, addition of the block into the blockchain is defined within the class for the blockchian. This is done in two ways for the two parts of the questions. 
For one of the parts of the question, we simply append it. We just develop a mechanism to check the integrity of the blocks using a function to prevent tampering. This is done by comparing the previous hash value to the calculated ones, as well as for the current hash value. The address of the block that is tampered externally is printed.
For the second part, a PoW or Proof of Work algorithm is used to check the integrity of the blocks added. Initially, we set a difficulty parameter and then further for the blockchain, we set its value to 4.
This ensures that only the hash value starting with difficulty*0 or 4 zeroes is printed; this prevents malicious addition by external agents or tampering, since only blocks with selective hash values are added to the blockchain.
