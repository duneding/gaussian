import twitter

import configuration.config as config

# from textblob import TextBlob

twitter_error = twitter.TwitterError
config = config.Config()

def consumer_key(app):
    return config.value(['twitter', app, 'consumer_key'])

def consumer_secret(app):
    return config.value(['twitter', app, 'consumer_secret'])

def access_token(app):
    return config.value(['twitter', app, 'access_token'])

def access_token_secret(app):
    return config.value(['twitter', app, 'access_token_secret'])

def username():
    return config.value('twitter', 'username')

def api(app):
    return twitter.Api(consumer_key(app), consumer_secret(app), access_token(app), access_token_secret(app))

def tweet_to_json(tweet):
    if (tweet.retweeted_status!=None):        
        retweeted_status = {
                "created_at": tweet.retweeted_status.created_at,
                "favorite_count": tweet.retweeted_status.favorite_count,
                "id": tweet.retweeted_status.id,
                "lang": str(tweet.retweeted_status.lang),
                "retweet_count": tweet.retweeted_status.retweet_count,
                "text": tweet.retweeted_status.text#(tweet.retweeted_status.text).encode("utf8")
              }
    else:
        retweeted_status = {}

    user = {"id": tweet.user.id, "screen_name": str(tweet.user.screen_name)}
    
    '''
    tb_es = TextBlob(tweet.text.encode("utf-8"))
    if tb_es.detect_language() == u'es':
        text_en = tb_es.translate(to="en")
        sentiment = text_en.sentiment
    else:
        sentiment = None
    '''
    return {
              "created_at": tweet.created_at,
              "id": str(tweet.id),
              "lang": str(tweet.lang),
              "retweet_count": tweet.retweet_count,
              "retweeted_status": retweeted_status,
              "text": tweet.text,#(tweet.text).encode("utf8"),
              "text_analyzed": tweet.text,
              "user": user#,
              #"sentiment": sentiment
            }

def user_to_json(user):

    return {
                'created_at': user.created_at,
                'description': user.description,
                'favourites_count': user.favourites_count,
                'followers_count': user.followers_count,
                'friends_count': user.friends_count,
                'id': user.id,
                'lang': user.lang,
                'listed_count': user.listed_count,
                'location': user.location,
                'name': user.name,
                #'profile_banner_url': str(user.profile_banner_url),
                'profile_image_url': user.profile_image_url,
                'screen_name': user.screen_name,
                'statuses_count': user.statuses_count,
                'url': user.url
            }

def get_tweets(api, screen_name, since_id):
    return api.GetUserTimeline(screen_name=str(screen_name), since_id=since_id, count=20000)

def get_friends(api):
    return api.GetFriends(skip_status=True)

def get_user(api,account):
    return api.GetUser(screen_name=account)

def get_followers(api):
    return api.GetFollowers(include_user_entities=True)
