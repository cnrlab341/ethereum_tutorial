import os, sys, json
_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(_PATH)

from web3 import Web3
from util import extract_key_from_keyfile

# w3 = Web3(Web3.IPCProvider("./blockchain/geth.ipc"))
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

account_list = []
password = ['coinbase', 'n1', 'n2']
for i in password :
    privKey = extract_key_from_keyfile(_PATH + '/keyFile/'+i+'.json', i.encode())

    with open(_PATH + '/keyFile/'+i+'.json', 'r') as f:
        key_file = json.load(f)

    print(i + ": ")
    print("accout : ", '0x' +key_file['address'])
    print("privKey : ", privKey.hex())
    print()