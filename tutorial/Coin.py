import os, sys
_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(_PATH)

from util import compile_contract, wait_contract_address, get_contract, transact_function, wait_event

# deploy smart contract and return contract object
def deploy_Coin_contract(w3, account):

    contract_interface = compile_contract(_PATH + '/smartContract/Coin.sol', "Coin")
    contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    transaction = contract.constructor().buildTransaction({
        'nonce': w3.eth.getTransactionCount(account.address),
        'from': account.address
    })
    signed_transaction = w3.eth.account.signTransaction(transaction, account.privateKey)
    tx_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    contract_address = wait_contract_address(w3, tx_hash)
    contract = get_contract(w3, contract_address, contract_interface['abi'])

    return contract

# mint
# args = address receiver, uint256 amount
def mint(w3, account, contract, receiver, amount) :
    transactor = contract.functions["mint"](receiver, amount)
    tx_hash = transact_function(w3, account, transactor)
    w3.eth.waitForTransactionReceipt(tx_hash)

# send
# args = address receiver, uint256 amount
def send(w3, account, contract, receiver, amount) :
    transactor = contract.functions["send"](receiver, amount)
    tx_hash = transact_function(w3, account, transactor)
    result = wait_event(w3, contract, tx_hash, "Sent")
    return result[0]['args']['from'], result[0]['args']['to'], result[0]['args']['amount']


# getBalance
def get_balance(account, contract) :
    transactor = contract.functions["get_balance"]()
    result = transactor.call({'from' : account.address})

    return result