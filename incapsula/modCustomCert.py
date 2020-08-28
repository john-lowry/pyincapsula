#!/usr/bin/env python3

"""Uploads a custom certificate for a site

Requires the Site_ID, location of the certificate file, location of the 
Private Key file, and the passphrase if required

 site_id -- numerical site id to retrive
 certificate -- file location of the certificate to upload
 private_key -- file location of the private key for the certificate
 passphrase -- passphrase for the private key (Default: None)
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
"""

import base64
from .com_error import errorProcess
from .sendRequest import ApiCredentials, ApiUrl, makeRequest

api_creds = ApiCredentials()
api_endpoint = ApiUrl.api_endpoint

# Requires the Site_ID, location of the certificate file, location of
# the Private Key file, and the passphrase if required
def modCustomCert(site_id, certificate, private_key, passphrase=None):
    try:
        with open(certificate,'rb') as certFile:
            read = certFile.read()
            cert = base64.b64encode(read)
    except EnvironmentError as error:
        return errorProcess(error,str(certificate)+'Certificate could not be read')
    except Exception as error:
        return errorProcess(error)
    try:
        with open(private_key,'rb') as privFile:
            read = privFile.read()
            privKey = base64.b64encode(privFile)
    except EnvironmentError as error:
        return errorProcess(error,str(private_key)+'Private Key could not be read')
    except Exception as error:
        return errorProcess(error)
    url = api_endpoint + 'prov/v1/customCertificate/upload'
    try:
        if(passphrase is not None):
            payload = {
                'api_id': api_creds.api_id,
                'api_key': api_creds.api_key,
                'site_id': site_id,
                'certificate': cert,
                'private_key': privKey,
                'passphrase': passphrase
            }
        else:
            payload = {
                'api_id': api_creds.api_id,
                'api_key': api_creds.api_key,
                'site_id': site_id,
                'certificate': cert,
                'private_key': privKey
            }
        r = makeRequest(url, payload)
        return r.text
    except Exception as error:
        return errorProcess(error)