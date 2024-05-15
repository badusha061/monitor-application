def is_condition_met(record , weather_data):
    if record.temperature <= weather_data['temperature'] and record.rainfall <= weather_data['rainfall']:
        return True
    else:
        return False