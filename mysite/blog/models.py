import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
	id = models.IntegerField(primary_key=True)
	published = models.DateTimeField('date published')
	title = models.CharField(max_length = 100)
	text = models.TextField(blank=True)
