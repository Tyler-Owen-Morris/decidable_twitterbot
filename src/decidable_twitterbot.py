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
url = 'http://127.0.0.1:8000/api/v1/save-question'


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
        # post to deciable
        myData = {'user_id': 666, 'question': question}
        x = requests.post(url, data=myData)
        print(x.text)
        resp = json.loads(x.text)
        qid = resp['questionId']
        print(qid)
        # retrieve question # from response

        # formulate tweet with dynamic link
        tweet = question + \
            f" || submit your answer now at https://6f31a8f9be9a.ngrok.io/api/v1/get-bot-question/{qid} "
        print(tweet)
        if len(tweet) > 260:
            print("this is too long to tweet")
        else:
            print("I can tweet this!")
            # api.update_status(tweet)
        print("sleeping")
        time.sleep(60)
        print("awake!")


if __name__ == "__main__":
    run_bot()
