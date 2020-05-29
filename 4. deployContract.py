from web3 import Web3
from util import extract_key_from_keyfile
from account import account
from smartContract.Coin import deploy_Coin_contract
import time

# w3 = Web3(Web3.IPCProvider("./block/geth.ipc"))
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
account_list = []
password = ['coinbase', 'n1', 'n2']
address = ['0xAE4099C5Dc1Fb2326a39d260949a7f349f96cf37',
           '0xB88Cd1eb95fc35CF74028300656AF50381abba61',
           '0xc1207fb8cD6aed09ad6aDA6Cb97ec17bA96b133c']

for i in range(len(password)) :
    privKey = extract_key_from_keyfile('./keyFile/'+password[i]+'.json',
                                       password[i].encode())

    account_list.append(account(privKey, address[i]))

# send token to n1, n2
# w3.geth.miner.setEtherbase(account_list[0].address)
# w3.geth.miner.start(1)
# time.sleep(15)

contract = deploy_Coin_contract(w3, account_list[0])
print("contract addresss : ", contract.address)

# w3.geth.miner.stop()