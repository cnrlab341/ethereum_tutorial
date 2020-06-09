import os, sys, time
_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(_PATH)

from web3 import Web3
from util import extract_key_from_keyfile
from account import account
from Coin import deploy_Coin_contract

# w3 = Web3(Web3.IPCProvider("./blockchain/geth.ipc"))
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
account_list = []
password = ['coinbase', 'n1', 'n2']
address = [
    '0x2C749426ff936a1B522fFdc8dcBf9eb8d78b3D00',
    '0x0697875dc0ae871809f049211d85b939b7B75A75',
    '0xdB66F629495c5B1d17d28A35ccEd5ECB6F494BD3'
]

for i in range(len(password)) :
    privKey = extract_key_from_keyfile(_PATH + '/keyFile/' + password[i] + '.json',
                                       password[i].encode())

    account_list.append(account(privKey, address[i]))

w3.geth.miner.setEtherbase(account_list[0].address)
w3.geth.miner.start(1)

contract = deploy_Coin_contract(w3, account_list[0])
print("contract addresss : ", contract.address)

w3.geth.miner.stop()