import engine
import csv

PAGINATION = 50
SEARCH_SIZE = 50
CAP = 100000
TYPE = 0
TIME = 1
KEY = 2
LOC = 3
REP = 4

query = {"bool": {"must": [
            {"range": {"database_id": {"gte": 2536268}}},
            {'match': {'tracked_data.form_params.department': '7daf94ed9226aa945a58b6550d142558'}}
        ]}}
request = {'size': SEARCH_SIZE, 'from': 0, 'query': query}

w = csv.writer(open('output.csv', 'w'))


def keyboard(track):
    events = track['_source']['tracked_data']['keyboard']
    return events[0]['events'] if len(events) > 0 else []


def device(track):
    return track['_source']['tracked_data']['device']


def meli_params(track):
    return track['_source']['tracked_data']['meli_params']


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


def is_up(event):
    return event[TYPE] == 0


def is_down(event):
    return event[TYPE] == 1


def is_last(index, events_count):
    return (index + 1) == events_count


'''
Return: TupleAVG(pressure, dwell_time, flight_time)
'''


def calculate_features(events):
    sum_delta_time, sum_flight_time, sum_dwell_time, sum_flight_time, sum_pressure = 0, 0, 0, 0, 0
    alt_right_count, alt_left_count, shift_right_count, shift_left_count, tab_count = 0, 0, 0, 0, 0
    ctrl_right_count, ctrl_left_count, enter_count, backspace_count, space_count = 0, 0, 0, 0, 0

    events = summarize_events(events)
    keys_count = len(filter(lambda x: x[0] == 1, events[1]))
    start_time = events[0]
    events_count = len(events[1])

    for index, event in enumerate(events[1]):

        # Stats
        sum_pressure += event[REP]
        sum_delta_time += event[TIME]
        sum_dwell_time += event[TIME] if is_up(event) else 0
        sum_flight_time += event[TIME] if is_down(event) or (not is_last(index, events_count)) else 0

        # Keys
        alt_right_count += 1 if is_key_code(event, 18) and is_right(event) else 0
        alt_left_count += 1 if is_key_code(event, 18) and is_left(event) else 0
        shift_right_count += 1 if is_key_code(event, 16) and is_right(event) else 0
        shift_left_count += 1 if is_key_code(event, 16) and is_left(event) else 0
        ctrl_right_count += 1 if is_key_code(event, 17) and is_right(event) else 0
        ctrl_left_count += 1 if is_key_code(event, 17) and is_left(event) else 0
        tab_count += 1 if is_key_code(event, 9) else 0
        enter_count += 1 if is_key_code(event, 13) else 0
        backspace_count += 1 if is_key_code(event, 8) else 0
        space_count += 1 if is_key_code(event, 32) else 0

    avg_pressure = round(sum_pressure/float(keys_count), 5) if keys_count > 0 else 0
    avg_dwell_time = round(sum_dwell_time/float(keys_count), 5) if keys_count > 0 else 0
    avg_flight_time = round(sum_flight_time/float(keys_count), 5) if keys_count > 0 else 0
    error_rate = round(backspace_count/float(keys_count), 5) if keys_count > 0 else 0
    avg_alt_right = round(alt_right_count/float(keys_count), 5) if keys_count > 0 else 0
    avg_alt_left = round(alt_left_count/float(keys_count), 5) if keys_count > 0 else 0
    avg_shift_right = round(shift_right_count/float(keys_count), 5) if keys_count > 0 else 0
    avg_shift_left = round(shift_left_count/float(keys_count), 5) if keys_count > 0 else 0
    avg_ctrl_right = round(ctrl_right_count/float(keys_count), 5) if keys_count > 0 else 0
    avg_ctrl_left = round(ctrl_left_count/float(keys_count), 5) if keys_count > 0 else 0
    avg_enter = round(enter_count/float(keys_count), 5) if keys_count > 0 else 0
    avg_space = round(space_count/float(keys_count), 5) if keys_count > 0 else 0
    avg_tab = round(tab_count/float(keys_count), 5) if keys_count > 0 else 0
    end_time = start_time + sum_dwell_time

    return start_time, end_time, avg_pressure, avg_dwell_time, avg_flight_time,\
           avg_alt_right, avg_alt_left, avg_shift_right, avg_shift_left, \
           avg_ctrl_right, avg_ctrl_left, avg_enter, avg_space, avg_tab, error_rate


def search():
    return engine.search('biometrics', 'desktop', request)


def update_pagination():
    request['from'] += PAGINATION
    print 'From: ' + repr(request['from'])


def get_hits(tracks):
    return tracks['hits']['hits']


def get_tracks(results):
    hits = get_hits(results)
    return [{'meli_params': meli_params(track), 'device': device(track), 'keyboard': keyboard(track)} for track in hits if len(keyboard(track)) > 0]


def match_device_with(feature, value):
    return int(value in str(feature).lower())


# Processing data
results = search()
while has_hits(results) and (request['size'] + request['from'] <= CAP):

    tracks = get_tracks(results)
    for track in tracks:
        keyboard_events = track['keyboard']

        device_app_version = track['device']['appVersion']
        device_platform = track['device']['platform']

        # Calculate Features:
        pattern = ''.join([str(event[0]) for event in keyboard_events])
        is_android = match_device_with(device_app_version, 'android')
        is_iphone = match_device_with(device_platform, 'iphone')
        is_ipad = match_device_with(device_platform, 'ipad')
        is_ipod = match_device_with(device_platform, 'ipod')
        is_mac = match_device_with(device_platform, 'macintel')
        is_linux = match_device_with(device_platform, 'linux') & ~match_device_with(device_app_version, 'android')
        is_window = match_device_with(device_platform, 'win')
        is_blackberry = match_device_with(device_platform, 'blackberry')
        is_playstation = match_device_with(device_platform, 'playstation')
        is_arm = match_device_with(device_platform, 'arm')
        is_masking_agent = match_device_with(device_platform, 'masking-agent')
        is_freebsd = match_device_with(device_platform, 'freebsd')
        is_osmeta = match_device_with(device_platform, 'osmeta')
        is_anomaly_user_agent = match_device_with(device_platform, 'android') & match_device_with(device_app_version, 'macintosh')
        is_empty_platform = 1 if not device_platform else 0
        user_id = str(track['meli_params']['user_id'])
        user_id = user_id if user_id != 'unknown' else -1

        (start_time,
         end_time,
         avg_dwell_time,
         avg_pressure,
         avg_flight_time,
         avg_alt_right,
         avg_alt_left,
         avg_shift_right,
         avg_shift_left,
         avg_ctrl_right,
         avg_ctrl_left,
         avg_enter,
         avg_space,
         avg_tab,
         error_rate) = calculate_features(keyboard_events)

        # Write on file
        instance = [start_time, end_time, avg_pressure, avg_dwell_time, avg_flight_time,
                    avg_alt_right, avg_alt_left, avg_shift_right, avg_shift_left,
                    avg_ctrl_right, avg_ctrl_left, avg_enter, avg_space,
                    avg_tab, error_rate, is_android, is_iphone, is_ipad, is_ipod, is_mac,
                    is_linux, is_window, is_blackberry, is_playstation, is_arm,
                    is_masking_agent, is_freebsd, is_osmeta, is_anomaly_user_agent,
                    is_empty_platform, user_id, pattern]
        w.writerow(instance)

    update_pagination()
    results = search()

print 1
