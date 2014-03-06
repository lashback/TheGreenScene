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
from string import split
#from time import strptime, strftime
import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
        #r = api.request('lists/statuses', {'owner_screen_name':'kennywang', 'slug':'green-scene-test'})
        r = api.request('lists/statuses', {'owner_screen_name':'thedailyillini', 'slug':'our-reporters'})
        print r
        
        #todo: build in error codes. What happens when we go over our rate limit?
        def filter_tweets(data):
            tweet_list = []
            hashtarget = "Unofficial"
            for tweet in data:
            	for hashtag in tweet['entities']['hashtags']:
            		if hashtarget in hashtag['text']:
            			tweet_list.append(tweet)
            print tweet_list
            return tweet_list

        def load_tweets(tweets):
            for tweet in tweets:
                print tweet
                handle = tweet['user']['screen_name']
                name = tweet['user']['name']
                print name
                user_image = tweet['user']['profile_image_url']
                print handle

                tweet_id = tweet['id']
                print tweet_id
                coordinate_string = tweet['coordinates']
                print coordinate_string
                created = tweet['created_at']
                print created
                created = datetime.datetime.strptime(created, '%a %b %d %H:%M:%S +0000 %Y')
                created_string = created.strftime('%Y-%m-%d %H:%M:%S')
                print created
                text = tweet['text']
                print text

                retweets = tweet['retweet_count']


                #image_url = tweet['entities']['media'][0]['media_url']

                
                for entity in tweet['entities']:
                    if 'media' in entity:
                        image_url = tweet['entities']['media'][0]['media_url']
                        print image_url


                user_import, user_created = User.objects.get_or_create(
                    name = name,
                    handle = handle,
                    image_url = user_image
                    )

                tweet_import, tweet_create = Tweet.objects.get_or_create(
                    user = user_import,
                    tweet_id = tweet_id,
                    coordinate_string = coordinate_string,
                    created = created_string,
                    text = text
                    )
                if image_url:
                    tweet_import.image_url = image_url
                    tweet_import.save()

                tweet_url = "http://twitter.com/%s/status/%s" %(name, tweet_id)
                tweet_import.tweet_url = tweet_url
                tweet_import.save()


        tweets = filter_tweets(r)
        load_tweets(tweets)



        #load_tweets(tweet_list)