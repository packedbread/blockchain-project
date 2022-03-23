## Blockchain Inventory Management Project

### Prerequisites

Obtain OAuth token for polygonscan.com account.

### How to use (Docker)

1. Build a docker image with obtained polygonscan.com token:

`docker build --build-arg POLYGONSCAN_TOKEN=<YOUR TOKEN GOES HERE> . -t inventory-management`

Along with building docker image, this command will create an Ethereum address for Polygon test network and request tokens for it from a faucet.

2. Run application:

`docker run -it inventory-management`

### How to use (locally)

1. Add .env file that contains `POLYGONSCAN_TOKEN` -- api token for polygonscan.com.
2. Run `./scripts/setup_brownie.sh` that setups virtual environment, adds network config and account for brownie 
3. Run `brownie run main.py --network polygon-test-2`
