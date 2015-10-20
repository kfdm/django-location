from django.contrib import admin, messages

from position.models import Location


class LocationAdmin(admin.ModelAdmin):
    def calculate_diff(self, request, queryset):
        try:
            diff = queryset[0].created - queryset[1].created
            self.message_user(request, "Time delta is %s." % diff)
        except:
            self.message_user(request, "Error calculating difference. len(%d)" % len(queryset), messages.ERROR)
    calculate_diff.short_description = 'Calculate difference between two times'

    actions = ['calculate_diff']
    list_display = ('label', 'created', 'state')
    list_filter = ('label', 'state')

admin.site.register(Location, LocationAdmin)
