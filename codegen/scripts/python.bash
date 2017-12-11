#!/usr/bin/env bash

GITROOT="${GITROOT-$(readlink -f ./$(git rev-parse --show-cdup))}"
source ${GITROOT}/codegen/scripts/_codegen.bash

codegen_configure()
{

    # swagger_codegen config-help -l python
    # CONFIG OPTIONS
    #         packageName
    #             python package name (convention: snake_case). (Default: swagger_client)

    #         projectName
    #             python project name in setup.py (e.g. petstore-api).

    #         packageVersion
    #             python package version. (Default: 1.0.0)

    #         packageUrl
    #             python package URL.

    #         sortParamsByRequiredFlag
    #             Sort method arguments to place required parameters before optional parameters. (Default: true)

    #         hideGenerationTimestamp
    #             hides the timestamp when files were generated (Default: true)

    #         library
    #             library template (sub-template) to use (Default: urllib3)

cat <<EOF > ${GITROOT}/codegen/config/python.json
{
    "packageName" : "ngenetzky_py_client"
}
EOF
}

codegen_generate()
{
    swagger_codegen \
        generate \
        -l python -t /gen/modules/swagger-codegen/src/main/resources/python \
        -i /workdir/api/swagger.yaml \
        -o /workdir/codegen/python/ \
        -c /workdir/codegen/config/python.json
}

main()
{
    codegen_configure
    codegen_generate
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi

