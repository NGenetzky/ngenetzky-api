#!/usr/bin/env bash

GITROOT="${GITROOT-$(readlink -f ./$(git rev-parse --show-cdup))}"
source ${GITROOT}/codegen/scripts/_codegen.bash

codegen_configure()
{

    # swagger_codegen config-help -l python-flask
    # CONFIG OPTIONS
    #         sortParamsByRequiredFlag
    #             Sort method arguments to place required parameters before optional parameters. (Default: true)

    #         ensureUniqueParams
    #             Whether to ensure parameter names are unique in an operation (rename parameters that are not). (Default: true)

    #         allowUnicodeIdentifiers
    #             boolean, toggles whether unicode identifiers are allowed in names or not, default is false (Default: false)

    #         packageName
    #             python package name (convention: snake_case). (Default: swagger_server)

    #         packageVersion
    #             python package version. (Default: 1.0.0)

    #         controllerPackage
    #             controller package (Default: controllers)

    #         defaultController
    #             default controller (Default: default_controller)

    #         supportPython2
    #             support python2 (Default: false)

    #         serverPort
    #             TCP port to listen to in app.run (Default: 8080)


cat <<EOF > ${GITROOT}/codegen/config/python-flask.json
{
    "packageName" : "ngenetzky_py_server"
}
EOF
}

codegen_generate()
{
    swagger_codegen \
        generate \
        -l python-flask -t /gen/modules/swagger-codegen/src/main/resources/flaskConnexion \
        -i /workdir/api/swagger.yaml \
        -o /workdir/codegen/python-flask/ \
        -c /workdir/codegen/config/python-flask.json
}

main()
{
    codegen_configure
    codegen_generate
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi

