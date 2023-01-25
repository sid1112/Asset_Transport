from django.db import models

from Asset_Transport_App.enums import *


class Requester(models.Model):
    fromLocation = models.CharField(max_length=255)
    toLocation = models.CharField(max_length=255)
    dateTime = models.DateTimeField()
    flexibleTimings = models.BooleanField()
    numberOfAssets = models.IntegerField()
    assetType = models.CharField(max_length=255, choices=AssetType.choices())
    assetSensitivity = models.CharField(max_length=255, choices=AssetSensitivity.choices())
    whomToDeliver = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=RequestStatus.choices())


class Riders(models.Model):
    fromLocation = models.CharField(max_length=255)
    toLocation = models.CharField(max_length=255)
    dateTime = models.DateTimeField()
    flexibleTimings = models.BooleanField()
    numberOfAssets = models.IntegerField()
    travelMedium = models.CharField(max_length=255, choices=TravelMedium.choices())
    status = models.CharField(max_length=255, choices=MatchedRequestStatus.choices())
    acceptedPersonDetails = models.CharField(max_length=255, null=True, blank=True)
