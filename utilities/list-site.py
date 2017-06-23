#!/usr/bin/env python
import json
import incapsula
import argparse

parser = argparse.ArgumentParser(description="Given a site_id, list status")
parser.add_argument("-s", "--site",dest='site_id', help='The site id to retrieve information for')
args = parser.parse_args()

r = json.loads(incapsula.getSiteStatus(args.site_id))
print(json.dumps(r, indent=2, separators=(',', ': ')))
