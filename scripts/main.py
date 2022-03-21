import json
import time
from brownie import Product, accounts


def add_product(expiration_timestamp: int, name: str) -> Product:
    account = accounts.load('deployment_account', password='1')
    return Product.deploy(expiration_timestamp, name, {'from': account}, publish_source=True)

def get_properties(contract_id: str) -> dict:
    product = Product.at(contract_id)
    return {
        'expirationTimestamp': product.getExpirationTimestamp(),
        'metadata': product.getMetadata(),
        'onShelf': product.getOnShelf(),
        'owner': product.getOwner(),
    }

def take_off_shelf(contract_id: str) -> None:
    product = Product.at(contract_id)
    product.takeOffShelf()

def transfer_ownership(contract_id: str, recepient_addr: str) -> None:
    product = Product.at(contract_id)
    product.transferOwnership(recepient_addr)

def main():
    while True:
        try:
            command = input('Enter command [add|get|take|transfer]: ').strip()
            if command.startswith('add'):
                _, fresh_seconds, name = command.split(' ', 2)
                expiration_timestamp = int(time.time()) + int(fresh_seconds)
                _ = add_product(expiration_timestamp, name)
            elif command.startswith('get'):
                _, contract_id = command.split(' ', 1)
                properties = get_properties(contract_id)
                print(json.dumps(properties, indent=4))
            elif command.startswith('take'):
                _, contract_id = command.split(' ', 1)
                take_off_shelf(contract_id)
            elif command.startswith('transfer'):
                _, contract_id, recepient_addr = command.split(' ', 2)
                transfer_ownership(contract_id, recepient_addr)
        except Exception as e:
            print('Error during command execution:', e)

if __name__ == '__main__':
    main()
