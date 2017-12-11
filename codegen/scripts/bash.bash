#!/usr/bin/env bash

GITROOT="${GITROOT-$(readlink -f ./$(git rev-parse --show-cdup))}"
source ${GITROOT}/codegen/scripts/_codegen.bash

codegen_configure()
{

    # swagger_codegen config-help -l bash
    # CONFIG OPTIONS
    #         sortParamsByRequiredFlag
    #             Sort method arguments to place required parameters before optional parameters. (Default: true)

    #         ensureUniqueParams
    #             Whether to ensure parameter names are unique in an operation (rename parameters that are not). (Default: true)

    #         allowUnicodeIdentifiers
    #             boolean, toggles whether unicode identifiers are allowed in names or not, default is false (Default: false)

    #         curlOptions
    #             Default cURL options

    #         processMarkdown
    #             Convert all Markdown Markup into terminal formatting (Default: false)

    #         scriptName
    #             The name of the script that will be generated (e.g. petstore-cli)

    #         generateBashCompletion
    #             Whether to generate the Bash completion script (Default: false)

    #         generateZshCompletion
    #             Whether to generate the Zsh completion script (Default: false)

    #         hostEnvironmentVariable
    #             Name of environment variable where host can be defined (e.g. PETSTORE_HOST='http://petstore.swagger.io:8080')

    #         basicAuthEnvironmentVariable
    #             Name of environment variable where username and password can be defined (e.g. PETSTORE_CREDS='username:password')

    #         apiKeyAuthEnvironmentVariable
    #             Name of environment variable where API key can be defined (e.g. PETSTORE_APIKEY='kjhasdGASDa5asdASD') (Default: false)

cat <<EOF > ${GITROOT}/codegen/config/bash.json
{
    "processMarkdown" : "false",
    "scriptName" : "ngenetzky_bash_client",
    "hostEnvironmentVariable" : "NGENETZKY_HOST",
    "basicAuthEnvironmentVariable" : "NGENETZKY_AUTH",
    "apiKeyAuthEnvironmentVariable" : "NGENETZKY_APIKEY"
}
EOF
}

codegen_generate()
{
    swagger_codegen \
        generate \
        -l bash -t /gen/modules/swagger-codegen/src/main/resources/bash/ \
        -i /workdir/api/swagger.yaml \
        -o /workdir/codegen/bash/ \
        -c /workdir/codegen/config/bash.json
}

main()
{
    codegen_configure
    codegen_generate
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi

