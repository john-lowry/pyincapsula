#!/usr/bin/env python3

import json
import requests

def errorProcess(error, data=None):
    if type(error) is NameError:
        outError = {
            'error':0,
            'description':'Required argument not provided',
            'details':str(data)+' was not provided'
        }
    elif type(error) is AssertionError:
        outError = {
            'error':0,
            'description':'Required argument not provided',
            'details':str(data)+' was not provided or is incorrect'
        }
    elif type(error) is ConnectionError:
        outError = {
            'error':1,
            'description':'Connection error.',
            'details':error
        }
    elif type(error) is TimeoutError:
        outError = {
            'error':2,
            'description':'Connection timed-out.',
            'details':error
        }
    elif type(error) is requests.exceptions.HTTPError:
        outError = {
            'error':3,
            'description':'HTTP Exception',
            'details':error
        }
    elif type(error) is EnvironmentError:
        outError = {
            'error':4,
            'description':data,
            'details':error
        }
    else:
        outError = {
            'error':99,
            'description':'Unknown Error',
            'details':error
        }
    return json.dumps(outError)