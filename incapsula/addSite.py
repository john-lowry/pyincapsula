#!/usr/bin/env python3
"""Create a new site

Creates a new site in Incapsula under the specified account.
After running you will recive an email from Incapsula with further
instructions to finnish verifing and setting up the site.
 domain -- the domain name for the site
 account_id -- sub-account to associate the site with
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
"""

import os
import requests
from .com_error import errorProcess

api_endpoint = 'https://my.incapsula.com/api/'


def addSite(domain, account_id,
        api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url= api_endpoint + 'prov/v1/sites/add'
    try:
        payload = {
            'api_id':api_id,
            'api_key':api_key,
            'domain':domain,
            'account_id':account_id,
            'send_site_setup_emails':'true'
        }
        r = requests.post(url, data=payload)
        return r.text
    except Exception as error:
        return errorProcess(error)