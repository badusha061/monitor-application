from .serializers import WeatherCondiotionSerializer , RecordSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from weather.models import Record , WeatherCondition
from .pagination import WeatherPagination , RecordsPagination
from rest_framework.filters import OrderingFilter , SearchFilter
from rest_framework.decorators import permission_classes
from rest_framework.permissions import  IsAuthenticated
from dotenv import load_dotenv
load_dotenv()
import os
import requests



@permission_classes(IsAuthenticated)
class ListCreateWeatherCondtion(ListCreateAPIView):
    serializer_class = WeatherCondiotionSerializer
    pagination_class = WeatherPagination
    filter_backends = (OrderingFilter , SearchFilter)
    search_fields  = ['comparison_operator']
    queryset = None
    try:
        queryset = WeatherCondition.objects.all()
    except Exception as e:
        queryset = None


@permission_classes(IsAuthenticated)
class ListCreateRecords(ListCreateAPIView):
    serializer_class  = RecordSerializer
    pagination_class  = RecordsPagination
    filter_backends = (OrderingFilter , SearchFilter)
    search_fields = ['user','weather_condition','status']
    
    queryset = None
    try:
        queryset = Record.objects.all()
    except Exception as e:
        queryset = None



@permission_classes(IsAuthenticated)
class RetrieUpateDestoryWeatherCondtion(RetrieveUpdateDestroyAPIView):
    serializer_class = WeatherCondiotionSerializer
    queryset = None
    try:
        queryset = WeatherCondition.objects.all()
    except Exception as e:
        queryset = None



@permission_classes(IsAuthenticated)
class RetrieUpateDestoryRecords(RetrieUpateDestoryWeatherCondtion):
    serializer_class = RecordSerializer 
    queryset = None
    try:
        queryset = Record.objects.all()
    except Exception as e:
        queryset = None

def Fetch_Weather_API():
    api_key =os.getenv('WEATHER_API')
    city = 'kozhikkode'
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q=${city}'
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
        return weather_data
    else:
  
        print(f"Error: {response.status_code}")
        return None



