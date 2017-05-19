import engine

request={"size":1, "query": {"match": {
    "online_data.form_params.department": "auth"}}}

#docs["hits"]["hits"][0][u'_source'][u'online_data'][u'keyboard'][0][u'events']
docs = engine.search("biometrics_data", "desktop_data", request)
if (len(docs["hits"]["hits"]) > 0):
    since_id = str(docs["hits"]["hits"][0][u'_id'])
else:
    since_id = None
