#!/usr/bin/python

import os
import requests

api_endpoint='https://my.incapsula.com/api/'


def addSite(domain, account_id, api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url= api_endpoint + 'prov/v1/sites/add'
    payload={'api_id': api_id, 'api_key': api_key, 'domain': domain, 'account_id': account_id, 'send_site_setup_emails': 'true'}
    r = requests.post(url, data=payload)
    return r.text


def getSiteStatus(site_id, api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url=api_endpoint + 'prov/v1/sites/status'
    payload={'api_id': api_id,'api_key': api_key, 'site_id': site_id}
    r = requests.post(url, data=payload)
    return r.text


# Returns emails that can be used to add SSL
# Requires the domain of the site
def getDomainApproverEmail(domain,api_id=os.environ.get('API_ID'),api_key=os.environ.get('API_KEY')):
    url= api_endpoint+'prov/v1/domain/emails'
    payload={
        'api_id':api_id,
        'api_key':api_key,
        'domain':domain
    }
    r = requests.post(url, data=payload)
    return r.text

'''Not Completed
# Changes a basic setting for the site
# Requires Site ID, the Parameter to change, and, value to assign
# Valid values are listed at: https://docs.incapsula.com/Content/API/sites-api.htm#Modify
def modSiteConfig(site_id,param,value,api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url=api_endpoint+'prov/v1/sites/configure'
    payload={'api_id': api_id, 'api_key': api_key, 'domain': domain, 'site_id':site_id, 'param':param, 'value':value}
    r = requests.post(url, data=payload)
    return r.text
'''

def modSiteLogLevel(site_id, log_level, api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url=api_endpoint + 'prov/v1/sites/setlog'
    payload={'api_id': api_id,'api_key': api_key, 'site_id': site_id, 'log_level': log_level}
    r = requests.post(url, data=payload)
    return r.text


# Changes a basic setting for the site
# Requires Site ID, the rule to change, and, value to assign
# For Bot blocking we assume that we should challange suspected bot unless told otherwise
# Valid values are listed at: https://docs.incapsula.com/Content/API/sites-api.htm#Modify3
# This is only a partial implementation, more still needs to be added
def modSiteSecurityConfig(site_id,rule_id,value,api_id=os.environ.get('API_ID'),api_key=os.environ.get('API_KEY'),chal_sus_bot='true'):
    url=api_endpoint+'prov/v1/sites/configure/security'
    if rule_id=='api.threats.ddos':
        payload={
            'api_id':api_id,
            'api_key':api_key,
            'site_id':site_id,
            'rule_id':rule_id,
            'activation_mode':'api.threats.ddos.activiation_mode.auto', #This is required, can also be on
            'ddos_traffic_threshold':value
        }
    elif rule_id=='api.threats.bot_access_control':
        payload={
            'api_id':api_id,
            'api_key':api_key,
            'site_id':site_id,
            'rule_id':rule_id,
            'block_bad_bots':value,
            'challenge_suspected_bots':chal_sus_bot
        }
    else:
        return 1
    r=requests.post(url, data=payload)
    return r.text


def modSiteACL(site_id, rule_id, listed, api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    if rule_id == 'api.acl.blacklisted_countries':
        payload={'api_id': api_id,'api_key': api_key, 'site_id': site_id, 'rule_id': rule_id, 'countries': listed}
    if rule_id == 'api.acl.blacklisted_urls':
        payload={'api_id': api_id,'api_key': api_key, 'site_id': site_id, 'rule_id': rule_id, 'urls': listed}
    if rule_id == 'api.acl.blacklisted_ips':
        payload={'api_id': api_id,'api_key': api_key, 'site_id': site_id, 'rule_id': rule_id, 'ips': listed}
    if rule_id == 'api.acl.whitelisted_ips':
        payload={'api_id': api_id,'api_key': api_key, 'site_id': site_id, 'rule_id': rule_id, 'ips': listed}
    url=api_endpoint + 'prov/v1/sites/configure/acl'
    r = requests.post(url, data=payload)
    return r.text

'''
def modWhitelistConfig
'''

'''
def delSite
'''

def listSites(api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url=api_endpoint + 'prov/v1/sites/list'
    payload={'api_id': api_id,'api_key': api_key, 'page_size': 100}
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
