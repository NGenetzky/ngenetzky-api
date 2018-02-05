#!//bin/sh
DOCKER_USER='ngenetzky'
run()
{
    docker run -d \
        -p 9002:80 \
        ${DOCKER_USER?}/ngapi-python-flask-server:0.0.1
}
run $@
