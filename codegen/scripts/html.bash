#!/usr/bin/env bash

GITROOT="${GITROOT-$(readlink -f ./$(git rev-parse --show-cdup))}"
source ${GITROOT}/codegen/scripts/_codegen.bash

codegen_configure()
{

    # swagger_codegen config-help -l html
    # CONFIG OPTIONS
    #         sortParamsByRequiredFlag
    #             Sort method arguments to place required parameters before optional parameters. (Default: true)

    #         ensureUniqueParams
    #             Whether to ensure parameter names are unique in an operation (rename parameters that are not). (Default: true)

    #         allowUnicodeIdentifiers
    #             boolean, toggles whether unicode identifiers are allowed in names or not, default is false (Default: false)

    #         appName
    #             short name of the application

    #         appDescription
    #             description of the application

    #         infoUrl
    #             a URL where users can get more information about the application

    #         infoEmail
    #             an email address to contact for inquiries about the application

    #         licenseInfo
    #             a short description of the license

    #         licenseUrl
    #             a URL pointing to the full license

    #         invokerPackage
    #             root package for generated code

    #         groupId
    #             groupId in generated pom.xml

    #         artifactId
    #             artifactId in generated pom.xml

    #         artifactVersion
    #             artifact version in generated pom.xml

cat <<EOF > ${GITROOT}/codegen/config/html.json
{
    "appName" : "ngenetzky_api",
    "appDescription" : "Playing out an idea I have using swagger.",
    "infoUrl" : "https://github.com/NGenetzky/ngenetzky-api",
    "infoEmail" : "nathan@genetzky.us",
    "licenseInfo" : "MIT",
    "licenseUrl" : "https://github.com/NGenetzky/ngenetzky-api/blob/master/LICENSE",
    "invokerPacakge" : "ngenetzky_api"
}
EOF
}

codegen_generate()
{
    swagger_codegen \
        generate \
        -l html -t /gen/modules/swagger-codegen/src/main/resources/htmlDocs2/ \
        -i /workdir/api/swagger.yaml \
        -o /workdir/codegen/html/ \
        -c /workdir/codegen/config/html.json
}

main()
{
    codegen_configure
    codegen_generate
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi

