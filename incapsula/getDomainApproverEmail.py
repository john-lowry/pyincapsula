#!/usr/bin/python

# Returns emails that can be used to add SSL
# Requires the domain of the site

import os
import requests

api_endpoint='https://my.incapsula.com/api/'


def getDomainApproverEmail(domain,api_id=os.environ.get('API_ID'),api_key=os.environ.get('API_KEY')):
    url= api_endpoint+'prov/v1/domain/emails'
    payload={
        'api_id':api_id,
        'api_key':api_key,
        'domain':domain
    }
    r = requests.post(url, data=payload)
    return r.text
