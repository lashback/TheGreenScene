from tastypie.contrib.resources import ModelResource  # Using GeoDjango ModelResource
from django.http import HttpResponse
from tastypie.resources import ALL, ALL_WITH_RELATIONS
from apps.Unofficial.models import Tweet, User
from tastypie.cache import SimpleCache
from django.utils import simplejson as json


class TweetResource(ModelResource):
    class Meta:
        queryset = Tweet.objects.all()
        resource_name = "tweet"
        allowed_methods = ['get']
        filtering = {
            'created': ('gte', 'lte')

        }
        cache = SimpleCache(timeout=5)
        max_limit = 20



        def dehydrate(self, bundle):
            bundle.data['geometry'] = "coordinates": bundle.obj.coordinate_string
            bundle.data['type'] = "Feature"
            bundle.data['properties'] = {
                                        "name": bundle.obj.User.name,
                                        "handle": bundle.obj.User.handle,
                                        "userlink": bundle.obj.User.link,
                                        "image_url": bundle.obj.User.image_url,

                                        "id": bundle.obj.tweet_id,
                                        "created": bundle.obj.created,
                                        "text": bundle.obj.text,

                                        "image_url": bundle.obj.image_url,
                                        "tweet_url": bundle.obj.tweet_url
            }
