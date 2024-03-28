from django.contrib import admin
from django.urls import path
#from location.views import locationList, locationCreate,location
from location.views import LocationList, LocationCreate, LocationDetail

urlpatterns = [
    path('location/list/', LocationList.as_view()),
    path('location/create/', LocationCreate.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view())
]
