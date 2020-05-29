import os, sys, time
_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(_PATH)

from web3 import Web3
from util import extract_key_from_keyfile, compile_contract, get_contract
from account import account
from Coin import mint, send, get_balance

# w3 = Web3(Web3.IPCProvider("./blockchain/geth.ipc"))
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
account_list = []
password = ['coinbase', 'n1', 'n2']
address = [
    '0xf2147021ea7A3461a27d8f311F438f1e93BbEf53',
    '0x86EB3b6133b30f84C664b23F5777a39295F030A4',
    '0x8F5F709a079ABBf657DE960721593d0e3b0480Ae'
]
contract_address = "0x269517a02323A060c65c3344c71F8b551F1cAF7e"

for i in range(len(password)) :
    privKey = extract_key_from_keyfile(_PATH + '/keyFile/' + password[i] + '.json',
                                       password[i].encode())

    account_list.append(account(privKey, address[i]))

w3.geth.miner.setEtherbase(account_list[0].address)
w3.geth.miner.start(1)
time.sleep(15)

contract_interface = compile_contract('../smartContract/Coin.sol', "Coin")
contract = get_contract(w3, contract_address, contract_interface['abi'])

mint(w3, account_list[0], contract, account_list[1].address, 100)
_from, _to, _amount = send(w3, account_list[1], contract, account_list[2].address, 10)
print("{} -> {} amount : {}".format(_from, _to, _amount))

balance = get_balance(account_list[1], contract)
print("{} balance : {}".format(account_list[1].address, balance))

balance = get_balance(account_list[2], contract)
print("{} balance : {}".format(account_list[1].address, balance))

w3.geth.miner.stop()




