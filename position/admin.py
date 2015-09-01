from django.contrib import admin, messages

from position.models import Location


class LocationAdmin(admin.ModelAdmin):
    def _location_url(self, obj):
        return '<a href="{0}">Google Maps</a>'.format(obj.location)
    _location_url.short_description = 'Location'
    _location_url.allow_tags = True

    def calculate_diff(self, request, queryset):
        try:
            diff = queryset[0].created - queryset[1].created
            self.message_user(request, "Time delta is %s." % diff)
        except:
            self.message_user(request, "Error calculating difference. len(%d)" % len(queryset), messages.ERROR)
    calculate_diff.short_description = 'Calculate difference between two times'

    actions = ['calculate_diff']
    list_display = ('label', 'created', 'state', '_location_url')
    list_filter = ('label', 'state')

admin.site.register(Location, LocationAdmin)
