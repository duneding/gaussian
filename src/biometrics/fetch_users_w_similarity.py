import csv
import json

import requests

from src.configuration import config

API_FEATURES = config.value(['biometrics', 'api_features'])
API_SCORING = config.value(['biometrics', 'api_scoring'])
INPUT_FILE = 'user_with_similarity.csv'
OUTPUT_FILE = 'users_w_similarity_w_biometric.csv'
w = csv.writer(open(OUTPUT_FILE, 'w'))


def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))


with open(INPUT_FILE, "rb") as file:
    ff = csv.reader(file)

    for col_user in ff:
        user = col_user[0]
        features = json.loads(str(requests.get(API_FEATURES + user).content))
        scorings = json.loads(str(requests.get(API_SCORING + user).content))

        for features_event in features:
            features = features_event['features'] if isinstance(features_event, dict) else None

            if features != None:
                date = features_event['date']
                bot_score = [score['bot_score'] for score in scorings if score['date'] == date]
                bot_score = bot_score[0] if len(bot_score) > 0 else -1

                # Write on file
                instance = [user,
                            features['dwell_disp'], features['dwell_time'],
                            features['flight_disp'], features['flight_time'],
                            features['mouse_distance'], features['mouse_points'],
                            bot_score]
                print instance
                w.writerow(instance)

print 1
