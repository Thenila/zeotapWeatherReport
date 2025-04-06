import requests
from datetime import datetime
from db import store_daily_summary

API_KEY = 'b9881dfa93f9a336994b84a4563c403f'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.json().get('message')}")
        return None

def process_weather_data(data):
    if data:
        city = data['name']
        main_weather = data['weather'][0]['main']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        date_str = datetime.now().strftime('%Y-%m-%d')

        print(f"\n📍 City: {city}")
        print(f"🌤️ Weather: {main_weather}")
        print(f"🌡️ Temp: {temp}°C (Feels like {feels_like}°C)")
        print(f"🔺 Max: {temp_max}°C, 🔻 Min: {temp_min}°C")

        summary = {
            'city': city,
            'date': date_str,
            'avg_temp': temp,
            'max_temp': temp_max,
            'min_temp': temp_min,
            'dominant_condition': main_weather
        }

        store_daily_summary(summary)
        print("✅ Summary stored in database.\n")
    else:
        print("❌ No data to process.")
