#!/bin/sh
COMMIT="20761760531afb3b9fe36c0741dd6e151623f899"
SWAGGER_URL="https://raw.githubusercontent.com/NGenetzky/ngenetzky-api/${COMMIT}/api/swagger.yaml"
SERVER_PORT="80"
curl -X POST \
  "http://generator.swagger.io/api/gen/servers/python-flask" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d "{  \"spec\": {},  \"options\": {    \"serverPort\": \"${SERVER_PORT}\"  },  \"swaggerUrl\": \"${SWAGGER_URL?}\"}" \
  | jq .
