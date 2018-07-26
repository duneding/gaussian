import json
import os
import random
from datetime import datetime

from config import config

path = os.path.dirname(os.path.abspath(__file__))
file_name = 'travels.json'
configuration = config.Config(path)
size = 100
data = []
countries = configuration.value(['country_codes'])
element = None

with open(path + '/catalog.json') as f:
    catalog = json.load(f)


def random_country():
    index = random.randint(0, len(countries) - 1)
    return countries[index]


def random_birthday():
    # ej. "1985-08-22 00:00:00"
    if (random.uniform(0, 1) > 0.90):
        return None
    else:
        year = random.randint(1930, 2017)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return str(datetime(year, month, day))


def random_gender():
    if (random.uniform(0, 1) > 0.90):
        return None
    else:
        return "FEMALE" if random.randint(0, 1) == 0 else "MALE"


def random_id():
    return random.randint(1, 10000) * random.randint(1, 5)


def lookup_in_catalog(code):
    for element in catalog:
        if (element['code'] == code):
            return element


def random_codes():
    codes = []
    if (random.uniform(0, 1) < 0.90):
        total_codes = random.randint(1, 10)
        for i in range(0, total_codes):
            #code = random.randint(1, 600)
            #airport = lookup_in_catalog(code)
            codes.append(random.randint(1, 600))
    return codes


def random_element():
    return {
        "id": random_id(),
        "country": random_country(),
        "gender": random_gender(),
        "birthday": random_birthday(),
        "codes": random_codes()
    }


for x in range(0, size):
    data.append(random_element())

with open(path + '/' + file_name, 'w+') as outfile:
    json.dump(data, outfile)
