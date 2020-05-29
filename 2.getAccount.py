from web3 import Web3
from util import extract_key_from_keyfile
import json
w3 = Web3(Web3.IPCProvider("./block/geth.ipc"))

account_list = []
password = ['coinbase', 'n1', 'n2']
for i in password :
    privKey = extract_key_from_keyfile('./keyFile/'+i+'.json', i.encode())

    with open('./keyFile/'+i+'.json', 'r') as f:
        key_file = json.load(f)

    print(i + ": ")
    print("accout : ", '0x' +key_file['address'])
    print("privKey : ", privKey.hex())
    print()