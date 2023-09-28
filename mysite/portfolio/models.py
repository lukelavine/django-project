import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class PortfolioEntry(models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length = 100)
	text = models.TextField(blank=True)
	date = models.DateTimeField('date published')
	icon = models.CharField(max_length = 32)