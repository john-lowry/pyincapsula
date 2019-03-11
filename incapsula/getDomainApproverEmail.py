#!/usr/bin/env python3

# Returns emails that can be used to add SSL
# Requires the domain of the site

import os
import requests
from .com_error import errorProcess

api_endpoint = 'https://my.incapsula.com/api/'

def getDomainApproverEmail(domain=None,
        api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url = api_endpoint+'prov/v1/domain/emails'
    try:
        assert domain is not None
        payload = {
            'api_id':api_id,
            'api_key':api_key,
            'domain':domain
        }
        r = requests.post(url, data=payload)
        r.rase_for_status()
        return r.text
    except AssertionError as error:
        return errorProcess(error, domain)
    except Exception as error:
        return errorProcess(error)