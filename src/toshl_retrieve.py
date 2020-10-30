#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import json
import pprint
import requests
from requests.auth import HTTPBasicAuth
from config import toshl_parameters
import six

prefix = ''

def get_from_toshl(svcName='categories', params=None):
    '''Downloads the data from toshl'''
    upload_url = toshl_parameters['upload_url'] + '{}'.format(svcName)
    ret = requests.get(upload_url, params=params, auth=HTTPBasicAuth(toshl_parameters['username'], toshl_parameters['password']))
    if ret.status_code == 200:
        return json.loads(ret.text)
    else:
        pprint.pprint(ret)

def save_json(filePath, contents):
    '''saves a json file'''
    with open(filePath,'a+') as f:
        f.write(contents)

to_download = {
    'categories': None,
    'tags': None,
    'entries': {'from': '1970-01-01', 'to': '2030-12-31'},
    'accounts': None,
    'budgets': {'from': '1970-01-01', 'to': '2030-12-31'},
    'currencies': None
}

for name, params in six.iteritems(to_download):
    entriesJson = get_from_toshl(svcName=name, params=params)
    save_json('/tmp/toshl_{}.json'.format(name), json.dumps(entriesJson, sort_keys=True, indent=4, separators=(',', ': ')))

"""
categories = {}
tags = {}
for cat in catsJson:
    categories[cat['id']] = cat['name']
for ta in tagsJson:
    tags[ta['name']] = categories[ta['category']]
#pprint.pprint(catsAll)
#pprint.pprint(tags)
"""