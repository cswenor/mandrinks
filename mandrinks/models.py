from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
	name = models.CharField(max_length=200)
	event_start = models.DateTimeField()
	duration = models.FloatField()
	attendees = models.ManyToManyField(User, blank=True)