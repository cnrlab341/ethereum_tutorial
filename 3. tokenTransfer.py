from web3 import Web3
from util import extract_key_from_keyfile
from account import account
import time

# w3 = Web3(Web3.IPCProvider("./block/geth.ipc"))
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
account_list = []
password = ['coinbase', 'n1', 'n2']
address = ['0xAE4099C5Dc1Fb2326a39d260949a7f349f96cf37',
           '0xB88Cd1eb95fc35CF74028300656AF50381abba61',
           '0xc1207fb8cD6aed09ad6aDA6Cb97ec17bA96b133c']

account_list.append(account(
    bytearray.fromhex('a191f4f7e8284e246de6ecba8ba267bd0e1aa7db46ebf6ce71f104fbe364a794'),
    '0x3284618cEBF0936A508732A9280291c06af611a3'))
for i in range(len(password)) :
    privKey = extract_key_from_keyfile('./keyFile/'+password[i]+'.json',
                                       password[i].encode())

    account_list.append(account(privKey, address[i]))

# send token to n1, n2
# w3.geth.miner.setEtherbase(account_list[0].address)
# w3.geth.miner.start(1)
# time.sleep(15)

account_list[0].token_transfer(w3, account_list[1], 10000000)
account_list[0].token_transfer(w3, account_list[2], 10000000)
print(w3.eth.getBalance(account_list[0].address))
print(w3.eth.getBalance(account_list[1].address))
print(w3.eth.getBalance(account_list[2].address))

# w3.geth.miner.stop()