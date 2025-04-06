import time
import requests
from weather_service import get_weather_data, process_weather_data
from db import init_db  

CITIES = ['Delhi', 'Mumbai', 'Erode', 'Bangalore', 'Kolkata', 'Hyderabad']
INTERVAL = 300  

def main():
    print("Starting the Weather Monitoring System...")

    init_db()  

    try:
        while True:
            for city in CITIES:
                print(f"\nFetching weather data for {city}...")
                weather_data = get_weather_data(city)  
                if weather_data:
                    process_weather_data(weather_data)  

            print(f"Waiting for {INTERVAL} seconds before the next update...\n")
            time.sleep(INTERVAL)  

    except KeyboardInterrupt:
        print("\nProgram stopped by the user.")

if __name__ == "__main__":
    main()
