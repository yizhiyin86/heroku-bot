# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "6dj1rPeIXm9lGHAJ0XDOlBCKT"
consumer_secret = "Czsnhwgan8wDkShkWclER9XNcpurhJFWmCBaC5EvVv5BcKPhHV"
access_token = "968998318780174336-zgI9bmi7Oaf3FbpeaIP6SxpFN85LewW"
access_token_secret ="kttUSYIn0NmynHBswVRehSC0BBV2akgqk4hfQ6i5VlFK7"
# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE
while True:
    api.update_status('hello')
    time.sleep(30)