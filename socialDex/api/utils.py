import password
from web3 import Web3


def send_transaction(message):
    w3 = Web3(Web3.HTTPProvider(password.network_url))
    address = password.address
    private_key = password.private_key
    nonce = w3.eth.getTransactionCount(address)
    gas_price = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signed_tx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gas_price,
        gas=30000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), private_key)

    tx = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_id = w3.toHex(tx)
    return tx_id
