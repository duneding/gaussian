import engine

PAGINATION = 10
SIZE = 10
request={"size": SIZE, "from": 0, "query": {"match": {
    "online_data.form_params.department": "auth"}}}

#tracks["hits"]["hits"][0][u'_source'][u'online_data'][u'keyboard'][0][u'events']
tracks = engine.search("biometrics_data", "desktop_data", request)

if (len(tracks["hits"]["hits"]) > 0):
    for track in tracks["hits"]["hits"]:
        keyboard_events = track[u'_source'][u'online_data'][u'keyboard']
        for keyboard_event in keyboard_events:
            events = keyboard_events[u'events']
            for event in events:
                time = event[u'time']
                type = event[u'type']




else:
    since_id = None
