#!/usr/bin/env bash

GITROOT="${GITROOT-$(readlink -f ./$(git rev-parse --show-cdup))}"
source ${GITROOT}/docker/scripts/_docker.bash

do_fetch()
{
    rm -rf "${GITROOT?}/docker/python-flask"
    cp -r -T \
        "${GITROOT}/codegen/python-flask" \
        "${GITROOT}/docker/python-flask"
}

docker_build()
{
    docker build \
        -t ${DOCKER_USER?}/python-flask:0.0.1 \
        "${GITROOT}/docker/python-flask"
}

docker_run()
{
    docker run -d \
        -p 9001:8080 \
        ${DOCKER_USER?}/python-flask:0.0.1
}

main()
{
    do_fetch
    docker_build
    docker_run
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi

