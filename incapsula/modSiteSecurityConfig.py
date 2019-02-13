#!/usr/bin/python

import os
import requests

api_endpoint='https://my.incapsula.com/api/'

def modSiteSecurityConfig(site_id,rule_id,value,api_id=os.environ.get('API_ID'),api_key=os.environ.get('API_KEY'),chal_sus_bot='true'):
    url=api_endpoint+'prov/v1/sites/configure/security'
    if rule_id=='api.threats.ddos':
        payload={
            'api_id':api_id,
            'api_key':api_key,
            'site_id':site_id,
            'rule_id':rule_id,
            'activation_mode':'api.threats.ddos.activiation_mode.auto', #This is required, can also be on
            'ddos_traffic_threshold':value
        }
    elif rule_id=='api.threats.bot_access_control':
        payload={
            'api_id':api_id,
            'api_key':api_key,
            'site_id':site_id,
            'rule_id':rule_id,
            'block_bad_bots':value,
            'challenge_suspected_bots':chal_sus_bot
        }
    else:
        return 1
    r=requests.post(url, data=payload)
    return r.text

