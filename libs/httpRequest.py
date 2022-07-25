# pip install request
import requests

class ServerBridge:

    def __init__(self):
        self.url = "http://54.200.49.87/uisrael/"
    
    def post(self, params = None):
        response = requests.post(self.url, params)
        return response.json()
    
    def get(self, module, params = None):
        response = requests.get(url = self.url + module, params = params)
        return response.json() 