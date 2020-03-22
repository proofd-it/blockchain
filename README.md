# blockchain
Collection of files used to deploy local instance of Hyperledger Fabric, using [Composer](https://hyperledger.github.io/composer/latest/)

## Deployment
To deploy your own network:
1. Make sure you have all pre-requisites - https://hyperledger.github.io/composer/latest/installing/installing-prereqs.html
2. Clone [fabric-dev-servers](https://github.com/hyperledger-archives/composer-tools/tree/master/packages/fabric-dev-servers) (folder full of scripts) and put it at the root of the repo.
3. Make sure scripts installed in step 1 are in your `PATH` (this is currently hard-coded [here](https://github.com/proofd-it/blockchain/blob/master/startFabric.sh#L2)). Repo should now look as follows
```
blokchain
│   README.md
│   startFabric.sh
│
└───test-proofd
│   │   ...
│   
└───fabric-dev-servers
    │   ...
```
4. `cd` to root of the project (i.e. `blockchain`), run the `startFabric.sh` script

## File structure
The most relevant file, defining the structure of entities stored on blockchain can be found in `test-proofd/models/org.abdn.ac.uk.cto`. There currently are 3 entities:
- Asset, called "Commodity"
- Participant, called "BusinessEntity"
- Transaction, called "Delivery"
