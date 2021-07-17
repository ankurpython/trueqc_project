from rest_framework import serializers

from weather_api.models import WeatherData


class WeatherSerializers(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'
