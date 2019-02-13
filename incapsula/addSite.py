#!/usr/bin/python
  
import os
import requests

api_endpoint='https://my.incapsula.com/api/'


def addSite(domain, account_id, api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url= api_endpoint + 'prov/v1/sites/add'
    payload={'api_id': api_id, 'api_key': api_key, 'domain': domain, 'account_id': account_id, 'send_site_setup_emails': 'true'}
    r = requests.post(url, data=payload)
    return r.text
