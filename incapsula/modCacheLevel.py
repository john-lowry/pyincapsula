#!/usr/bin/env python3

"""Enable or Disable caching for a specific site

 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)

 """

from .com_error import errorProcess
from .sendRequest import ApiCredentials, ApiUrl, makeRequest

api_creds = ApiCredentials()
api_endpoint = ApiUrl.api_endpoint

def modCacheLevel(cache_mode, site_id):
    url = api_endpoint + 'prov/v1/sites/performance/cache-mode'
    try:
        payload = {
            'api_id': api_creds.api_id,
            'api_key': api_creds.api_key,
            'site_id': site_id,
            'cache_mode': cache_mode
        }
        r = makeRequest(url, payload)
        return r.text
    except Exception as error:
        return errorProcess(error)