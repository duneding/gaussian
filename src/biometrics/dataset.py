import engine
import csv

PAGINATION = 50
SEARCH_SIZE = 50
CAP = 20000
TYPE = 0
TIME = 1
KEY = 2
LOC = 3
REP = 4

request={'size': SEARCH_SIZE, 'from': 0, 'query': {'match': {
    'tracked_data.form_params.department': '7daf94ed9226aa945a58b6550d142558'}}}

w = csv.writer(open('output.csv', 'w'))


def keyboard(track):
    return track['_source']['tracked_data']['keyboard']


def has_hits(tracks):
    return len(tracks['hits']['hits']) > 0


def is_same_event(previous, current):
    return  (previous is None) or \
            ((previous[TYPE] == current[TYPE]) and (previous[KEY] == current[KEY]))

def summarize_events(events):
    prev_event = None
    sum_time, key_count = 0, 0

    start_time = events[0][TIME] if len(events) > 0 else 0
    stack_event = [start_time, []]

    for index, event in enumerate(events):

        if not is_same_event(prev_event, event):
            # Change Key Type. Add delta
            stack_event[1].append([
                                    prev_event[TYPE],
                                    sum_time,
                                    prev_event[KEY],
                                    prev_event[LOC],
                                    key_count
                                ])
            sum_time = 0
            key_count = 0

        sum_time += event[TIME] if(index > 0) else 0
        key_count += 1
        prev_event = event

    return stack_event


def is_key_code(event, code):
    return event[KEY] == code

def is_right(event):
    return event[LOC] == 2

def is_left(event):
    return event[LOC] == 1


'''
Return: TupleAVG(pressure, dwell_time, flight_time)
'''


def calculate_features(events):
    sum_flight_time, sum_delta_time, sum_flight_time, sum_pressure = 0, 0, 0, 0
    alt_right_count, alt_left_count, shift_right_count, shift_left_count = 0, 0, 0, 0
    enter_count, backspace_count, space_count = 0, 0, 0

    events = summarize_events(events)
    keys_count = len(filter(lambda x: x[0] == 1, events[1]))
    start_time = events[0]

    for event in events[1]:

        # Stats
        sum_delta_time += event[TIME]
        sum_pressure += event[REP]
        sum_flight_time += event[TIME] if event[TYPE] else 0

        # Keys
        alt_right_count += 1 if is_key_code(event, 18) and is_right(event) else 0
        alt_left_count += 1 if is_key_code(event, 18) and is_left(event) else 0
        shift_right_count += 1 if is_key_code(event, 16) and is_right(event) else 0
        shift_left_count += 1 if is_key_code(event, 16) and is_left(event) else 0
        enter_count += 1 if is_key_code(event, 13) else 0
        backspace_count += 1 if is_key_code(event, 8) else 0
        space_count += 1 if is_key_code(event, 32) else 0

    avg_pressure = round(sum_pressure/float(keys_count), 5) if keys_count > 0 else 0
    avg_dwell_time = round(sum_delta_time/float(keys_count), 5) if keys_count > 0 else 0
    avg_flight_time = round(sum_flight_time/float(keys_count), 5) if keys_count > 0 else 0
    error_rate = round(backspace_count/float(keys_count), 5) if keys_count > 0 else 0
    end_time = start_time + sum_delta_time

    return start_time, end_time, avg_pressure, avg_dwell_time, avg_flight_time,\
           alt_right_count, alt_left_count, shift_right_count, shift_left_count,\
           enter_count, backspace_count, space_count, error_rate


def search():
    return engine.search('biometrics', 'desktop', request)


def update_pagination():
    request['from'] += PAGINATION
    print 'From: ' + repr(request['from'])


def get_hits(tracks):
    return tracks['hits']['hits']


def get_tracks(results):
    hits = get_hits(results)
    return [keyboard(track) for track in hits if len(keyboard(track)) > 0]


# Processing data
results = search()
while has_hits(results) and request['from'] < CAP:

    tracks = get_tracks(results)
    for track in tracks:
        key_events = track[0]['events']

        # Calculate Features:
        pattern = ''.join([str(event[0]) for event in key_events])
        (start_time,
         end_time,
         avg_dwell_time,
         avg_pressure,
         avg_flight_time,
         alt_right_count,
         alt_left_count,
         shift_right_count,
         shift_left_count,
         enter_count,
         backspace_count,
         space_count,
         error_rate) = calculate_features(key_events)

        # Write on file
        w.writerow([start_time, end_time, avg_pressure, avg_dwell_time, avg_flight_time,
                    alt_right_count, alt_left_count, shift_right_count, shift_left_count,
                    enter_count, backspace_count, space_count, error_rate, pattern])

    update_pagination()
    tracks = search()

print 1
