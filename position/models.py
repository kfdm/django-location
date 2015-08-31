from django.db import models


class Location(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    label = models.TextField()
    location = models.TextField()
    state = models.TextField()
