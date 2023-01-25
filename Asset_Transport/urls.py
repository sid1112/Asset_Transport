from django.contrib import admin
from django.urls import path

from Asset_Transport_App.views import requesterListView
from Asset_Transport_App.views import riderListView
from Asset_Transport_App.views import riderView
from Asset_Transport_App.views import matchedTransportRequestListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/requester/', requesterListView),
    path('api/rider/', riderListView),
    path('api/rider/<int:pk>', riderView),
    path('api/matchAssetTransport/', matchedTransportRequestListView)

]
