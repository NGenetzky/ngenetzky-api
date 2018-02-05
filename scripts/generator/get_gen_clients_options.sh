#!/bin/sh
curl -s \
  -X GET \
  "http://generator.swagger.io/api/gen/clients/python" \
  -H  "accept: application/json" \
  | jq .
