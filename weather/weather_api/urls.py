from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from weather_api.views import *

router = DefaultRouter()
router.register('fetch_weather_data', FetchWeatherData, basename='fetch_weather_data')
router.register('weather_data', Weather, basename='weather_data')
router.register('weather_csv', WeatherCSV, basename='weather_csv')


urlpatterns = [
    path("", include(router.urls)),
]
