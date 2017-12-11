#!/usr/bin/env bash

# Bash Strict Mode
set -eu -o pipefail

PROJECT="ngenetzky-api"
GITROOT="${GITROOT-$(readlink -f ./$(git rev-parse --show-cdup))}"
source "${GITROOT}/docker/scripts/_docker.bash"

do_fetch()
{
    rm -rf "${GITROOT?}/docker/${PROJECT?}"
    mkdir -p "${GITROOT?}/docker/${PROJECT?}"

    cp -r -T -v \
        "${GITROOT}/codegen/python-flask" \
        "${GITROOT}/docker/${PROJECT?}/python-flask"

    cp -r -T -v \
        "${GITROOT}/codegen/bash" \
        "${GITROOT}/docker/${PROJECT?}/bash"

    cp -r -T -v \
        "${GITROOT}/codegen/python" \
        "${GITROOT}/docker/${PROJECT?}/python"
    cp -r -T -v \
        "${GITROOT}/src/ngenetzky_py_client" \
        "${GITROOT}/docker/${PROJECT?}/python"

}

docker_configure()
{
cat <<EOF > "${GITROOT?}/docker/${PROJECT?}/docker-compose.yaml"
version: '2'

services:

  python-flask:
    build: ./python-flask
    ports:
    - "127.0.0.1:9001:8080"

  bash:
    build: ./bash
    links:
      - "python-flask:server"
    environment:
      NGENETZKY_HOST: "server:8080"
    # CLI mode:
    # command: ["-c", "ngenetzky_bash_client --help"]
    # Interactive mode:
    tty: true
    stdin_open: true

  ui:
    image: swaggerapi/swagger-ui:v2.2.9
    links:
      - "python-flask:server"
    ports:
    - "127.0.0.1:9002:8080"
    environment:
      API_URL: "http://server:8080/nathansen/ngenetzky/api/swagger.json"

  python:
    build: ./python
    links:
      - "python-flask:server"
    environment:
      NGENETZKY_HOST: "server:8080"
    # CLI mode:
    # command: ["-m", "ngenetzky_py_client", "--", "--help"]
    # Interactive mode:
    entrypoint: "python3"
    tty: true
    stdin_open: true
EOF
}

docker_up()
{
    (
        cd "${GITROOT?}/docker/${PROJECT}" ; sleep 1 ;
        docker-compose up
    )
}

docker_run()
{
    (
        cd "${GITROOT?}/docker/${PROJECT}" ; sleep 1 ;
        docker-compose run $@
    )
}

main()
{
    do_fetch
    docker_configure
    docker_up
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    set -x
    main "$@"
fi

