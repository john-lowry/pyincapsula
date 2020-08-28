#!/usr/bin/env python3

"""Modifies a sites logging level

 site_id -- numerical site id to retrive
 log level -- log level to set
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
"""

from .com_error import errorProcess
from .sendRequest import ApiCredentials, ApiUrl, makeRequest

api_creds = ApiCredentials()
api_endpoint = ApiUrl.api_endpoint

def modSiteLogLevel(site_id, log_level):
    url = api_endpoint + 'prov/v1/sites/setlog'
    try:
        payload = {
            'api_id': api_creds.api_id,
            'api_key': api_creds.api_key,
            'site_id': site_id,
            'log_level': log_level
        }
        r = makeRequest(url, payload)
        return r.text
    except Exception as error:
        return errorProcess(error)