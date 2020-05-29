from web3 import Web3
from util import extract_key_from_keyfile, compile_contract, get_contract
from account import account
from smartContract.Coin import deploy_Coin_contract, mint, send, get_balance
import json, time

# w3 = Web3(Web3.IPCProvider("./block/geth.ipc"))
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
account_list = []
password = ['coinbase', 'n1', 'n2']
address = ['0xAE4099C5Dc1Fb2326a39d260949a7f349f96cf37',
           '0xB88Cd1eb95fc35CF74028300656AF50381abba61',
           '0xc1207fb8cD6aed09ad6aDA6Cb97ec17bA96b133c']

contract_address = "0xD583609BB926B8c2da2c17E4866c638a98a3e21e"

for i in range(len(password)) :
    privKey = extract_key_from_keyfile('./keyFile/'+password[i]+'.json',
                                       password[i].encode())

    account_list.append(account(privKey, address[i]))

# send token to n1, n2
# w3.geth.miner.setEtherbase(account_list[0].address)
# w3.geth.miner.start(1)
# time.sleep(15)

contract_interface = compile_contract('./smartContract/Coin.sol', "Coin")
contract = get_contract(w3, contract_address, contract_interface['abi'])

mint(w3, account_list[0], contract, account_list[1].address, 100)
result2 = send(w3, account_list[1], contract, account_list[0].address, 10)
print(result2)
# # print(contract.address, account_list[1].address)
# # result3 = get_balance(account_list[1], contract)
# # print(result3)
# # result4 = getBalance(account_list[2], contract)
# # print(contract)
# # print(result2)
# # print(result3)
# # print(result4)
#
# w3.geth.miner.stop()



# token_transfer(w3, )


