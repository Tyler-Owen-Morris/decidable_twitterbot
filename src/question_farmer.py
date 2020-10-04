from tweepy import OAuthHandler, Cursor, API
import json
import pandas as pd
import time
import os
from random import randint, randrange, choice
import requests

import twitter_credentials as tc

# auth to twitter
auth = OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
print("connected to twitter...")


def get_topic_question_tweets(topic, max_tweets=100):
    searched_tweets = [
        status
        for status in Cursor(
            api.search, q=topic + " -filter:retweets ?", lang="en", tweet_mode="extended"
        ).items(max_tweets)
    ]
    found_tweets = []
    for tweet in searched_tweets:
        try:
            found_tweets.append(tweet.full_text)
        except:
            pass
    return found_tweets


topics = ["Trump", "Biden", "NFL", 'NBA']


def store_twitter_questions():
    # pick a topic
    topic = choice(topics)
    print("Farming for questions on topic: "+topic)
    # fetch tweets on topic
    file_name = "../data/"+topic+".txt"
    questions = get_topic_question_tweets(topic, 100)
    q_string = " \n\n ".join(questions)
    with open(file_name, 'a+') as f:
        f.writelines(" \n\n " + q_string)


def run_bot():
    while True:
        store_twitter_questions()
        print("waiting")
        time.sleep(60*15)
        print("searching again!")


if __name__ == "__main__":
    run_bot()
