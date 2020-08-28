#!/usr/bin/env python3

"""Use this operation to set-up advanced caching rules.

Valid options are listed at:
https://docs.incapsula.com/Content/API/sites-api.htm#Modify7

Only partial functionality - more needs to be added. Comma seperated lists need to be strings, not pythonic lists.

 site_id -- numerical site id to retrive (Default: None)
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)

All options below are optional:

 always_cache_resource_url -- Comma separated list of always cache resources url
 always_cache_resource_pattern -- Comma separated list of always cache resources pattern. One of: contains | equals | prefix | suffix | not_equals | not_contains | not_prefix | not_suffix
 always_cache_resource_duration -- Duration that resources will be in cache, pass number followed by '_' and one of: hr | min | sec | days | weeks.  Either provide a comma separated list of duration expressions, matching the number of always cache rules, or a single duration expression to be used for all always cache rules.
 never_cache_resource_url -- Comma separated list of never cache resources url.
 never_cache_resource_pattern -- Comma separated list of never cache resources pattern. One of: contains | equals | prefix | suffix | not_equals | not_contains | not_prefix | not_suffix
 cache_headers -- Comma separated list of cached headers.
 clear_always_cache_rules -- An optional boolean parameter. If set to "true", the site's always cache rules will be cleared.
 clear_never_cache_rules -- An optional boolean parameter. If set to "true", the site's never cache rules will be cleared.
 clear_cache_headers_rules -- An optional boolean parameter. If set to "true", the site's cache header rules will be cleared.
"""

from .com_error import errorProcess
from .sendRequest import ApiCredentials, ApiUrl, makeRequest

api_creds = ApiCredentials()
api_endpoint = ApiUrl.api_endpoint

def modCachingRule(
        site_id=None, never_cache_resource_pattern=None, never_cache_resource_url=None, always_cache_resource_url=None,
        always_cache_resource_pattern=None, always_cache_resource_duration=None, cache_headers=None,
        clear_always_cache_rules=None, clear_never_cache_rules=None, clear_cache_headers_rules=None):

    url = api_endpoint+'prov/v1/sites/performance/caching-rules'
    try:  # Setup the payload
        assert site_id is not None
        payload = {
            'api_id': api_creds.api_id,
            'api_key': api_creds.api_key,
            'site_id': site_id
        }

        if never_cache_resource_pattern is not None:
            payload['never_cache_resource_pattern'] = never_cache_resource_pattern
        if never_cache_resource_url is not None:
            payload['never_cache_resource_url'] = never_cache_resource_url
        if always_cache_resource_url is not None:
            payload['always_cache_resource_url'] = always_cache_resource_url
        if always_cache_resource_pattern is not None:
            payload['always_cache_resource_pattern'] = always_cache_resource_pattern
        if always_cache_resource_duration is not None:
            payload['always_cache_resource_duration'] = always_cache_resource_duration
        if cache_headers is not None:
            payload['cache_headers'] = cache_headers
        if clear_always_cache_rules is not None:
            payload['clear_always_cache_rules'] = clear_always_cache_rules
        if clear_never_cache_rules is not None:
            payload['clear_never_cache_rules'] = clear_never_cache_rules
        if clear_cache_headers_rules is not None:
            payload['clear_cache_headers_rules'] = clear_cache_headers_rules

    except AssertionError as error:
        return errorProcess(error, site_id)
    except Exception as error:
        return errorProcess(error)
    try:  # Deliver the payload
        r = makeRequest(url, payload)
        r.raise_for_status()
        return r.text
    except NameError as error:
        return errorProcess(error, 'Rule ID')
    except Exception as error:
        return errorProcess(error)
