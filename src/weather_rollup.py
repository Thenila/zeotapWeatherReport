from datetime import time
import statistics
from collections import Counter
from db import store_daily_summary

def calculate_daily_summary(city, weather_data):
    temperatures = [entry['temp'] for entry in weather_data]
    conditions = [entry['main'] for entry in weather_data]

    avg_temp = statistics.mean(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)

    dominant_condition = Counter(conditions).most_common(1)[0][0]

    summary = {
        'city': city,
        'date': time.strftime('%Y-%m-%d'),
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_condition': dominant_condition
    }
    
    store_daily_summary(summary)
    return summary
