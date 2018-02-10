#!/bin/sh
curl -s \
  -X GET \
  "http://generator.swagger.io/api/gen/servers/python-flask" \
  -H  "accept: application/json" \
  | jq .
