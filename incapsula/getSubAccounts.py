#!python3

import os
import requests

api_endpoint='https://my.incapsula.com/api/'

# Returns all sub accounts that the api id can see
def getSubAccounts(api_id=os.environ.get('API_ID'),api_key=os.environ.get('API_KEY')):
    # https://docs.incapsula.com/Content/API/accounts-api.htm#List2
    url=api_endpoint+'prov/v1/accounts/listSubAccounts'
    payload={
        'api_id':api_id,
        'api_key':api_key
    }
    r=requests.post(url, data=payload)
    return r.text