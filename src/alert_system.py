def check_thresholds(weather_data, temp_threshold=35):
    for data in weather_data:
        if data['temp'] > temp_threshold:
            print(f"ALERT: {data['city']} temperature exceeds {temp_threshold}°C. Current: {data['temp']:.2f}°C")
