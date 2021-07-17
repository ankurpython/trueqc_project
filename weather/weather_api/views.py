import pandas as pd
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response

from weather_api.models import WeatherData
from weather_api.serializers import WeatherSerializers
from weather_api.weather_data import weather_data


class FetchWeatherData(viewsets.ViewSet):

    @staticmethod
    def create(request):
        data = request.data
        data = weather_data(data['lat'], data['lon'])
        return Response(data)


class Weather(viewsets.ModelViewSet):
    serializer_class = WeatherSerializers
    queryset = WeatherData.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['weather_main', 'weather_description', 'temp']
    search_fields = ['temp']
    ordering_fields = ['dt', 'sunrise', 'sunset']


class WeatherCSV(viewsets.ViewSet):

    @staticmethod
    def create(request):
        data = request.data
        dt = WeatherData.objects.filter(**data).values()
        df = pd.DataFrame(dt) #dict to pandas dataframe

        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="weather_data.csv"'},
        )

        df.to_csv(response, index=False)

        return response
