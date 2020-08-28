#!/usr/bin/env python3

"""Gathers a list of all sub accounts

Returns all sub accounts by default and itterates throught pagination.
Does not require any argument be default to return all sub accounts.
https://docs.incapsula.com/Content/API/accounts-api.htm#List2

 page -- Page to start listing sub accounts (Default: 0)
 page_size -- Number of objects per page (Default: 100)
 recursive -- determine if the function should loop through pagination\
 (Default: True)
 account_id -- account id to operate on (Default: None)
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
"""

import json
from .com_error import errorProcess
from .sendRequest import ApiCredentials, ApiUrl, makeRequest

api_creds = ApiCredentials()
api_endpoint = ApiUrl.api_endpoint

def getSubAccounts(page=0, page_size=30, recursive=True, account_id=None):
    url= api_endpoint+'prov/v1/accounts/listSubAccounts'
    payload = {
        'api_id': api_creds.api_id,
        'api_key': api_creds.api_key,
        'page_size': page_size,
        'page_num': page
    }
    if account_id is not None:
        payload['account_id']= account_id
    try:
        r = makeRequest(url, payload)
        results = json.loads(r.text)
        if recursive and results['res'] == 0:
            max_objects= page_size
            out_json = results # Setups up initial out_json object
            # We can't have more then the max, and if we have less, then
            # we already have all the data and it's time to move on.
            while len(results['resultList']) == max_objects:
                payload['page_num']=payload['page_num']+1
                r = makeRequest(url, payload)
                results = json.loads(r.text)
                out_json['resultList'].extend(results['resultList'])
        else:
            out_json= results
        return json.dumps(out_json)
    except Exception as error:
        return errorProcess(error)