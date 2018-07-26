import json
import os
from collections import namedtuple
from string import ascii_uppercase

path = os.path.dirname(os.path.abspath(__file__))
file_name = 'catalog.json'
ASCII_UPPERCASE = set(ascii_uppercase)
Airport = namedtuple('Airport', ['name', 'city', 'country', 'iata', 'icao', 'lat', 'lon', 'alt', 'tz', 'dst', 'tzdb'])
data = []

with open(path + '/airport_list.json') as f:
    airports = json.load(f)

for index, airport in enumerate(airports):
    element = {
        "code": index + 1,
        "name": airport[0],
        "iata": airport[3],
        "country": {"name": airport[2]},
        "continent": {"name": airport[10].split('/')[0]}
    }
    data.append(element)

with open(path + '/' + file_name, 'w+') as outfile:
    json.dump(data, outfile)
