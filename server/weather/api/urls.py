from django.urls import path
from .views import * 

urlpatterns = [
    path('weather/', ListCreateWeatherCondtion.as_view(), name='creating-weather'),
    path('weather-update/<int:pk>/', RetrieUpateDestoryWeatherCondtion.as_view(), name='upate-weather'),
    path('records/', ListCreateRecords.as_view(), name='creating-records'),
    path('records-update/<int:pk>/', RetrieUpateDestoryRecords.as_view(), name='creating-weather'),
]

