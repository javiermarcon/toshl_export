#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import json
import os
import sqlalchemy

FOLDER = os.path.dirname(__file__) + '/../json/'

to_read = ['accounts', 'categories', 'currencies', 'entries', 'tags']

file_contents = {}

for name in to_read:
    file_name = 'toshl_{}'.format(name)
    file_path = os.path.join(FOLDER, file_name)
    with open('{}{}'.format(file_path, '.json'), 'r') as f:
        content = f.read()
        jcontent = json.loads(content)
        file_contents[name] = jcontent

