# app.py - a minimal flask api using flask_restful
import os 
from flask import Flask, request
from flask_restplus import Resource, Api, fields, abort, reqparse
from logic.appConfig import AppConfig

CONFIG_FILE = "./keys/nextclud-access.json"
AppConfig.init(CONFIG_FILE)
#AppConfig.from_json(CONFIG_FILE)

app = Flask(__name__)
api = Api(app, 
    version='1.0.0',
    title='Python API: Flask, swagger',
    description='This is sample project to host Flask with swagger',
    validate=True)

from endpoints.storage_direcory_endpoint import *

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True, host='0.0.0.0', port=5000)