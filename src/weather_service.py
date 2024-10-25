import requests

API_KEY = 'b9881dfa93f9a336994b84a4563c403f'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to get weather data for a given city
def get_weather_data(city):
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # Fetch data in Celsius
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            print(f"Failed to retrieve data for {city}. Error: {data.get('message')}")
            return None
    except Exception as e:
        print(f"Error while fetching data: {e}")
        return None

# Function to process and display the weather data
def process_weather_data(data):
    if data:
        city = data['name']
        main_weather = data['weather'][0]['main']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']

        print(f"City: {city}")
        print(f"Main weather: {main_weather}")
        print(f"Temperature: {temp}°C")
        print(f"Feels like: {feels_like}°C")
    else:
        print("No data to process.")
