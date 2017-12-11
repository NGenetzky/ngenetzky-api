#!/usr/bin/env bash

GITROOT="${GITROOT-$(readlink -f ./$(git rev-parse --show-cdup))}"
SWAGGER_CODEGEN_DIR='/home/ngenetzky/workspaces/swagger/swagger-codegen'

swagger_codegen() {
    local maven_cache_repo="${HOME}/.m2/repository"
    mkdir -p "${maven_cache_repo}"

    docker run --rm -it \
            -w /gen \
            -e GEN_DIR=/gen \
            -e MAVEN_CONFIG=/var/maven/.m2 \
            -u "$(id -u):$(id -g)" \
            -v "${SWAGGER_CODEGEN_DIR?}:/gen" \
            -v "${maven_cache_repo}:/var/maven/.m2/repository" \
            -v "${GITROOT}:/workdir/" \
            --entrypoint /gen/docker-entrypoint.sh \
            maven:3-jdk-7 "$@"
}
