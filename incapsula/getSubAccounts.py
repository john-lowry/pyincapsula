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

import os
import requests
import json
from .com_error import errorProcess

api_endpoint = 'https://my.incapsula.com/api/'

def getSubAccounts(page=0,page_size=30,recursive=True,account_id=None,
        api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url=api_endpoint+'prov/v1/accounts/listSubAccounts'
    run=True
    try:
        while run==True:
            payload = {
                'api_id':api_id,
                'api_key':api_key,
                'page_size':page_size,
            }
            if page > 0:
                payload.update({'page_num':page})
            if account_id is not None:
                payload.update({'account_id':account_id})
            r = requests.post(url, data=payload)
            results = json.loads(r.text)
            if recursive:
                max_results=page_size-1
                # This is the first page, start the output
                if page==0:
                    out_json=results
                    page=page+1
                # Find out if this is a standard page or the end of the line
                # (EOTL)
                elif len(results['resultList'])>max_results:
                    out_json['resultList'].extend(results['resultList'])
                    page=page+1
                # Last page was the end, no more objects, EOTL
                elif len(results.get('res_message')) is 'OK':
                    run=False
                # This is the last page, less then the max objects EOTL
                else:
                    out_json['resultList'].extend(results['resultList'])
                    run=False
            else:
                out_json=results
                run=False
        return json.dumps(out_json)
    except Exception as error:
        return errorProcess(error)