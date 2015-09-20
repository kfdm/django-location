from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


class Location(models.Model):
    created = models.DateTimeField(default=now)
    label = models.TextField()
    location = models.TextField()
    state = models.CharField(
        max_length=16,
        choices=(
            ('', _('Unselected')),
            ('entered', _('Entered an Area')),
            ('exited', _('Exited an Area')),
            ('Do Button', _('Test Entry')),
        )
    )
