class account :
    def __init__(self, privateKey, address):
        self.privateKey = privateKey
        self.address = address

    # token tranfer
    def token_transfer(self, w3, receiver, amount):
        tx = w3.eth.account.signTransaction({
            'nonce': w3.eth.getTransactionCount(self.address),
            'from': self.address,
            'to': receiver.address,
            'gasPrice': 1,
            'gas': 0x2fefd8,
            'value': amount,
        }, self.privateKey)
        tx_hash = w3.eth.sendRawTransaction(tx.rawTransaction)
        w3.eth.waitForTransactionReceipt(tx_hash)

        return True


