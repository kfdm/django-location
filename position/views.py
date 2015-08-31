import datetime
import json

import pytz
from django.http import HttpResponse
from django.views.generic.base import View
from icalendar import Calendar, Event
from rest_framework import mixins, viewsets
from rest_framework.decorators import list_route

from position.models import Location
from position.serializers import LocationSerializer


class LocationCalendarView(View):
    def get(self, request):
        now = datetime.datetime.now(pytz.utc)
        delta = datetime.timedelta(days=7)

        cal = Calendar()
        cal.add('prodid', '-//My calendar product//mxm.dk//')
        cal.add('version', '2.0')

        locations = {}
        for location in Location.objects.filter(created__gte=datetime.datetime.now() - delta):
            if location.state == 'entered':
                locations[location.label] = location.created
            elif location.state == 'exited':
                if location.label in locations:
                    entered = locations.pop(location.label)

                    event = Event()
                    event.add('summary', location.label)
                    event.add('dtstart', entered)
                    event.add('dtend', location.created)
                    event['uid'] = location.id
                    cal.add_component(event)

        # Check for any remaining locations that have not been 'popped'
        # and assume we're currently located there

        for label, entered in locations.items():
            event = Event()
            event.add('summary', label)
            event.add('dtstart', entered)
            event.add('dtend', now.replace(minute=0, second=0, microsecond=0))
            cal.add_component(event)

        return HttpResponse(
            content=cal.to_ical(),
            content_type='text/plain; charset=utf-8'
        )


class LocationPattern(View):
    def get(self, request):
        response = HttpResponse(content_type='text/plain')
        response.write(json.dumps({
            'created': '{{OccurredAt}}',
            'label': '<label>',
            'state': '{{EnteredOrExited}}',
            'location': '{{LocationMapUrl}} ',
        }))
        return response


class LocationViewSet(
        mixins.CreateModelMixin,
        # mixins.ListModelMixin,
        # mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    """
    POST Only View to accept location updates from IFTTT
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @list_route()
    def datatable(self, request):
        def dateformat(date):
            return "Date(%d,%d,%d,%d,%d,%d)" % (
                date.year, date.month - 1, date.day, date.hour, date.minute, date.second)

        delta = datetime.timedelta(days=7)
        dataset = {'cols': [
            {'id': 'Location', 'label': 'Location', 'type': 'string'},
            {'id': 'Duration', 'label': 'Duration', 'type': 'string'},
            {'id': 'Enter', 'pattern': 'yyyy/MM/dd H:mm:ss', 'type': 'datetime'},
            {'id': 'Exit', 'pattern': 'yyyy/MM/dd H:mm:ss', 'type': 'datetime'},
            {"id": "", "label": "", "pattern": "", "type": "string", "p": {"role": "tooltip"}},
        ], 'rows': []}
        # Later try to get proper tooltips working
        # http://stackoverflow.com/a/11181882/622650

        locations = {}
        for location in Location.objects.filter(created__gte=datetime.datetime.now() - delta):
            if location.state == 'entered':
                locations[location.label] = location.created
            elif location.state == 'exited':
                if location.label in locations:
                    entered = locations.pop(location.label)
                    dataset['rows'].append({'c': [
                        {"v": location.label},
                        {"v": str(location.created - entered)},
                        {"v": dateformat(entered)},
                        {"v": dateformat(location.created)},
                        {"v": str(location.created - entered)},
                    ]})

        # Check for any remaining locations that have not been 'popped'
        # and assume we're currently located there
        now = datetime.datetime.now(pytz.utc).replace(microsecond=0)
        for label, entered in locations.items():
            entered = entered.replace(microsecond=0)
            dataset['rows'].append({'c': [
                {"v": label},
                {"v": str(now - entered)},
                {"v": dateformat(entered)},
                {"v": dateformat(now)},
                {"v": str(now - entered)},
            ]})

        response = HttpResponse(content_type='application/json')
        response.write('google.visualization.Query.setResponse(' + json.dumps({
            'version': '0.6',
            'table': dataset,
            'reqId': '0',
            'status': 'ok',
        }) + ');')
        return response
