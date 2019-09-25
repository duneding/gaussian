import math
from datetime import datetime

import twitter

import src.configuration.config as config
from .engine import index as

config = config.Config()
index
index("")
consumer_key = config.value(['twitter', 'aroundme', 'consumer_key'])
consumer_secret = config.value(['twitter', 'aroundme', 'consumer_secret'])
access_token = config.value(['twitter', 'aroundme', 'access_token'])
access_token_secret = config.value(['twitter', 'aroundme', 'access_token_secret'])
api = twitter.Api(consumer_key, consumer_secret, access_token, access_token_secret)

# tweets = api.GetUserTimeline(screen_name=str("margostino"), count=20000)
followers = api.GetFollowers(include_user_entities=True)

for follower in followers:
    age_delta = datetime.now() - datetime.strptime(follower.created_at, '%a %b %d %H:%M:%S +0000 %Y')
    age_in_years = math.floor(age_delta / 365)
