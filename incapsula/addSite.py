#!/usr/bin/env python3
"""Create a new site

Creates a new site in Incapsula under the specified account.
After running you will recive an email from Incapsula with further
instructions to finnish verifing and setting up the site.
 domain -- the domain name for the site
 account_id -- sub-account to associate the site with
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
 site_ip -- manually set the web server IP/CNAME aka Origin Server
"""

from .com_error import errorProcess
from .sendRequest import ApiCredentials, ApiUrl, makeRequest

api_creds = ApiCredentials()
api_endpoint = ApiUrl.api_endpoint

def addSite(domain, account_id, site_ip):
    url = api_endpoint + 'prov/v1/sites/add'
    try:
        payload = {
            'api_id': api_creds.api_id,
            'api_key': api_creds.api_key,
            'domain': domain,
            'account_id': account_id,
            'send_site_setup_emails': 'true',
            'site_ip': site_ip,
            'force_ssl': 'true'
        }
        r = makeRequest(url, payload)
        return r.text
    except Exception as error:
        return errorProcess(error)