'''
Created on March 2, 2014
@author: Kenneth G. Wang, Nathaniel H. Lash

This is a program for parsing json obtained via
https://api.twitter.com/1.1/lists/statuses.json?owner_screen_name=kennywang&slug=green-scene-test
'''

import json
from TwitterAPI import TwitterAPI
from greenscene.keys import *
from greenscene.apps.Unofficial.models import *
from django.core.management.base import BaseCommand, CommandError
from time import strptime, strftime
from string import split

class Command(BaseCommand):
    def handle(self, *args, **options):
        api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
        r = api.request('lists/statuses', {'owner_screen_name':'kennywang', 'slug':'green-scene-test'})

        for item in r.get_iterator():
            print item


        def filter_tweets(data):
            tweet_list = []
            hashtarget = "GreenScene"
            for tweet in data:
            	for hashtag in tweet['entities']['hashtags']:
            		if hashtarget in hashtag['text']:
            			tweet_list.append(tweet)
            return tweet_list

        def load_tweets(tweets):
            for tweet in tweets:
                



        load_tweets(tweet_list)