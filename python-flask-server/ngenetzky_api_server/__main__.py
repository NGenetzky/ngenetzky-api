#!/usr/bin/env python3

import connexion

from ngenetzky_api_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'NGenetzky&#39;s API'})
    app.run(port=80)


if __name__ == '__main__':
    main()
