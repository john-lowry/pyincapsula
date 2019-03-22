#!/usr/bin/env python3

"""Changes security settings for the spesified site
Requires FQDN, the rule id, and, the value to assign
Values are either a number (DDoS) True/False (Bot Blocking) or the
action without the api.threats.action portion, as that is appended

For Bot blocking we assume that we should challange suspected bot
unless told otherwise.

Valid values are listed at:
https://docs.incapsula.com/Content/API/sites-api.htm#Modify3
This is only a partial implementation, more still needs to be added

 site_id -- numerical site id to retrive (Default: None)
 rule_id -- rule to change (Default: None)
 value -- value to set (Default: None)
 chal_sus_bot -- challenge suspected bots, only use on\
 api.theats.bot_access_control (Default: True)
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
"""

import os
import requests
from .com_error import errorProcess

api_endpoint = 'https://my.incapsula.com/api/'

def modSiteSecurityConfig(site_id=None,rule_id=None,value=None,
        chal_sus_bot='true',api_id=os.environ.get('API_ID'),
        api_key=os.environ.get('API_KEY')):
    url = api_endpoint+'prov/v1/sites/configure/security'
    try: # Setup the payload
        assert site_id is not None
        if rule_id == 'api.threats.ddos':
            payload = {
                'api_id':api_id,
                'api_key':api_key,
                'site_id':site_id,
                'rule_id':rule_id,
                'activation_mode':'api.threats.ddos.activation_mode.auto',
                'ddos_traffic_threshold':value
            }
        elif rule_id == 'api.threats.bot_access_control':
            value = str(value).lower()
            chal_sus_bot = str(chal_sus_bot).lower()
            payload = {
                'api_id':api_id,
                'api_key':api_key,
                'site_id':site_id,
                'rule_id':rule_id,
                'block_bad_bots':value,
                'challenge_suspected_bots':chal_sus_bot
            }
        elif rule_id == 'api.threats.remote_file_inclusion'\
            or rule_id == 'api.threats.sql_injection'\
            or rule_id == 'api.threats.cross_site_scripting'\
            or rule_id == 'api.threats.illegal_resource_access'\
            or rule_id == 'api.threats.backdoor':
            value = 'api.threats.action.' + str(value).lower()
            payload = {
                'api_id':api_id,
                'api_key':api_key,
                'site_id':site_id,
                'rule_id':rule_id,
                'security_rule_action':value
            }
    except AssertionError as error:
        return errorProcess(error,site_id)
    except Exception as error:
        return errorProcess(error)
    try: # Deliver the payload
        r = requests.post(url, data=payload)
        r.raise_for_status()
        return r.text
    except NameError as error:
        return errorProcess(error,'Rule ID')
    except Exception as error:
        return errorProcess(error)