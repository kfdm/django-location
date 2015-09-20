from django.db import models
from django.utils.timezone import now


class Location(models.Model):
    created = models.DateTimeField(default=now)
    label = models.TextField()
    location = models.TextField()
    state = models.CharField(
        max_length=16,
        choices=(
            ('', 'Unselected'),
            ('entered', 'Entered an Area'),
            ('exited', 'Exited an Area'),
            ('Do Button', 'Test Entry'),
        )
    )
