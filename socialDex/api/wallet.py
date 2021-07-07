import password
from web3 import Web3

network_url = password.network_url
w3 = Web3(Web3.HTTPProvider(network_url))
account = w3.eth.account.create()
private_key = account.privateKey.hex()
address = account.address

print(f'Your address: {address}\nYour key: {private_key}')
