import pandas as pandas
import re
import requests
from bs4 import BeautifulSoup
from datetime import date

import tweepy

# get keys and tokens for twitter app from a file
all_keys = open('twitterkeys.txt', 'r').read().splitlines()
api_key = all_keys[0]
api_key_secret = all_keys[1]
bearer_token = all_keys[2]
access_token = all_keys[3]
access_token_secret = all_keys[4]

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

# api = tweepy.API(authenticator, wait_on_rate_limit=True)
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during")
client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)
# client = tweepy.Client(bearer_token)

#Pull in Aaron Judge's stats source code
url = 'https://www.espn.com/mlb/player/stats/_/id/33192/aaron-judge'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

stats = soup.find('ul', attrs = {'class': 'StatBlock__Content flex list ph4 pv3 justify-between'})

homerun_li_element = stats.find_all('li')[1]

#Today's date
today = date.today()

judge_stats = "Aaron Judge has " + homerun_li_element.find('div', attrs = {'class': 'StatBlockInner__Value'}).get_text() + f" homeruns in his magical 2022 season as of {today}."
print(judge_stats)

# api.update_status(judge_stats)
client.create_tweet(text=judge_stats)
# query = 'Aaron Judge'
# tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

# for tweet in tweets.data:
#     print(tweet.text)
#     if len(tweet.context_annotations) > 0:
#         print(tweet.context_annotations)