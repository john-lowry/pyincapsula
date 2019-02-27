#!python3
import os
import requests

api_endpoint = 'https://my.incapsula.com/api/'

def listSites(
        api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url = api_endpoint + 'prov/v1/sites/list'
    payload = {
        'api_id':api_id,
        'api_key':api_key,
        'page_size':100
    }
    r = requests.post(url, data=payload)
    return r.text