from weather.models import WeatherCondition ,Record 
from rest_framework.serializers import ModelSerializer
from user_auth.api.serializers import UserSerializerList


class WeatherCondiotionSerializer(ModelSerializer):
    class Meta:
        model = WeatherCondition
        fields = ['id','temperature_threshold','rainfall_threshold','comparison_operator','frequency']


class RecordSerializer(ModelSerializer):
    class Meta:
        model = Record
        fields = ['id','user','weather_condition','status','last_checked','next_check']