#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import json
import os
import csv

FOLDER = '../json/' # os.path.dirname(__file__) +

to_read = ['accounts', 'categories', 'entries', 'tags']

file_contents = {}

# dictionary of file contents
for name in to_read:
    file_name = 'toshl_{}.json'.format(name)
    file_path = os.path.join(FOLDER, file_name)
    with open(file_path, 'r') as f:
        content = f.read()
        jcontent = json.loads(content)
        file_contents[name] = {}
        for entry in jcontent:
            file_contents[name][entry['id']] = entry

entries = {}

# entries separated by account
for entry_id in file_contents['entries']:
    data = file_contents['entries'][entry_id]
    account = file_contents['accounts'][data['account']]['name']
    data['currency']  = file_contents['accounts'][data['account']]['currency']['code']
    if 'tags' in data:
        data['tags'] = '|'.join([file_contents['tags'][x]['name'] for x in data['tags']])
    if 'transaction' in data:
        data['transfer_to'] = file_contents['accounts'][data['transaction']['account']]['name']
        data['other_amount'] = data['transaction']['amount']
        data['other_currency'] = data['transaction']['currency']['code']
    if not account in entries:
        entries[account] = []
    entries[account].append(data)

# make csv
headers = ['id', 'account', 'amount', 'date', 'desc', 'currency', 'tags', 'transfer_to', 'other_amount', 'other_currency']

for account in entries:
    file_name = 'toshl_{}.csv'.format(account)
    file_path = os.path.join(FOLDER, file_name)
    with open(file_path, 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, headers, quoting=csv.QUOTE_NONNUMERIC, extrasaction='ignore')
        dict_writer.writeheader()
        dict_writer.writerows(entries[account])