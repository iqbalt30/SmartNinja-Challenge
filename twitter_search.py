import tweepy as tw
import sys
from datetime import datetime


def display_tweets(search_words):
    consumer_key = input('Enter Consumer Key: ')
    consumer_secret = input('Enter Consumer Secret: ')
    access_token = input('Enter Access Token: ')
    access_token_secret = input('Enter Access Token Secret: ')
    
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    
    date_since = datetime.today().strftime('%Y-%m-%d')
    
    tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since).items(100)#assuming 100 is the maximum number of tweets with a specific keyword
    [print(tweet.text) for tweet in tweets]
    

if __name__ == "__main__":
    keyword = sys.argv[1]
    display_tweets(keyword)

