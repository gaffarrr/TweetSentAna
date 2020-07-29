__author__ = 'Gaffar Gusti Pratama'
from secrets import Oauth_Secrets
import tweepy
from textblob import TextBlob


def primary(input_hashtag):
    secrets = Oauth_Secrets()
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)
    
    api = tweepy.API(auth)

    T = 1000
    Tweets = tweepy.Cursor(api.search, q=input_hashtag).items(T)
    neg = 0.0
    pos = 0.0
    neg_count = 0
    neutral_count = 0
    pos_count = 0
    for tweet in Tweets :
        # print tweet.text
        blob = TextBlob(tweet.text)
        if blob.sentiment.polarity < 0 :        #Negative
            neg += blob.sentiment.polarity
            neg_count += 1
        elif blob.sentiment.polarity == 0:      #Neutral
            neutral_count += 1
        else :
            pos += blob.sentiment.polarity
            pos_count += 1
    return [['Sentiment', 'no. of tweets'],['Positive',pos_count],
            ['Neutral',neutral_count],['Negative',neg_count]]
