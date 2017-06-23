#!/usr/bin/python

import os
import requests

api_endpoint='https://my.incapsula.com/api/'
api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')

'''
def addSite
'''

def getSiteStatus(site_id, api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url=api_endpoint + 'prov/v1/sites/status'
    payload={'api_id': api_id,'api_key': api_key, 'site_id': site_id}
    r = requests.post(url, data=payload)
    return r.text

'''
def getDomainApproverEmail
'''

'''
def modSiteConfig
'''

'''
def modSiteLogLevel
'''

'''
def modSiteSecurityConfig
'''

'''
def modSiteACL
'''

'''
def modWhitelistConfig
'''

'''
def delSite
'''

def listSites(api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url=api_endpoint + 'prov/v1/sites/list'
    payload={'api_id': api_id,'api_key': api_key}
    r = requests.post(url, data=payload)
    return r.text

'''
def getSiteReport
'''

'''
def purgeSiteCache
'''

'''
def modCacheMode
'''

'''
def getStats
'''

'''
def getVisits
'''

'''
def uploadPubKey
'''

'''
def changeLogCollectorStatus
'''

'''
def addLoginProtectUser
'''

'''
def editLoginProtectUser
'''

'''
def getLoginProtectUsers
'''

'''
def rmLoginProtectUser
'''

'''
def sendSMStoUser
'''

'''
def modSiteLoginProtectConfig
'''

'''
def configLoginProtectOnAdmin
'''

'''
def getIPRanges
'''

'''
def getTexts
'''

'''
def getGeoInfo
'''

'''
def getClientAppInfo
'''
