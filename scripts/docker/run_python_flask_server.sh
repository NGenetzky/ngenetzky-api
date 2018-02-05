#!//bin/sh
DOCKER_USER='ngenetzky'
run()
{
    docker run \
        -p 80:80 \
        -v "$(pwd)/data:/data:rw" \
        ${DOCKER_USER?}/ngapi-python-flask-server:0.0.1
}
run $@
