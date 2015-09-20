from rest_framework import serializers

from position.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        read_only = ('created',)
        fields = ('label', 'location', 'state')
