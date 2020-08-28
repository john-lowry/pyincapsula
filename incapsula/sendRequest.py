#!/usr/bin/env python3

import os
import requests


class ApiCredentials:
    api_id = os.environ.get('API_ID')
    api_key = os.environ.get('API_KEY')


class ApiUrl:
    api_endpoint = 'https://my.incapsula.com/api/'


def makeRequest(url, payload):
    return requests.post(url, data=payload)
