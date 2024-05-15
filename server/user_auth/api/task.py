from celery import shared_task
from datetime import datetime , timedelta
from weather.models  import Record 
from weather.api.views import Fetch_Weather_API
from .utils import is_condition_met

@shared_task
def add(x,y):
    print('come')
    print('come')
    print('come')
    print('come')
    print('come')
    print('come')
    print('come')
    return x + y

@shared_task
def test_celery_beat():
    print(f"The task is excuted {datetime.now()}")
    print(f"The task is excuted {datetime.now()}")
    print(f"The task is excuted {datetime.now()}")
    print(f"The task is excuted {datetime.now()}")
    print(f"The task is excuted {datetime.now()}")
    print(f"The task is excuted {datetime.now()}")


@shared_task
def Update_Record_Status():
    weather_data = Fetch_Weather_API()
    records = Record.objects.all()
    for record in records:
        if record.is_condition_met(weather_data):
            record.status = "Completed"
            record.save()

