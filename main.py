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


searchString = 'Emanuel Ciuca'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, searchString).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
