from django.db import models
from django.utils.timezone import now


class Location(models.Model):
    created = models.DateTimeField(default=now)
    label = models.TextField()
    location = models.TextField()
    state = models.TextField()
