from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=100)
	handle = models.CharField(max_length=30)
	link = models.CharField(max_length=100)
	image_url = models.CharField(max_length=100, null = True, blank = True)


class Tweet(models.Model):
	user = models.ForeignKey(User, null = True)
	tweet_id = models.CharField(max_length=50)

	coordinate_string = models.CharField(max_length=255, null = True)	
	lat = models.FloatField()
	longi = models.FloatField()

	created = models.DateTimeField()
	text = models.CharField(max_length=150)

	image_url = models.CharField(max_length=100)
	tweet_url = models.CharField(max_length=100)

