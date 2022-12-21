from django.contrib import admin
from django.urls import path

from test1.views import requesterListView
from test1.views import riderListView
from test1.views import riderView
from test1.views import matchedTransportRequestListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/requester/', requesterListView),
    path('api/rider/', riderListView),
    path('api/rider/<int:pk>', riderView),
    path('api/matchAssetTransport/', matchedTransportRequestListView)

]
