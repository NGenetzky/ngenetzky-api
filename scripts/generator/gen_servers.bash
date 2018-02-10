#!/bin/sh -x
COMMIT="5858e03eab7971e6161915a3177738311c2650df"
SWAGGER_URL="https://raw.githubusercontent.com/NGenetzky/ngenetzky-api/${COMMIT}/api/swagger.yaml"
SERVER_PORT="80"

post_gen_servers()
{
  local gen_reply=$(curl -X POST \
    "http://generator.swagger.io/api/gen/servers/python-flask" \
    -H  "accept: application/json" \
    -H  "content-type: application/json" \
    -d "{  \"spec\": {},  \"options\": {    \"serverPort\": \"${SERVER_PORT}\"  },  \"swaggerUrl\": \"${SWAGGER_URL?}\"}" \
    ) || return $?
  echo $gen_reply | jq --raw-output .link
}

gen_servers()
{
  local filename="${1-archive.zip}"
  local url=$(post_gen_servers)
  wget --output-document "${filename}" "${url}"
}

gen_servers python-flask-generated.zip

