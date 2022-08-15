# pip install request
import requests

class ServerBridge:

    def __init__(self):
        self.url = "http://54.214.117.174/controlcar_uisrael/php/"
    
    def post(self, params = None):
        response = requests.post(self.url, params)
        return response.json()
    
    def get(self, module, params = None):
        try:
            response = requests.get(url = self.url + module, params = params)
            return response.json()
        except:
            print("Sin Acceso de Internet")
            return {'estado': False}
         