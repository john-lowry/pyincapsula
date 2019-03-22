#!/usr/bin/env pyton3

"""Modifies a sites ACL rules

 site_id -- numerical site id to retrive
 rule_id -- rule to change
 listed -- list things to send for the rule
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
"""

import os
import requests
from .com_error import errorProcess

api_endpoint = 'https://my.incapsula.com/api/'


def modSiteACL(site_id, rule_id, listed,
        api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    try:
        if rule_id == 'api.acl.blacklisted_countries':
            payload = {
                'api_id':api_id,
                'api_key':api_key,
                'site_id':site_id,
                'rule_id':rule_id,
                'countries':listed
            }
        if rule_id == 'api.acl.blacklisted_urls':
            payload = {
                'api_id':api_id,
                'api_key':api_key,
                'site_id':site_id,
                'rule_id':rule_id,
                'urls':listed
            }
        if rule_id == 'api.acl.blacklisted_ips':
            payload = {
                'api_id':api_id,
                'api_key':api_key,
                'site_id':site_id,
                'rule_id':rule_id,
                'ips':listed
            }
        if rule_id == 'api.acl.whitelisted_ips':
            payload = {
                'api_id':api_id,
                'api_key':api_key,
                'site_id':site_id,
                'rule_id':rule_id,
                'ips':listed
            }
        url = api_endpoint + 'prov/v1/sites/configure/acl'
        r = requests.post(url, data=payload)
        return r.text
    except Exception as error:
        return errorProcess(error)