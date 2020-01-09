import sys
import os
from os.path import dirname
from os.path import join

UPLOAD_DIRECTORY = "api_uploaded_files"
sys.path.insert(0, join(dirname(__file__), 'src'))

from nextcloud import NextCloud

class NextCloudIntegration:    
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

        to_js = True
        self.nxc = NextCloud(endpoint=url, user=username, password=password, json_output=to_js)

    def get_list_folder(self, path_name=None, file_name=None, with_files=True):
        if file_name is not None:
            path_name = os.path.join(path_name,file_name)
        list_folders_response = self.nxc.list_folders(self.username, path=path_name, all_properties=True)
        
        if not list_folders_response.is_ok:
            return None
            
        if with_files is False:
            return list(filter(lambda x: x['resource_type'] == 'collection', list_folders_response.data))
        
        return list_folders_response.data
    
    def get_list_relative_folder(self, path_name=None, file_name=None, with_files=True):
        folders = self.get_list_folder(path_name, file_name, with_files)
        if folders is None: return folders 

        for folder in folders:
            k = folder['href'].find(self.username)
            folder['href'] = folder['href'][(k+len(self.username)+1):]
            
        return folders

    def get_file_list(self, path_name=None):
        folders = self.get_list_folder(path_name)
        if folders is None:
            return None

        return list(filter(lambda x: x['resource_type'] is None, folders))

    def download_file(self, file_path, destination_path=None):        
        folders = self.get_list_folder(file_path)
        if folders is None:
            return None

        if folders[0]['href'] is None:
            return None
        
        local_file_path = self.nxc.download_file(self.username, file_path, destination_path)
        return local_file_path
        
