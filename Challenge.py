

import tweepy as tw
import sys
from datetime import datetime



def displayTweets(search_words):
    consumer_key= 'kCvcaIvht30cgYCkiOFnAduK1'
    consumer_secret= 'Pgom2RYGdMI7jttzXvaQpmohrVOysYRg8wOZa4XDe4dFaCBOnD'
    access_token= '191563270-MlLYQskzpZxjuRqKK4Kp8GtOBZlgTTiomFq7fQPb'
    access_token_secret= 'thcmrJjj4KtyqBpsEsRPgJMcz1DlmRzIWgCS61A5156iE'
    
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    
    date_since = datetime.today().strftime('%Y-%m-%d')
    
    tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since).items(100)#assuming 100 is the maximum number of tweets with a specific keyword
    [print(tweet.text) for tweet in tweets]
    

if __name__ == "__main__":
    keyword = sys.argv[1]
    displayTweets(keyword)

