#!python3
import os
import requests

api_endpoint = 'https://my.incapsula.com/api/'

# Returns all site assosiated with the provided account
def getSites(account,page,page_size=100,
        api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    # https://docs.incapsula.com/Content/API/sites-api.htm#List
    url = api_endpoint+'prov/v1/sites/list'
    payload = {
        'api_id':api_id,
        'api_key':api_key,
        'account_id':account,
        'page_size':page_size,
        'page_num':page
    }
    r = requests.post(url, data=payload)
    return r.text