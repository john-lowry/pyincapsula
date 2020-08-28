#!/usr/bin/env pyton3

"""Modifies a sites ACL rules

 site_id -- numerical site id to retrive
 rule_id -- rule to change
 listed -- list things to send for the rule
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
"""

from .com_error import errorProcess
from .sendRequest import ApiCredentials, ApiUrl, makeRequest

api_creds = ApiCredentials()
api_endpoint = ApiUrl.api_endpoint


def modSiteACL(site_id, rule_id, listed):
    try:
        if rule_id == 'api.acl.blacklisted_countries':
            payload = {
                'api_id': api_creds.api_id,
                'api_key': api_creds.api_key,
                'site_id': site_id,
                'rule_id': rule_id,
                'countries': listed
            }
        if rule_id == 'api.acl.blacklisted_urls':
            payload = {
                'api_id': api_creds.api_id,
                'api_key': api_creds.api_key,
                'site_id':site_id,
                'rule_id':rule_id,
                'urls':listed
            }
        if rule_id == 'api.acl.blacklisted_ips':
            payload = {
                'api_id': api_creds.api_id,
                'api_key': api_creds.api_key,
                'site_id':site_id,
                'rule_id':rule_id,
                'ips':listed
            }
        if rule_id == 'api.acl.whitelisted_ips':
            payload = {
                'api_id': api_creds.api_id,
                'api_key': api_creds.api_key,
                'site_id':site_id,
                'rule_id':rule_id,
                'ips':listed
            }
        url = api_endpoint + 'prov/v1/sites/configure/acl'
        r = makeRequest(url, payload)
        return r.text
    except Exception as error:
        return errorProcess(error)