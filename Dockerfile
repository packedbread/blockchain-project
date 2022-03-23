FROM python:3.8

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y curl jq

COPY . /app
WORKDIR /app

ARG POLYGONSCAN_TOKEN

RUN echo "POLYGONSCAN_TOKEN=$POLYGONSCAN_TOKEN" >> .env

RUN echo 1 | ./scripts/setup_brownie.sh

RUN curl 'https://api.faucet.matic.network/transferTokens' -H 'content-type: application/json' --data-raw "{\"network\":\"mumbai\",\"address\":$(cat ~/.brownie/accounts/deployment_account.json | jq '.address'),\"token\":\"maticToken\"}"

CMD brownie run main.py --network polygon-test-2
