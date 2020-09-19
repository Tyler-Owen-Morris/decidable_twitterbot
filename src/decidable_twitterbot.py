from tweepy import OAuthHandler, Cursor, API
import json
import pandas as pd
import time
import os
from random import randint, randrange, choice

import twitter_credentials as tc

# auth to twitter
auth = OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
print("connected to twitter...")


def select_question():
    # select new question to post
    questions = pd.read_csv("../data/questions.csv")
    questionrow = questions['question']
    ind = randint(0, questionrow.shape[0])
    question = questionrow[ind]
    return question


# post question to decidable

def run_bot():
    while True:
        question = select_question()
        tweet = question + " || What do you think? Answer now at decidable.ai!"
        print(tweet)
        api.update_status(tweet)
        print("sleeping")
        time.sleep(60)
        print("awake!")


if __name__ == "__main__":
    run_bot()
