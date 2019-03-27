#!/usr/bin/env python3

"""Changes the TLS supported by the site

 site_id -- numerical site id to retrive
 support_all_tls_versions -- boolen to support all versions of TLS\
 (Default: True)
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
"""

import os
import requests
from .com_error import errorProcess

api_endpoint = 'https://my.incapsula.com/api/'

# Requires Site_ID and if all versions of TLS should be supported
def modTLS(
        site_id, support_all_tls_versions='true',
        api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url = api_endpoint+'prov/v1/sites/tls'
    try:
        support_all_tls_versions = str(support_all_tls_versions).lower()
        payload = {
            'api_id':api_id,
            'api_key':api_key,
            'site_id':site_id,
            'support_all_tls_versions':support_all_tls_versions
        }
        r = requests.post(url, data=payload)
        return r.text
    except Exception as error:
        return errorProcess(error)