import json
import threading
from urllib import request
from urllib.error import HTTPError

ASSET = {
    "$class": "org.abdn.ac.uk.Commodity",
    "tradingSymbol": "DeliveryItem",
    "description": "DeliveryItem",
    "status": "accepted",
    "complianceReport": "report",
    "owner": "resource:org.abdn.ac.uk.BusinessEntity#MestonIndustries"
}
PARTICIPANT = {
    "businessId": "MestonIndustries",
    "businessName": "MestonIndustries"
}
TRANSACTION = {
    "$class": "org.abdn.ac.uk.Delivery",
    "commodity": "resource:org.abdn.ac.uk.Commodity#DeliveryItem",
    "newOwner": "resource:org.abdn.ac.uk.BusinessEntity#MestonIndustries",
    "status": "accepted",
    "complianceReport":
    "@prefix fs-prov-mapping: <https://w3id.org/abdn/foodsafety/fs-prov_mapping_to_ep-plan#> .\n@prefix ucp:   <https://github.com/proofd-it/Ontologies/deliveryCateringPlan1.ttl#> .\n@prefix ep-plan: <https://w3id.org/ep-plan#> .\n@prefix prov:  <http://www.w3.org/ns/prov#> .\n@prefix fs-prov: <https://w3id.org/abdn/foodsafety/fs-prov#> .\n@prefix prov-trace: <https://github.com/proofd-it/prov-trace#> .\n\nprov-trace:fac03f5c-2727-4962-b063-500df92a047a\n        a                     ep-plan:ExecutionTraceBundle ;\n        prov:wasInfluencedBy  prov-trace:2557619c-23fa-4c44-92f4-979d57a1bb15 .\n\nucp:AmbientStorageConstraint\n        ep-plan:qualifiedEvaluation  prov-trace:849de0e0-52b1-46f9-9025-c2c22fdc5643 .\n\nprov-trace:UniversityCatering\n        a       prov:Agent .\n\nprov-trace:df64ef90-fe06-4f9f-89f3-3cac2a725f98\n        a                              ep-plan:ConstraintEvaluation ;\n        prov:wasAttributedTo           <https://github.com/proofd-it/prov-trace#Puck/e4b30760> ;\n        ep-plan:evaluatedTraceElement  prov-trace:2557619c-23fa-4c44-92f4-979d57a1bb15 .\n\nucp:ColdStorageConstraint\n        ep-plan:qualifiedEvaluation  prov-trace:9a4f1a3b-cc95-4fab-9c0e-7cd0caadf530 .\n\nprov-trace:0fe9d329-a0e7-4962-9082-0f2aa3479749\n        a                              ep-plan:ConstraintEvaluation ;\n        prov:wasAttributedTo           <https://github.com/proofd-it/prov-trace#Puck/e4b30760> ;\n        ep-plan:evaluatedTraceElement  prov-trace:2557619c-23fa-4c44-92f4-979d57a1bb15 .\n\nprov-trace:b1f2cffb-b245-4ee8-8a23-de1b6070d4da\n        a                              ep-plan:Entity ;\n        prov:generatedAtTime           \"1581983457000\"^^<http://www.w3.org/2001/XMLSchema#long> ;\n        prov:invalidatedAtTime         \"1582018382000\"^^<http://www.w3.org/2001/XMLSchema#long> ;\n        prov:wasGeneratedBy            prov-trace:0221db3d-3ea5-4466-a63e-2d726ddbc7c2 ;\n        ep-plan:correspondsToVariable  ucp:ChilledItem ;\n        ep-plan:isElementOfTrace       prov-trace:fac03f5c-2727-4962-b063-500df92a047a .\n\nprov-trace:1b522fc7-1ccb-416f-9d1b-27c6b396eb22\n        a                          ep-plan:Activity ;\n        prov:used                  prov-trace:b1f2cffb-b245-4ee8-8a23-de1b6070d4da ;\n        ep-plan:correspondsToStep  ucp:AmbientTemperatureStroage ;\n        ep-plan:violated           ucp:AmbientStorageConstraint .\n\nucp:MaxCombinedAmbientStorageTime\n        ep-plan:qualifiedEvaluation  prov-trace:0fe9d329-a0e7-4962-9082-0f2aa3479749 .\n\nprov-trace:9a4f1a3b-cc95-4fab-9c0e-7cd0caadf530\n        a                              ep-plan:ConstraintEvaluation ;\n        prov:wasAttributedTo           <https://github.com/proofd-it/prov-trace#Puck/e4b30760> ;\n        ep-plan:evaluatedTraceElement  prov-trace:0221db3d-3ea5-4466-a63e-2d726ddbc7c2 .\n\n<https://github.com/proofd-it/prov-trace#Puck/e4b30760>\n        a       prov:Agent .\n\nucp:MaxNumberOfAmbientStorageStages\n        ep-plan:qualifiedEvaluation  prov-trace:df64ef90-fe06-4f9f-89f3-3cac2a725f98 .\n\nprov-trace:849de0e0-52b1-46f9-9025-c2c22fdc5643\n        a                              ep-plan:ConstraintEvaluation ;\n        prov:wasAttributedTo           <https://github.com/proofd-it/prov-trace#Puck/e4b30760> ;\n        ep-plan:evaluatedTraceElement  prov-trace:1b522fc7-1ccb-416f-9d1b-27c6b396eb22 .\n\nprov-trace:2557619c-23fa-4c44-92f4-979d57a1bb15\n        a                          prov:Activity ;\n        prov:qualifiedAssociation  prov-trace:c00fa642-ef87-4f4a-9455-833f11a91a1f ;\n        prov:wasAssociatedWith     prov-trace:UniversityCatering ;\n        ep-plan:satisfied          ucp:MaxCombinedAmbientStorageTime , ucp:MaxSingleStageAmbientStorageTime ;\n        ep-plan:violated           ucp:MaxNumberOfAmbientStorageStages , ucp:OverallTemperatureComplianceConstraint .\n\nucp:MaxSingleStageAmbientStorageTime\n        ep-plan:qualifiedEvaluation  prov-trace:5545101b-6403-4fa9-a4fa-f307b23962fa .\n\nprov-trace:c00fa642-ef87-4f4a-9455-833f11a91a1f\n        a             prov:Association ;\n        prov:agent    prov-trace:UniversityCatering ;\n        prov:hadPlan  ucp:UniversityCateringSandwichDeliveryPlan .\n\nprov-trace:077fb275-c1cb-45bb-bdf4-9ab3ad83dd2d\n        a                              ep-plan:Entity ;\n        prov:generatedAtTime           \"1582018382000\"^^<http://www.w3.org/2001/XMLSchema#long> ;\n        prov:invalidatedAtTime         \"1582148843000\"^^<http://www.w3.org/2001/XMLSchema#long> ;\n        prov:wasGeneratedBy            prov-trace:1b522fc7-1ccb-416f-9d1b-27c6b396eb22 ;\n        ep-plan:correspondsToVariable  ucp:OutOfColdStorageItem ;\n        ep-plan:isElementOfTrace       prov-trace:fac03f5c-2727-4962-b063-500df92a047a .\n\nprov-trace:5545101b-6403-4fa9-a4fa-f307b23962fa\n        a                              ep-plan:ConstraintEvaluation ;\n        prov:wasAttributedTo           <https://github.com/proofd-it/prov-trace#Puck/e4b30760> ;\n        ep-plan:evaluatedTraceElement  prov-trace:2557619c-23fa-4c44-92f4-979d57a1bb15 .\n\nucp:OverallTemperatureComplianceConstraint\n        ep-plan:qualifiedEvaluation  prov-trace:7194a7f5-9fd6-4d79-8a05-b0a480be6141 .\n\nprov-trace:7194a7f5-9fd6-4d79-8a05-b0a480be6141\n        a                              ep-plan:ConstraintEvaluation ;\n        prov:wasAttributedTo           <https://github.com/proofd-it/prov-trace#Puck/e4b30760> ;\n        ep-plan:evaluatedTraceElement  prov-trace:2557619c-23fa-4c44-92f4-979d57a1bb15 .\n\nprov-trace:0221db3d-3ea5-4466-a63e-2d726ddbc7c2\n        a                          ep-plan:Activity ;\n        prov:used                  prov-trace:096d1a63-d3dd-498f-8f6e-da013d99b3db ;\n        ep-plan:correspondsToStep  ucp:ColdStorage ;\n        ep-plan:isElementOfTrace   prov-trace:fac03f5c-2727-4962-b063-500df92a047a ;\n        ep-plan:satisfied          ucp:ColdStorageConstraint .\n\nprov-trace:096d1a63-d3dd-498f-8f6e-da013d99b3db\n        a                              ep-plan:Entity ;\n        ep-plan:correspondsToVariable  ucp:PackedItem ;\n        ep-plan:isElementOfTrace       prov-trace:fac03f5c-2727-4962-b063-500df92a047a .\n",
    "timestamp": "2020-02-19T21:47:49.640Z"
}

BASE_URL = "http://localhost:3000/api/"


def send_request(endpoint, payload, x):
    req = request.Request(BASE_URL + endpoint,
                          headers={"Content-Type": "application/json"},
                          data=json.dumps(payload).encode("utf-8"),
                          method="POST")
    try:
        resp = request.urlopen(req)
        if resp.getcode() == 200:
            print("Success #" + str(x))
    except HTTPError as err:
        print("Already Exists #" + str(x))


def create_participants(start, count):
    threads = []
    for x in range(start, count):
        participant = PARTICIPANT.copy()
        participant["businessId"] = participant["businessId"] + str(x)
        threads.append(
            threading.Thread(target=send_request,
                             args=(
                                 "BusinessEntity",
                                 participant,
                                 x,
                             )))
    for x in threads:
        x.start()
    for x in threads:
        x.join()


def create_assets(start, count):
    threads = []
    for x in range(start, count):
        asset = ASSET.copy()
        asset["tradingSymbol"] = asset["tradingSymbol"] + str(x)
        asset["owner"] = asset["owner"] + "0"
        # asset["owner"] = asset["owner"] + str(x)
        threads.append(
            threading.Thread(target=send_request,
                             args=(
                                 "Commodity",
                                 asset,
                                 x,
                             )))
    for x in threads:
        x.start()
    for x in threads:
        x.join()


def create_transaction(start, count):
    threads = []
    for x in range(start, count):
        transaction = TRANSACTION.copy()
        transaction["newOwner"] = transaction["newOwner"] + "0"
        transaction["commodity"] = transaction["commodity"] + str(x)
        threads.append(
            threading.Thread(target=send_request,
                             args=(
                                 "Delivery",
                                 transaction,
                                 x,
                             )))
    for x in threads:
        x.start()
    for x in threads:
        x.join()


def evaluate():
    print("Creating Participants")
    create_participants(0, 1)
    print("\nCreating Assets")
    for x in range(0, 10000, 500):
        create_assets(x, x + 500)
    print("\nCreating Transactions")
    for x in range(0, 10000, 500):
        create_transaction(x, x + 500)


if __name__ == "__main__":
    evaluate()
