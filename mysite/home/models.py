import datetime

from django.db import models
from django.utils import timezone

class Contact(models.Model):
	timesent = models.DateTimeField('time sent')
	name = models.CharField(max_length = 64)
	email = models.EmailField(max_length = 64)
	subject = models.CharField(max_length = 128)
	message = models.TextField(blank=True)