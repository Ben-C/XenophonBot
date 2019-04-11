import tweepy
from twitter_credentials import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_SECRET, CONSUMER_KEY
import markovify
from time import sleep

class XenophonBot:
    def __init__(self, corpus):
        self.load_corpus(corpus)

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

    def load_corpus(self, corpus):
        with open('corpus.txt') as corpus_file:
            corpus = corpus_file.read()
        self.model = markovify.Text(corpus)

    def tweet(self):
        message = self.model.make_short_sentence(140)
        try:
            self.api.update_status(message)
        except tweepy.TweepError as error:
            print(error.reason)

    def automate(self, delay):
        while True:
            self.tweet()
            sleep(delay)

def main():
	bot = XenophonBot("corpus.txt")
	bot.automate(3600)

if __name__ == "__main__":
    main()
