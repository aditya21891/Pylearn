# this is a program to learn sentiment analysis of machine learning 

#! /usr/bin/env python 

import tweepy 
from textblob import TextBlob 

consumer_key="WJrH0h02HptNuIQiDEt9ttbCC"
consumer_secret="VYeve6Vv9BGUa6Ujdo2vXbx1MFxtkI3s8P4s7lMTTpkFLBb3zO"

access_token = "294669373-lSOQcSVqIhQNZJdVG5sqQcGwxYLzEVtS3475pPSK"
access_token_secret = "uSvQN9rSHz0UaTXo0mwqjx9E9ZDcbvKRZ2Y9UTlux1Y7Y"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
public_tweets=api.search('Obama')

for tweet in public_tweets:
	print(tweet.text)
	analysis=TextBlob(tweet.text) 
 	print(analysis.sentiment)


