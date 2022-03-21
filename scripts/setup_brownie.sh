#!/bin/bash

virtualenv venv
. ./venv/bin/activate
pip install -r requirements.txt

brownie networks add Polygon polygon-test-2 host=https://rpc-mumbai.matic.today chainid=80001 explorer=https://api-testnet.polygonscan.com/api

echo 'Please, set password to `1`'
brownie accounts generate deployment_account
