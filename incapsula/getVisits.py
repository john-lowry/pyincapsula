#!/usr/bin/env python3
"""Gathers the JSON for visits to a site

Further documentation on granularity and time ranges, can be found here:
https://docs.incapsula.com/Content/API/traffic-api.htm#Getvisits
Granularity, Start Time, and End Time must have a value and not be None
in order to be used.

 site_id -- Numerical ID of the site to gather statistics on
 time_range -- time range to gather, use custom to specify a start and\
 end (Default: last_7_days)
 granularity -- milliseconds between intervals, ignored if None\
 (Default: None)(Must be int)
 start -- milliseconds since 1/1/1970 to start gathering at,\
 ignored if None (Default: None)(Must be int)
 end -- milliseconds since 1/1/1970 to stop gathering at,\
 ignored if None (Default: None)(Must be int)
 page -- Page to start listing sites (Default: 0)
 page_size -- Number of objects per page (Default: 100)
 recursive -- determine if the function should loop through pagination\
 (Default: True)
 security -- Security rules to filter by, comma seperated single string\
 ignored if None (Default: None)
 country -- Filter visits by origin country ignored if None\
 (Default: None)
 ip -- Filter visits by origin IP ignored if None (Default: None)
 visit_id -- single string, comma seperated list of visits to display\
 ignored if None (Default: None)
 list_live_visits -- bool to list active sessions or not\
 (Default: false)
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
"""

import json
from .com_error import errorProcess
from .sendRequest import ApiCredentials, ApiUrl, makeRequest

api_creds = ApiCredentials()
api_endpoint = ApiUrl.api_endpoint

def getVisits(
        site_id, time_range='last_7_days', granularity=None, start=None,
        end=None, page=0, page_size=100, security=None, country=None, ip=None,
        visit_id=None, recursive=True, list_live_visits='false'):
    url = api_endpoint + 'visits/v1'
    list_live_visits = str(list_live_visits).lower
    # Miss type? you didn't want it.
    if list_live_visits not in ('true', 'false'):
        list_live_visits = 'false'
    payload = {
        'api_id': api_creds.api_id,
        'api_key': api_creds.api_key,
        'site_id':site_id,
        'time_range':time_range,
        'page_num':page,
        'page_size':page_size,
        'list_live_visits':list_live_visits
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
    except ValueError as error:
        return errorProcess(error,'int')
    except Exception as error:
        return errorProcess(error)
    if security is not None:
        payload['security']=security
    if country is not None:
        payload['country']=country
    if ip is not None:
        payload['ip']=ip
    if visit_id is not None:
        payload['visit_id']=visit_id
    try:
        r = makeRequest(url, payload)
        r_json = json.loads(r.text)
        # ['visits'] will always be returned. Unless an error has
        # occured, in whcich case res will be greater then 0.
        if recursive and r_json['res'] == 0:
            max_objects=page_size
            out = r_json # Setups up initial out object
            # We can't have more then the max, and if we have less, then
            # we already have all the data and it's time to move on.
            while len(r_json['visits']) == max_objects:
                payload['page_num']=payload['page_num']+1
                r = makeRequest(url, payload)
                r_json = json.loads(r.text)
                out['visits'].extend(r_json['visits'])
        else:
            out = r_json
        return json.dumps(out)
    except Exception as error:
        return errorProcess(error)