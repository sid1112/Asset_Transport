from .models import Requester, Riders
from rest_framework import serializers


class RequesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requester
        fields = ['id', 'fromLocation', 'toLocation', 'dateTime', 'flexibleTimings', 'numberOfAssets', 'assetType',
                  'assetSensitivity', 'whomToDeliver', 'status']


class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riders
        fields = ['id', 'fromLocation', 'toLocation', 'dateTime', 'flexibleTimings', 'numberOfAssets',
                  'status', 'travelMedium', 'acceptedPersonDetails']
