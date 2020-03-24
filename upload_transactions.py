#!/usr/bin/python3

import base64
import json
from urllib import request
from urllib.error import HTTPError

USERNAME = ""
PASSWORD = ""

ASSETS_LOCATION = "fixtures/assets.json"
PARTICIPANTS_LOCATION = "fixtures/participants.json"
TRANSCATIONS_LOCATION = "fixtures/deliveries.json"

if __name__ == "__main__":
    transactions = {}
    with open(TRANSCATIONS_LOCATION, "r") as f:
        transactions = json.loads(f.read())
    participant = {}
    with open(PARTICIPANTS_LOCATION, "r") as f:
        participant = json.loads(f.read())
    asset = {}
    with open(ASSETS_LOCATION, "r") as f:
        asset = json.loads(f.read())
    base64string = base64.b64encode(
        ('%s:%s' % (USERNAME, PASSWORD)).encode("ascii")).decode("ascii")

    req = request.Request("https://trustlens.abdn.ac.uk/api/BusinessEntity",
                          headers={
                              "Authorization": "Basic %s" % base64string,
                              "Content-Type": "application/json"
                          },
                          data=json.dumps(participant).encode("utf-8"),
                          method="POST")
    try:
        resp = request.urlopen(req)
        print(resp.getcode())
    except HTTPError as err:
        print(err.read())
    print("\n")

    req = request.Request("https://trustlens.abdn.ac.uk/api/Commodity",
                          headers={
                              "Authorization": "Basic %s" % base64string,
                              "Content-Type": "application/json"
                          },
                          data=json.dumps(asset).encode("utf-8"),
                          method="POST")
    try:
        resp = request.urlopen(req)
        print(resp.getcode())
    except HTTPError as err:
        print(err.read())
    print("\n")

    # Inject transactions
    for transaction in transactions:
        req = request.Request("https://trustlens.abdn.ac.uk/api/Delivery",
                              headers={
                                  "Authorization": "Basic %s" % base64string,
                                  "Content-Type": "application/json"
                              },
                              data=json.dumps(transaction).encode("utf-8"),
                              method="POST")
        try:
            resp = request.urlopen(req)
            print(resp.getcode())
        except HTTPError as err:
            print(err.read())
