#!/usr/bin/env python
import tweepy
import time
import markovify
from twitter_credentials import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_SECRET, CONSUMER_KEY

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

print("Hit 'Ctrl+C' to stop.")

while True:
    with open("corpus.txt") as corpus:
        corpus_lines = corpus.read()
    text_model = markovify.Text(corpus_lines)
    message = text_model.make_short_sentence(140)
    twt = api.search(q="#Ancient", max_tweets=100)
    for s in twt:
        m = "@{} {}".format(s.user.screen_name, message)
        s = api.update_status(m, s.id)
    time.sleep(3600)
