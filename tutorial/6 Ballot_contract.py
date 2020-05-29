import os, sys, time
_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(_PATH)

from web3 import Web3
from util import extract_key_from_keyfile
from account import account
from Ballot import deploy_Ballot_contract, giveRightToVote, vote, winnerName

# w3 = Web3(Web3.IPCProvider("./blockchain/geth.ipc"))
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
account_list = []
password = ['coinbase', 'n1', 'n2']
address = [
    '0xf2147021ea7A3461a27d8f311F438f1e93BbEf53',
    '0x86EB3b6133b30f84C664b23F5777a39295F030A4',
    '0x8F5F709a079ABBf657DE960721593d0e3b0480Ae'
]

for i in range(len(password)) :
    privKey = extract_key_from_keyfile(_PATH + '/keyFile/'+password[i]+'.json',
                                       password[i].encode())

    account_list.append(account(privKey, address[i]))

w3.geth.miner.setEtherbase(account_list[0].address)
w3.geth.miner.start(1)
time.sleep(15)

proposal_node = [
    '0daDa006Be098D919433E05F15Fdb7d40daDa006Be098D919433E05F15Fdb7d4',
    'dDd2b8e44e7249C130EFacA61A849032dDd2b8e44e7249C130EFacA61A849032',
    '7B6551d16a3EFd50Fe8699B131F514877B6551d16a3EFd50Fe8699B131F51487'
]
contract = deploy_Ballot_contract(w3, account_list[0], proposal_node)
print("contract addresss : ", contract.address)

giveRightToVote(w3, account_list[0], contract, account_list[1].address)
giveRightToVote(w3, account_list[0], contract, account_list[2].address)

vote(w3, account_list[1], contract, 0)
vote(w3, account_list[2], contract, 0)

result = winnerName(account_list[0], contract)
print(result.hex())

w3.geth.miner.stop()