from web3 import Web3
from util import random_key, create_keyfile_json
import json

w3 = Web3(Web3.IPCProvider("./block/geth.ipc"))

account_list = []
password = ["coinbase", "n1", "n2"]
for i in range(len(password)):
    privKey = random_key()
    byte_privKey = bytearray.fromhex(privKey)
    keyFile = create_keyfile_json(byte_privKey, password[i].encode())

    with open("./keyFile/" + password[i] + ".json", 'w', encoding='utf-8') as make_file:
        json.dump(keyFile, make_file, indent="\t")

    print(password[i] + " : ")
    print("privKey : ", privKey)
    print("address : ", '0x' + keyFile['address'])
    print("checksum address : ", Web3.toChecksumAddress('0x' + keyFile['address']))
    print("password : ", password[i])
    print()
