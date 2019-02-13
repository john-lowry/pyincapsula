#!python3

# Changes security settings for the sepesified site
# Requires Site ID, the rule id, and, the value to assign
# Values are either a number (DDoS) True/False (Bot Blocking) or the action 
# without the api.threats.action portion, as that is appended
# 
# For Bot blocking we assume that we should challange suspected bot unless told otherwise
# Valid values are listed at: https://docs.incapsula.com/Content/API/sites-api.htm#Modify3
# This is only a partial implementation, more still needs to be added

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
            'activation_mode':'api.threats.ddos.activation_mode.auto', #This is required, can also be on
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
    elif rule_id=='api.threats.remote_file_inclusion'\
        or rule_id=='api.threats.sql_injection'\
        or rule_id=='api.threats.cross_site_scripting'\
        or rule_id=='api.threats.illegal_resource_access'\
        or rule_id=='api.threats.backdoor':
        value='api.threats.action.'+value
        payload={
            'api_id':api_id,
            'api_key':api_key,
            'site_id':site_id,
            'rule_id':rule_id,
            'security_rule_action':value
        }
    else:
        return 1
    r=requests.post(url, data=payload)
    return r.text
