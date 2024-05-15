from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User

# Create your models here.


class WeatherCondition(models.Model):
    temperature_threshold = models.FloatField()
    rainfall_threshold = models.FloatField()
    comparison_operator = models.CharField(max_length=2, choices=[('<', '<'), ('>', '>'), ('<=', '<='), ('>=', '>='), ('==', '==')])
    FREQUENCY_CHOICES = [
        ('Daily', 'Daily'),
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly')
    ]
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)

    def __str__(self) -> str:
        return self.frequency


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    weather_condition = models.ForeignKey(WeatherCondition, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="Pending")
    last_checked = models.DateTimeField(auto_now=True)
    next_check = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username_validator