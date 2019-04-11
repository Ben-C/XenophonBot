import tweepy, time
import markovify
from twitter_credentials import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
time.sleep(120)
while True:
    with open("corpus.txt") as corpus:
        corpus.lines = corpus.read()
        model = markovify.Text(corpus.lines)
        message = model.make_short_sentence(200)
        api.update_status(message)
    time.sleep(1800)
