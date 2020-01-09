
import os
import werkzeug
from run import app, api, Resource, request, fields, abort, reqparse, AppConfig
from logic.nextcloudIntegration import NextCloudIntegration
from endpoints.models.get_direcotry_response import get_direcotry_response, get_direcotries_response

ns = api.namespace('Dierectory',
                   description='Show or search store directories')

@ns.route('', methods=['GET'])
@ns.route('/<path:direcotry>', methods=['GET'])
@ns.doc(params={'direcotry': 'Directory'})
class Get(Resource):
    @ns.marshal_with(get_direcotry_response, as_list=True, mask=False, code=200)
    def get(self, direcotry=None):              
        store = NextCloudIntegration(AppConfig.url, AppConfig.username, AppConfig.password)
        folders = store.get_list_relative_folder(path_name=direcotry, with_files=False)
        
        return folders
