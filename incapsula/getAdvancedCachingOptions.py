#!/usr/bin/env python3

"""Returns the JSON advanced caching status for a site

 param -- the specific caching status for a site
 site_id -- numerical site id to retrive
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
"""

from .com_error import errorProcess
from .sendRequest import ApiCredentials, ApiUrl, makeRequest

api_creds = ApiCredentials()
api_endpoint = ApiUrl.api_endpoint

def getAdvancedCachingOptions(site_id, param):
    url = api_endpoint + 'prov/v1/sites/performance/advanced/get'
    try:
        payload = {
            'api_id': api_creds.api_id,
            'api_key': api_creds.api_key,
            'site_id': site_id,
            'param': param
        }
        r = makeRequest(url, payload)
        return r.text
    except Exception as error:
        return errorProcess(error)
