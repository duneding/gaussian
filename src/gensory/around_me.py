import math
from datetime import datetime

from social import api
from social import get_followers

api = api('aroundme')

# tweets = api.GetUserTimeline(screen_name=str("margostino"), count=20000)
followers = get_followers(api)

for follower in followers:
    age_delta = datetime.now() - datetime.strptime(follower.created_at, '%a %b %d %H:%M:%S +0000 %Y')
    age_in_years = math.floor(age_delta / 365)


