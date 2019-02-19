#!python3
import os
import requests

api_endpoint = 'https://my.incapsula.com/api/'

# Requires Site_ID and if all versions of TLS should be supported
def modTLS(site_id, support_all_tls_versions='true',
        api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    support_all_tls_versions = str(support_all_tls_versions).lower()
    url = api_endpoint+'prov/v1/sites/tls'
    payload = {
        'api_id':api_id,
        'api_key':api_key,
        'site_id':site_id,
        'support_all_tls_versions':support_all_tls_versions
    }
    r = requests.post(url, data=payload)
    return r.text
