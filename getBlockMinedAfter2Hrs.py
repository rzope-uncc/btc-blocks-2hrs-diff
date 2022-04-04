import requests

class BlockChain:
    def getBlockMinedAfter2Hrs(self):
        i = 1
        count = 0
        blocks = []
        #API fetches last 10 blocks on the Bitcoin network
        r = requests.get(f"https://blockstream.info/api/blocks/")
        ts = r.json()[0]['timestamp']
        while i < len(r.json()):
            print(f"Block {r.json()[i]['height']}")
            #Check whether the block took more than 2 hrs to mine
            if ts - r.json()[i]['timestamp']  > 7200:
                count += 1
                blocks.append(r.json()[i]['height'] + 1)
            ts = r.json()[i]['timestamp']
            #Breaking loop once we reach to Block 0 from current block
            if r.json()[i]['height'] == 0:
                break
            #Fetching next 10 blocks on the Bitcoin network
            if i == 9 and {r.json()[i]['height'] - 1} != 0:
                r = requests.get(f"https://blockstream.info/api/blocks/{r.json()[i]['height'] - 1}")
                i = 0
                print(f"Count => {count} Block => {blocks}")
            else:
                i += 1
        print(f"Count => {count} Block => {blocks}")
        

b = BlockChain()
b.getBlockMinedAfter2Hrs()