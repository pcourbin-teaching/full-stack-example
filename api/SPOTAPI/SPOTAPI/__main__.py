#!/usr/bin/env python3

import connexion
from flask_cors import CORS # To correct error 'Access-Control-Allow-Origin', see https://swagger.io/docs/open-source-tools/swagger-ui/usage/cors/
from SPOTAPI import encoder
import os
port = int(os.environ.get("PORT", 8080))

def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    CORS(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'SPOT API'},
                pythonic_params=True)
    app.run(port=port, debug=True)


if __name__ == '__main__':
    main()
