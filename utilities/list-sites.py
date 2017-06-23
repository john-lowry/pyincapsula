#!/usr/bin/python

import json
import incapsula

r = json.loads(incapsula.listSites())

#print(json.dumps(r, indent=2, separators=(',', ': ')))

for site, siteId, status in zip(r['sites'], r['sites'], r['sites']):
  print site['domain'] + ", " + str(site['site_id']) + ", " + site['active']


