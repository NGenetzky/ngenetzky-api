#!/usr/bin/env bash

GITROOT="${GITROOT-$(readlink -f ./$(git rev-parse --show-cdup))}"
DOCKER_USER='ngenetzky'

