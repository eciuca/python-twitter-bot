import tweepy
import time

auth = tweepy.OAuthHandler('api key', 'consumer secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# Generous bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Some name':
        print(follower.name)
        follower.follow()
        break
