#!/usr/bin/env python3

"""Gathers a list of all sites

Returns all sites by default and itterates throught pagination.
Does not require any argument be default to return all sites.
https://docs.incapsula.com/Content/API/sites-api.htm#List

 account -- sub account to list sites for, ignored if None\
 (Default: None)
 page -- Page to start listing sites (Default: 0)
 page_size -- Number of objects per page (Default: 100)
 recursive -- determine if the function should loop through pagination\
 (Default: True)
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
"""

import os
import requests
import json
from .com_error import errorProcess

api_endpoint = 'https://my.incapsula.com/api/'

def getSites(
        account=None, page=0, page_size=100, recursive=True,
        api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url = api_endpoint+'prov/v1/sites/list'
    payload = {
        'api_id':api_id,
        'api_key':api_key,
        'page_size':page_size,
        'page_num':page
    }
    if account is not None:
        payload['account_id']=account
    try: 
        r = requests.post(url, data=payload)
        results = json.loads(r.text)
        if recursive and results['res'] == 0:
            max_objects=page_size
            out_json = results # Setups up initial out_json object
            # We can't have more then the max, and if we have less, then
            # we already have all the data and it's time to move on.
            while len(results['sites']) == max_objects:
                payload['page_num']=payload['page_num']+1
                r = requests.post(url, data=payload)
                results = json.loads(r.text)
                out_json['sites'].extend(results['sites'])
        else:
            out_json=results
        return json.dumps(out_json)
    except Exception as error:
        return errorProcess(error)