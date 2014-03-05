from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=100)
	handle = models.CharField(max_length=30)
	link = models.CharField(max_length=100, null = True, blank=True)
	image_url = models.CharField(max_length=100, null = True, blank = True)


class Tweet(models.Model):
	user = models.ForeignKey(User, null = True)
	tweet_id = models.CharField(max_length=50)

	coordinate_string = models.CharField(max_length=255, null = True)	
	lat = models.FloatField(default = 0)
	longi = models.FloatField(default= 0)

	created = models.DateTimeField()
	text = models.CharField(max_length=150)

	image_url = models.CharField(max_length=100, null = True)
	tweet_url = models.CharField(max_length=100, null = True)

	def save(self, *args, **kwargs):
		super(Tweet, self).save(*args, **kwargs)