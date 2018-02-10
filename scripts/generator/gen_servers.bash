#!/bin/bash -x
# Defaults
COMMIT="65920aaa8afb9c035b58a63a091aea3f801a3f2d"

get_swagger_url(){
  local commit="${1-$COMMIT}"
  local url="https://raw.githubusercontent.com/NGenetzky/ngenetzky-api/${commit}/api/swagger.yaml"
  local http_status="$(curl -s -o /dev/null -w "%{http_code}" ${url})"
  case ${http_status} in
    200) echo "${url}" ; return 0 ;;
    *) return 1;
  esac
}

use_commit_from_HEAD() {
  local head="$(git rev-parse HEAD)"
  local remotes_with_head="$(git branch -r --contains ${head})"
  case ${remotes_with_head} in
    '') # Empty
      echo "$head not pushed. Using default (COMMIT=$COMMIT)" ;;
    *) # Some remote has it.
      COMMIT="${head}" ; echo "Using (COMMIT=$COMMIT)";;
  esac
}

post_gen_servers_python_flask()
{
  local swagger_url="${1?}"
  local server_port="80"
  local gen_reply=$(curl -X POST \
    "http://generator.swagger.io/api/gen/servers/python-flask" \
    -H  "accept: application/json" \
    -H  "content-type: application/json" \
    -d "{  \"spec\": {},  \"options\": {    \"serverPort\": \"${server_port}\"  },  \"swaggerUrl\": \"${swagger_url}\"}" \
    ) || return $?
  echo $gen_reply | jq --raw-output .link
}

gen_servers_python_flask()
{
  local swagger_url="${1?}"
  local filename="${2-python-flask-generated.zip}"
  local url=$(post_gen_servers_python_flask  ${swagger_url})
  wget --output-document "${filename}" "${url}"
}

gen_servers() {
  local swagger_url="$(get_swagger_url $(git rev-parse HEAD))"
  case $swagger_url in
    *swagger.yaml*) echo "Using HEAD commit." ;;
    *) local swagger_url="$(get_swagger_url)"
  esac
  # TODO: Case statement for other server types
  gen_servers_python_flask "${swagger_url}"
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Bash Strict Mode
    set -eu -o pipefail
    set -x
    gen_servers "$@"
fi

