#!/bin/bash

URL="localhost:3000/api/"

generate_transaction()
{
  cat <<EOF
{
"states": [
  {
    "state": "fridge",
    "timeStart": "Mon Feb 24 2020 10:55:54",
    "assessment": "ok",
    "average": 3.5625,
    "data": [],
    "totalReadings": 16,
    "timeEnd": "Mon Feb 24 2020 15:56:46"
  },
  {
    "state": "outside",
    "timeStart": "Mon Feb 24 2020 15:56:46",
    "assessment": "ok",
    "average": 24.625,
    "data": [],
    "totalReadings": 1,
    "timeEnd": "Mon Feb 24 2020 16:12:15"
  }
],
"warnings": [],
"puckID": "compliant",
"status": "accepted",
"deliveryID": "ba59f44b-b76e-425e-a222-9de35b44689d"
}
EOF
}

get() {
  # Warmup
  for i in {1..5}
  do
    curl -L "${URL}/Delivery/9be61d4831211bc40dae3423782f6c674a8d67748b6affef4fbf87cc9777c317" -s -o /dev/null -w  "%{time_starttransfer}\n" > /dev/null
  done

  for i in {1..100}
  do
    curl -L "${URL}/Delivery/9be61d4831211bc40dae3423782f6c674a8d67748b6affef4fbf87cc9777c317" -s -o /dev/null -w  "%{time_starttransfer}\n" >> get_test
  done
}

post() {
  # Warmup
  for i in {1..5}
  do
    curl --header "Content-Type: application/json" \
      --request POST \
      --data "$(generate_transaction)" \
      http://localhost:8080/api/transaction > /dev/null

  done

  for i in {1..100}
  do
    echo "Request #${i}"
    curl --header "Content-Type: application/json" \
      --request POST \
      --data "$(generate_transaction)" \
      http://localhost:8080/api/transaction \
      -s -o /dev/null -w  "%{time_starttransfer}\n" >> post_test

  done
}
post
