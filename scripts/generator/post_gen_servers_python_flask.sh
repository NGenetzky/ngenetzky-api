#!/bin/sh
COMMIT="f9eee76f2bc98ee9f0345f39af59d3571bd0a26b"
SWAGGER_URL="https://raw.githubusercontent.com/NGenetzky/ngenetzky-api/${COMMIT}/api/swagger.yaml"
SERVER_PORT="80"
curl -X POST \
  "http://generator.swagger.io/api/gen/servers/python-flask" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d "{  \"spec\": {},  \"options\": {    \"serverPort\": \"${SERVER_PORT}\"  },  \"swaggerUrl\": \"${SWAGGER_URL?}\"}" \
  | jq .
