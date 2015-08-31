from django.conf.urls import patterns, url
from django.views.generic import TemplateView

import position.views

urlpatterns = patterns(
    '',
    url(r'^location$', position.views.LocationPattern.as_view(), name='location'),
    url(r'^timeline', TemplateView.as_view(template_name="location_timeline.html")),
    url(r'^calendar$', position.views.LocationCalendarView.as_view(), name='calendar'),
)
