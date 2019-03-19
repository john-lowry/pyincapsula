#!/usr/bin/env python3
import os
import requests
from .com_error import errorProcess

api_endpoint = 'https://my.incapsula.com/api/'

def getReport(site_id,time_range,stats,granularity=None,start=None,end=None,
        api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url = api_endpoint + 'stats/v1'
    payload = {
        'api_id':api_id,
        'api_key':api_key,
        'site_id':site_id,
        'time_range':time_range,
        'stats':stats
    }
    if granularity is not None and isinstance(granularity, int):
        payload['granularity']=granularity
    if start is not None and isinstance(start, int):
        payload['start']=start
    if end is not None and isinstance(end, int):
        payload['end']=end
    try:
        r = requests.post(url, data=payload)
        return r.text
    except Exception as error:
        return errorProcess(error)