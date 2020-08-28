#!/usr/bin/env python3

"""Depreciated Site listing module, DO NOT USE

 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
 """

from .com_error import errorProcess
from .sendRequest import ApiCredentials, ApiUrl, makeRequest

api_creds = ApiCredentials()
api_endpoint = ApiUrl.api_endpoint

def listSites():
    url = api_endpoint + 'prov/v1/sites/list'
    try:
        payload = {
            'api_id': api_creds.api_id,
            'api_key': api_creds.api_key,
            'page_size': 100
        }
        r = makeRequest(url, payload)
        return r.text
    except Exception as error:
        return errorProcess(error)