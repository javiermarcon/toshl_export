#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import json
import pprint
import requests
from requests.auth import HTTPBasicAuth
from config import toshl_parameters

def get_from_toshl(svcName='categories', params=None):

    upload_url = toshl_parameters['upload_url'] + '{}'.format(svcName)
    ret = requests.get(upload_url, params=params, auth=HTTPBasicAuth(toshl_parameters['username'], toshl_parameters['password']))
    if ret.status_code == 200:
        return json.loads(ret.text)
    else:
        pprint.pprint(ret)

catsJson = get_from_toshl(svcName='categories')
tagsJson = get_from_toshl(svcName='tags')
entriesJson = get_from_toshl(svcName='entries', params={'from': '1970-01-01', 'to': '2030-12-31'})
pprint.pprint(entriesJson)
accoutsJson = get_from_toshl(svcName='accounts')
pprint.pprint(accoutsJson)
categories = {}
tags = {}
for cat in catsJson:
    categories[cat['id']] = cat['name']
for ta in tagsJson:
    tags[ta['name']] = categories[ta['category']]
#pprint.pprint(catsAll)
pprint.pprint(tags)
