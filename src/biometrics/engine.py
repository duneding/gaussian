__author__ = 'root'
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from src import config

def host():
    return config.value(['elasticsearch', 'host'])

def port():
    return config.value(['elasticsearch', 'port'])

es = Elasticsearch([{'host': host(), 'port': port()}])

def search(index, type, request):
    return es.search(index=index, doc_type=type, body=request)