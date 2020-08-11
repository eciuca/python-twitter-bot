import tweepy

auth = tweepy.OAuthHandler('api key', 'consumer secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
