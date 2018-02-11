#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'This is an API I am designing for myself using swagger. You can find  out more about Swagger at [http://swagger.io](http://swagger.io) '})
    app.run(port=80)
