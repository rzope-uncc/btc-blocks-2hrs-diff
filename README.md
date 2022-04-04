# Finding BTC Blocked mined 2 hrs after its previous block

### How to run
````
python getBlockMinedAfter2Hrs.py
````

### API Used

````
Method: GET
URL: https://blockstream.info/api/blocks/
Details: It fetches details of recently mined 10 block on the bitcoin network.
````

````
Method: GET
URL: https://blockstream.info/api/blocks/{BLOCK_NUMBER/BLOCK_HEIGHT}
Details: It fetches details of 10 recent block counting from the given block.
````
