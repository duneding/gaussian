from elasticsearch import Elasticsearch
import configuration.config as config

config = config.Config()

host = config.value(['elasticsearch', 'host'])
port = config.value(['elasticsearch', 'port'])
es = Elasticsearch([{'host': host, 'port': port}])

def index(index, type, id, object):
    return es.index(index=index, doc_type=type, id=id, body=object)
    #log = 'Indexing Gensory - Type: ' + type + ' ID: ' + str(id)
    #print log

def search(index, type, request):
    return es.search(index=index, doc_type=type,body=request)