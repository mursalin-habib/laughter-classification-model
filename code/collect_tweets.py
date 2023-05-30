import tweepy
import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

joy_tweets = tweepy.Cursor(api.search_tweets, lang = "en", q = "(\U0001F923 OR \U0001F602 OR \U0001f606) AND (-(#Hilarious) OR #ROFL OR #lol OR #lmao OR #lmfao OR #lololol OR #looool) AND (#happyness OR #happy OR #joy OR #laughter OR #fun OR #Celebrate OR #Celetration OR #cute OR #Joyful OR #Blessed OR #Greatful OR #GoodVibes #enjoy OR #Enjoying OR #funTime) AND -filter:retweets", tweet_mode = 'extended').items(30)

columns = ['Label', 'Tweet']
data = []

for tweet in joy_tweets :
    data.append(['Joyous', tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)

df.to_csv('joy_tweets.csv')


schadenfrude_tweets = tweepy.Cursor(api.search_tweets, lang = "en", q = "(\U0001F480 OR \U0001F639 OR \U0001F923 OR \U0001F602 OR #Hilarious OR #ROFL OR #lol OR #lmao OR #lmfao OR hahaha) AND (#schadenfreude OR #karma OR #MiseryLovesCompany OR #Roasting OR #HumbleBrag OR #KarmaIsABitch OR #failarmy OR #Fights OR #brawls OR #SchoolFights OR #ByeFelicia OR #EvilLaugh OR #InstantKarma OR #HumbleBrag OR #lessonLearned OR #Revenge) AND -filter:retweets", tweet_mode = 'extended').items(1000)

columns = ['Label', 'Tweet']
data = []

for tweet in schadenfrude_tweets :
    data.append(['Schadenfreude', tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)

df.to_csv('Schadenfreude_tweets.csv')

sarcasm_tweets = tweepy.Cursor(api.search_tweets, lang = "en", q = "(\U0001F92D OR \U0001F61D OR \U0001F480 OR \U0001F638 OR \U0001F639 OR \U0001F923 OR \U0001F602 OR \U0001f606) OR (#irony OR #ROFL OR #Hilarious OR #lol OR #lmao OR #lmfao OR #lololol OR #looool) AND (#Sarcasm OR #SarcasmAlert OR #SarcasmDetected OR #SarcasmOverload OR #NotReally OR #JustKidding OR #NotSerious OR #Irony OR #ironic OR #TongueInCheek OR #SarcasmByAssociation OR #BeingSarcastic OR #SorryNotSorry OR #ISaidWhatISaid) AND -filter:retweets", tweet_mode = 'extended').items(1000)

columns = ['Label', 'Tweet']
data = []

for tweet in sarcasm_tweets :
    data.append(['Sarcasm', tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)

df.to_csv('sarcasm_tweets.csv')

#This code was adapted from following github repository https://github.com/mehranshakarami/AI_Spectrum/blob/main/2021/Twitter_API/twitter_api.py