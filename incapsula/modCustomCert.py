#!python3
import os
import requests
import base64

api_endpoint = 'https://my.incapsula.com/api/'

# Requires the Site_ID, location of the certificate file, location of
# the Private Key file, and the passphrase if required
def modCustomCert(site_id, certificate, private_key, passphrase,
        api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    try:
        with open(certificate,'rb') as certFile:
            read = certFile.read()
            cert = base64.b64encode(read)
    except:
        print('Certificate could not be read')
        print(EnvironmentError)
    try:
        with open(private_key,'rb') as privFile:
            read = privFile.read()
            privKey = base64.b64encode(privFile)
    except:
        print('Private Key could not be read')
        print(EnvironmentError)
    url = api_endpoint + 'prov/v1/customCertificate/upload'
    if(passphrase is not None):
        payload = {
            'api_id':api_id,
            'api_key':api_key,
            'site_id':site_id,
            'certificate':cert,
            'private_key':privKey,
            'passphrase':passphrase
        }
    else:
        payload = {
            'api_id':api_id,
            'api_key':api_key,
            'site_id':site_id,
            'certificate':cert,
            'private_key':privKey
        }
    r = requests.post(url, data=payload)
    return r.text
