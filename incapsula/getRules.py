#!/usr/bin/env python3
import os
import requests
from .com_error import errorProcess

api_endpoint = 'https://my.incapsula.com/api/'

# https://docs.incapsula.com/Content/API/sites-api.htm#List3
# Returns all site assosiated with the provided account
def getRules(site_id,page=0,page_size=100,include_ad_rules='Yes',
        include_incap_rules='yes', api_id=os.environ.get('API_ID'),
        api_key=os.environ.get('API_KEY')):
    # https://docs.incapsula.com/Content/API/sites-api.htm#List
    url = api_endpoint+'prov/v1/sites/incapRules/list'
    try:
        payload = {
            'api_id':api_id,
            'api_key':api_key,
            'site_id':site_id,
            'include_ad_rules':include_ad_rules,
            'include_incap_rules':include_incap_rules,
            'page_size':page_size,
            'page_num':page
        }
        r = requests.post(url, data=payload)
        return r.text
    except Exception as error:
        return errorProcess(error)