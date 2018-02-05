#!/bin/sh
COMMIT="5858e03eab7971e6161915a3177738311c2650df"
SWAGGER_URL="https://raw.githubusercontent.com/NGenetzky/ngenetzky-api/${COMMIT}/api/swagger.yaml"
SERVER_PORT="80"
curl -X POST \
  "http://generator.swagger.io/api/gen/servers/python-flask" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d "{  \"spec\": {},  \"options\": {    \"serverPort\": \"${SERVER_PORT}\"  },  \"swaggerUrl\": \"${SWAGGER_URL?}\"}" \
  | jq .
