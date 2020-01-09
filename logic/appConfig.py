import json

class AppConfig:
    url = ''
    username=''
    password=''

    def __init__(self, url, username, password):

        if not url:
            raise Exception('required url is empty')
        AppConfig.url = url

        if not username:
            raise Exception('required username is empty')
        AppConfig.username = username

        if not password:
            raise Exception('required password is empty')
        AppConfig.password = password

    @classmethod
    def from_json(cls, file_name):
        loaded_json = {}
        with open(file_name, 'r') as f:
            loaded_json = json.load(f)
        return cls(**loaded_json)

    
    @classmethod
    def init(cls, CONFIG_FILE):
        AppConfig.from_json(CONFIG_FILE)