import engine
import csv
import os

PAGINATION = 10
SEARCH_SIZE = 10
CAP = 1000

request={'size': SEARCH_SIZE, 'from': 0, 'query': {'match': {
    'online_data.form_params.department': 'auth'}}}

w = csv.writer(open('output.csv', 'w'))

def encode_type(type):
    if type == 'keydown':
        return '1'

    return '0'

def to_pattern(types):
    return ''.join(map(encode_type, types))

def calculate_avg_flying_time(times):
    sum = 0
    cap = len(times)
    for index, time in enumerate(times):
        if (index+1 < cap):
            sum = times[index+1] - time

    return sum/(index+1)

def keyboard(track):
    return track['_source']['online_data']['keyboard']

def events(key_track):
    return key_track[0]['events']

def has_hits(tracks):
    return len(tracks['hits']['hits']) > 0

patterns = []
tracks = engine.search('biometrics_data', 'desktop_data', request)
while (has_hits(tracks) and request['from'] < CAP):

    tracks = tracks['hits']['hits']
    for key_track in [keyboard(track) for track in tracks if len(keyboard(track))>0]:
        key_events = key_track[0]['events']#events(key_track)
        pattern = to_pattern([events['type'] for events in key_events])
        patterns.append(pattern)
        time_end = key_track[0]['events'][len(key_events)-1]['time']
        flying_avg_time = calculate_avg_flying_time([events['time'] for events in key_events])
        w.writerow([time_end, flying_avg_time, pattern])

    request['from'] = request['from'] + PAGINATION
    print 'From: ' + `request['from']`
    tracks = engine.search('biometrics_data', 'desktop_data', request)

print 1
