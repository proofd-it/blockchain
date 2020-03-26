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
  "complianceReport": "@prefix fs-prov-mapping: <https://w3id.org/abdn/foodsafety/fs-prov_mapping_to_ep-plan#> .\n@prefix ucp:   <https://github.com/proofd-it/Ontologies/deliveryCateringPlan1.ttl#> .\n@prefix ep-plan: <https://w3id.org/ep-plan#> .\n@prefix prov:  <http://www.w3.org/ns/prov#> .\n@prefix fs-prov: <https://w3id.org/abdn/foodsafety/fs-prov#> .\n@prefix prov-trace: <https://github.com/proofd-it/prov-trace#> .\n\nucp:AmbientStorageConstraint\n        ep-plan:qualifiedEvaluation  prov-trace:ea96e900-54b5-44bd-bcbd-d290954419bd .\n\nprov-trace:5cc0ce34-5660-4932-9f68-13f153a71de3\n        a                              ep-plan:Entity ;\n        prov:generatedAtTime           \"1582541754000\"^^<http://www.w3.org/2001/XMLSchema#long> ;\n        prov:invalidatedAtTime         \"1582559806000\"^^<http://www.w3.org/2001/XMLSchema#long> ;\n        prov:wasGeneratedBy            prov-trace:6b8d4272-cda2-4b6d-8af7-db20d6bfa25b ;\n        ep-plan:correspondsToVariable  ucp:ChilledItem ;\n        ep-plan:isElementOfTrace       prov-trace:99a538c5-4022-4ba9-b883-996f7441e317 ;\n        <https://w3id.org/proofd-it#deliveryID>\n                \"ba59f44b-b76e-425e-a222-9de35b44689d\" .\n\nprov-trace:03fe969b-95b0-4371-b8a8-b8bbaa5e4638\n        a                       ep-plan:Activity , prov:Activity ;\n        prov:wasAssociatedWith  prov-trace:UniversityCatering ;\n        ep-plan:satisfied       ucp:TotalTimeAllowedForColdStorage , ucp:TotalTimeAllowedForAmbientTemperatureStorage , ucp:TotalNumberOfAmbientTemperatureStorageStages .\n\nprov-trace:35216028-480e-44dc-98ff-f6b34ba88879\n        a                     prov:Collection , <https://w3id.org/proofd-it#ObservationCollection> ;\n        prov:wasAttributedTo  <https://github.com/proofd-it/prov-trace#Puck/compliant> ;\n        prov:wasGeneratedBy   prov-trace:fc8f7519-ec7b-4cfc-aaa2-aea27e3fc9b6 ;\n        <https://w3id.org/proofd-it#average>\n                \"24.625\"^^<http://www.w3.org/2001/XMLSchema#double> ;\n        <https://w3id.org/proofd-it#numberOfReadings>\n                \"1\"^^<http://www.w3.org/2001/XMLSchema#int> ;\n        <https://w3id.org/proofd-it#unit>\n                <http://www.ontology-of-units-of-measure.org/resource/om-2/degreeCelsius> .\n\nprov-trace:c19f50dc-e6d7-4e28-84d2-ed907c9b900d\n        a                              ep-plan:Entity ;\n        prov:generatedAtTime           \"1582560735000\"^^<http://www.w3.org/2001/XMLSchema#long> ;\n        prov:value                     \"accepted\" ;\n        prov:wasGeneratedBy            prov-trace:2f6d64f0-6a5a-48d4-91f5-1a995f7968d8 ;\n        ep-plan:correspondsToVariable  ucp:DeliveryResult ;\n        ep-plan:isElementOfTrace       prov-trace:99a538c5-4022-4ba9-b883-996f7441e317 .\n\nprov-trace:UniversityCatering\n        a       prov:Agent .\n\nprov-trace:AirTemperature\n        a       <http://www.w3.org/ns/sosa/ObservableProperty> .\n\nprov-trace:d577805d-4715-4d7a-b681-575424d71ee5\n        a                              ep-plan:ConstraintEvaluation ;\n        ep-plan:evaluatedTraceElement  prov-trace:03fe969b-95b0-4371-b8a8-b8bbaa5e4638 ;\n        <https://w3id.org/proofd-it#assessedBy>\n                prov-trace:99a538c5-4022-4ba9-b883-996f7441e317 ;\n        <https://w3id.org/proofd-it#basedOn>\n                <https://github.com/proofd-it/prov-trace#Puck/compliant> .\n\nprov-trace:b97b4b1e-7a16-4485-bb75-fd83e7f00290\n        a                              ep-plan:ConstraintEvaluation ;\n        ep-plan:evaluatedTraceElement  prov-trace:03fe969b-95b0-4371-b8a8-b8bbaa5e4638 ;\n        <https://w3id.org/proofd-it#assessedBy>\n                prov-trace:99a538c5-4022-4ba9-b883-996f7441e317 ;\n        <https://w3id.org/proofd-it#basedOn>\n                <https://github.com/proofd-it/prov-trace#Puck/compliant> .\n\nprov-trace:f4f8f88a-3f7d-43ec-978c-94ba3101240f\n        a                     prov:Collection , <https://w3id.org/proofd-it#ObservationCollection> ;\n        prov:wasAttributedTo  <https://github.com/proofd-it/prov-trace#Puck/compliant> ;\n        prov:wasGeneratedBy   prov-trace:7d654db8-6afd-4ee9-b4d6-4106a374ed0a ;\n        <https://w3id.org/proofd-it#average>\n                \"3.5625\"^^<http://www.w3.org/2001/XMLSchema#double> ;\n        <https://w3id.org/proofd-it#numberOfReadings>\n                \"16\"^^<http://www.w3.org/2001/XMLSchema#int> ;\n        <https://w3id.org/proofd-it#unit>\n                <http://www.ontology-of-units-of-measure.org/resource/om-2/degreeCelsius> .\n\nucp:ColdStorageConstraint\n        ep-plan:qualifiedEvaluation  prov-trace:6735e223-7c4e-4b09-990b-7f0c171fb28f .\n\n<https://github.com/proofd-it/prov-trace#Puck/compliant>\n        a       <http://www.w3.org/ns/sosa/Sensor> , prov:Agent .\n\nprov-trace:a5f6ab64-7df8-43ba-bef3-6d51f1aa2b1d\n        a                          ep-plan:Activity ;\n        prov:used                  prov-trace:5cc0ce34-5660-4932-9f68-13f153a71de3 ;\n        ep-plan:correspondsToStep  ucp:AmbientTemperatureStorage ;\n        ep-plan:isElementOfTrace   prov-trace:99a538c5-4022-4ba9-b883-996f7441e317 ;\n        ep-plan:satisfied          ucp:AmbientStorageConstraint .\n\nprov-trace:e684658f-9cc7-46d5-a9f4-ddb2ce22dc3c\n        a                              ep-plan:Entity ;\n        ep-plan:correspondsToVariable  ucp:PackedItem ;\n        ep-plan:isElementOfTrace       prov-trace:99a538c5-4022-4ba9-b883-996f7441e317 ;\n        <https://w3id.org/proofd-it#deliveryID>\n                \"ba59f44b-b76e-425e-a222-9de35b44689d\" .\n\nprov-trace:ea96e900-54b5-44bd-bcbd-d290954419bd\n        a                              ep-plan:ConstraintEvaluation ;\n        ep-plan:evaluatedTraceElement  prov-trace:a5f6ab64-7df8-43ba-bef3-6d51f1aa2b1d ;\n        <https://w3id.org/proofd-it#assessedBy>\n                <https://github.com/proofd-it/prov-trace#Puck/compliant> ;\n        <https://w3id.org/proofd-it#basedOn>\n                prov-trace:35216028-480e-44dc-98ff-f6b34ba88879 .\n\nucp:TotalNumberOfAmbientTemperatureStorageStages\n        ep-plan:qualifiedEvaluation  prov-trace:d577805d-4715-4d7a-b681-575424d71ee5 .\n\nprov-trace:279aabe4-c527-490c-a026-75eedac7e0dc\n        a                              ep-plan:Entity ;\n        prov:generatedAtTime           \"1582559806000\"^^<http://www.w3.org/2001/XMLSchema#long> ;\n        prov:invalidatedAtTime         \"1582560735000\"^^<http://www.w3.org/2001/XMLSchema#long> ;\n        prov:wasGeneratedBy            prov-trace:a5f6ab64-7df8-43ba-bef3-6d51f1aa2b1d ;\n        ep-plan:correspondsToVariable  ucp:OutOfColdStorageItem ;\n        ep-plan:isElementOfTrace       prov-trace:99a538c5-4022-4ba9-b883-996f7441e317 ;\n        <https://w3id.org/proofd-it#deliveryID>\n                \"ba59f44b-b76e-425e-a222-9de35b44689d\" .\n\nucp:TotalTimeAllowedForColdStorage\n        ep-plan:qualifiedEvaluation  prov-trace:6cc1bce9-9539-438c-acba-524edc1259eb .\n\nprov-trace:6735e223-7c4e-4b09-990b-7f0c171fb28f\n        a                              ep-plan:ConstraintEvaluation ;\n        ep-plan:evaluatedTraceElement  prov-trace:6b8d4272-cda2-4b6d-8af7-db20d6bfa25b ;\n        <https://w3id.org/proofd-it#assessedBy>\n                <https://github.com/proofd-it/prov-trace#Puck/compliant> ;\n        <https://w3id.org/proofd-it#basedOn>\n                prov-trace:f4f8f88a-3f7d-43ec-978c-94ba3101240f .\n\nprov-trace:2f6d64f0-6a5a-48d4-91f5-1a995f7968d8\n        a                          ep-plan:Activity ;\n        prov:used                  prov-trace:279aabe4-c527-490c-a026-75eedac7e0dc ;\n        ep-plan:correspondsToStep  ucp:RecievedByCustomer ;\n        ep-plan:isElementOfTrace   prov-trace:99a538c5-4022-4ba9-b883-996f7441e317 .\n\nprov-trace:99a538c5-4022-4ba9-b883-996f7441e317\n        a                     ep-plan:ExecutionTraceBundle ;\n        prov:wasDerivedFrom   ucp:UniversityCateringSandwichDeliveryPlan ;\n        prov:wasInfluencedBy  prov-trace:03fe969b-95b0-4371-b8a8-b8bbaa5e4638 .\n\nucp:TotalTimeAllowedForAmbientTemperatureStorage\n        ep-plan:qualifiedEvaluation  prov-trace:b97b4b1e-7a16-4485-bb75-fd83e7f00290 .\n\nprov-trace:ac171473-d777-47e3-93a3-68546cfab9b6\n        a                              ep-plan:Entity ;\n        prov:generatedAtTime           \"1582560735000\"^^<http://www.w3.org/2001/XMLSchema#long> ;\n        prov:wasGeneratedBy            prov-trace:2f6d64f0-6a5a-48d4-91f5-1a995f7968d8 ;\n        ep-plan:correspondsToVariable  ucp:DeliveredItem ;\n        ep-plan:isElementOfTrace       prov-trace:99a538c5-4022-4ba9-b883-996f7441e317 ;\n        <https://w3id.org/proofd-it#deliveryID>\n                \"ba59f44b-b76e-425e-a222-9de35b44689d\" .\n\nprov-trace:7d654db8-6afd-4ee9-b4d6-4106a374ed0a\n        a                       <http://www.w3.org/ns/sosa/Observation> , prov:Activity , <https://w3id.org/proofd-it#MultiSensingActivity> ;\n        prov:wasAssociatedWith  <https://github.com/proofd-it/prov-trace#Puck/compliant> ;\n        <http://www.w3.org/ns/sosa/hasFeatureOfInterest>\n                prov-trace:5cc0ce34-5660-4932-9f68-13f153a71de3 ;\n        <http://www.w3.org/ns/sosa/hasObservableProperty>\n                prov-trace:AirTemperature .\n\nprov-trace:fc8f7519-ec7b-4cfc-aaa2-aea27e3fc9b6\n        a                       <http://www.w3.org/ns/sosa/Observation> , prov:Activity , <https://w3id.org/proofd-it#MultiSensingActivity> ;\n        prov:wasAssociatedWith  <https://github.com/proofd-it/prov-trace#Puck/compliant> ;\n        <http://www.w3.org/ns/sosa/hasFeatureOfInterest>\n                prov-trace:279aabe4-c527-490c-a026-75eedac7e0dc ;\n        <http://www.w3.org/ns/sosa/hasObservableProperty>\n                prov-trace:AirTemperature .\n\nprov-trace:6b8d4272-cda2-4b6d-8af7-db20d6bfa25b\n        a                          ep-plan:Activity ;\n        prov:used                  prov-trace:e684658f-9cc7-46d5-a9f4-ddb2ce22dc3c ;\n        ep-plan:correspondsToStep  ucp:ColdStorage ;\n        ep-plan:isElementOfTrace   prov-trace:99a538c5-4022-4ba9-b883-996f7441e317 ;\n        ep-plan:satisfied          ucp:ColdStorageConstraint .\n\nprov-trace:6cc1bce9-9539-438c-acba-524edc1259eb\n        a                              ep-plan:ConstraintEvaluation ;\n        ep-plan:evaluatedTraceElement  prov-trace:03fe969b-95b0-4371-b8a8-b8bbaa5e4638 ;\n        <https://w3id.org/proofd-it#assessedBy>\n                prov-trace:99a538c5-4022-4ba9-b883-996f7441e317 ;\n        <https://w3id.org/proofd-it#basedOn>\n                <https://github.com/proofd-it/prov-trace#Puck/compliant> .\n",
  "timestamp": "2020-03-26T11:44:16.962Z"
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
    # print("Creating Participants")
    create_participants(0, 1)
    for x in range(50000, 100000, 500):
        create_assets(x, x + 500)
        create_transaction(x, x + 500)


if __name__ == "__main__":
    evaluate()
