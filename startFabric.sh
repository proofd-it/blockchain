#/bin/sh
PATH="/home/s10mm2/.npm-global/bin:$PATH"
cd fabric-dev-servers
./startFabric.sh
./createPeerAdminCard.sh
cd ../test-proofd
version=$(sed -rn 's/"version": "(.*)",/\1/p' package.json | tr -d [:space:])
composer archive create -t dir -n .
composer network install --card PeerAdmin@hlfv1 --archiveFile "test-proofd@$version.bna"
composer network start --networkName test-proofd --networkVersion "$version" --networkAdmin admin --networkAdminEnrollSecret adminpw --card PeerAdmin@hlfv1 --file networkadmin.card
composer card delete -c admin@test-proofd
composer card import --file networkadmin.card
composer-rest-server -c admin@test-proofd -n never -u true -d n -w true  
