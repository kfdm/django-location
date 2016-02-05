from django.conf.urls import url
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

import position.views

urlpatterns = [
    url(r'^location$', position.views.LocationPattern.as_view(), name='location'),
    url(r'^timeline', TemplateView.as_view(template_name="position/chart/timeline.html"), name='timeline'),
    url(r'^calendar$', position.views.LocationCalendarView.as_view(), name='calendar'),
]


def subnav(namespace, request):
    if request.user.is_authenticated():
        return {
            _('Location'): [
                (_('timeline'), reverse(namespace + ':timeline')),
                (_('calendar'), reverse(namespace + ':calendar')),
            ]
        }
    return {}
