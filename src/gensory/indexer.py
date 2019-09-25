#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import threading
# import logging
import time
from datetime import datetime

from engine import index
from engine import search
from social import api
from social import get_friends
from social import get_followers
from social import get_tweets
from social import tweet_to_json
from social import user_to_json

#logging.basicConfig(filename='indexer.log',level=logging.INFO)

INDEX = 'twitter'
TYPE = 'record'
twitter_error = True

alpha = api('alpha')
beta = api('beta')
gamma = api('gamma')
around_me = api('aroundme')
strimy = api('strimy')
pybig = api('pybig')
api = pybig

#thread = list()

def stats(checkpoint):
    timestamp = str(datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    log = str((threading.currentThread().getName(), checkpoint))
    print(log + ':' + timestamp)

def save(type, records):
    for record in records:
        record._json['track_type'] = type
        index(INDEX, TYPE, record.id, record._json)

def worker(api):

    stats('Launched')

    friends = get_friends(api)
    followers = get_followers(api)

    save('friends', friends)
    save('followers', followers)

    # for record in friends:
    #     save('friends', friends)
    #
    #     request={"size":1,"sort":[{"id":{"order":"desc"}}], "query": {"match": {
    #              "user.screen_name":record.screen_name}}}
    #
    #     docs = search(INDEX, 'tweet', request)
    #     if (len(docs["hits"]["hits"]) > 0):
    #         since_id = str(docs["hits"]["hits"][0][u'_id'])
    #     else:
    #         since_id = None
    #
    #     tweets = get_tweets(api, record.screen_name, since_id)
    #
    #     for tweet in tweets:
    #         index(INDEX, 'tweet', tweet.id, tweet_to_json(tweet))

    stats('Finishing')
    return

# INDEXER

# while twitter_error:
#     try:
#         friends = get_friends(api)
#         twitter_error = False
#     except twitter_error:
#         twitter_error = True
#         if api == alpha:
#             api = beta
#         elif api == beta:
#             api = gamma
#         else:
#             api = alpha
#         print("Twitter Error:", sys.exc_info()[1])

# half = len(friends)/2
# alpha_thread = threading.Thread(target=worker, name='Alpha', args=(alpha, friends[:half],))
# beta_thread = threading.Thread(target=worker, name='Beta', args=(beta, friends[half:],))
# alpha_thread.start()
# beta_thread.start()

worker(api)
