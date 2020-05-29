import os, sys
_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(_PATH)

from util import compile_contract, wait_contract_address, get_contract, transact_function, wait_event

# deploy smart contract and return contract object
def deploy_Ballot_contract(w3, account, proposalNames):

    contract_interface = compile_contract(_PATH + '/smartContract/Ballot.sol', "Ballot")
    contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    transaction = contract.constructor(proposalNames).buildTransaction({
        'nonce': w3.eth.getTransactionCount(account.address),
        'from': account.address
    })
    signed_transaction = w3.eth.account.signTransaction(transaction, account.privateKey)
    tx_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    contract_address = wait_contract_address(w3, tx_hash)
    contract = get_contract(w3, contract_address, contract_interface['abi'])

    return contract

def giveRightToVote(w3, account, contract, voter) :
    transactor = contract.functions["giveRightToVote"](voter)
    tx_hash = transact_function(w3, account, transactor)
    w3.eth.waitForTransactionReceipt(tx_hash)

def delegate(w3, account, contract, to) :
    transactor = contract.functions["delegate"](to)
    tx_hash = transact_function(w3, account, transactor)
    w3.eth.waitForTransactionReceipt(tx_hash)

def vote(w3, account, contract, proposal) :
    transactor = contract.functions["vote"](proposal)
    tx_hash = transact_function(w3, account, transactor)
    w3.eth.waitForTransactionReceipt(tx_hash)

# getBalance
def winnerName(account, contract) :
    transactor = contract.functions["winnerName"]()
    result = transactor.call({'from' : account.address})

    return result