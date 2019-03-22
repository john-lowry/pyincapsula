#!/usr/bin/env python3
"""Gathers the JSON results for statistics

Further documentation on granularity, time ranges, and statistics that
can be gathers can be found here:
https://docs.incapsula.com/Content/API/traffic-api.htm#Getstatistics
Granularity, Start Time, and End Time must have a value and not be None
in order to be used.

 site_id -- Numerical ID of the site to gather statistics on
 time_range -- time range to gather, use custom to specify a start and end
 stats -- Statistics to gather, Comma seperated list
 granularity -- milliseconds between intervals, ignored if None (Default: None)
 start -- milliseconds since 1/1/1970 to start gathering at,\
 ignored if None (Default: None)
 end -- milliseconds since 1/1/1970 to stop gathering at,\
 ignored if None (Default: None)
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
"""

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