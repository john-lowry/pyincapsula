#!/usr/bin/env python3
"""Gathers the JSON results for statistics

Further documentation on granularity, time ranges, and statistics that
can be gathered can be found here:
https://docs.incapsula.com/Content/API/traffic-api.htm#Getstatistics
Granularity, Start Time, and End Time must have a value and not be None
in order to be used.

 site_id -- Numerical ID of the site to gather statistics on
 time_range -- time range to gather, use custom to specify a start and end
 stats -- Statistics to gather, Comma seperated list
 granularity -- milliseconds between intervals, ignored if None\
 (Default: None)(Must be int)
 start -- milliseconds since 1/1/1970 to start gathering at,\
 ignored if None (Default: None)(Must be int)
 end -- milliseconds since 1/1/1970 to stop gathering at,\
 ignored if None (Default: None)(Must be int)
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
"""

from .com_error import errorProcess
from .sendRequest import ApiCredentials, ApiUrl, makeRequest

api_creds = ApiCredentials()
api_endpoint = ApiUrl.api_endpoint

def getReport(site_id, time_range, stats, granularity=None, start=None, end=None):
    url = api_endpoint + 'stats/v1'
    payload = {
        'api_id': api_creds.api_id,
        'api_key': api_creds.api_key,
        'site_id': site_id,
        'time_range': time_range,
        'stats': stats
    }
    try:
        if granularity is not None:
            if not isinstance(granularity, int):
                granularity = int(granularity)
            payload['granularity']=granularity
        if start is not None:
            if not isinstance(start, int):
                start = int(start)
            payload['start']=start
        if end is not None:
            if not isinstance(end, int):
                end = int(end)
            payload['end']=end
        r = makeRequest(url, payload)
        return r.text
    except ValueError as error:
        return errorProcess(error,'int')
    except Exception as error:
        return errorProcess(error)