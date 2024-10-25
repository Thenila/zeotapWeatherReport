import time
import requests
from weather_service import get_weather_data, process_weather_data

# Constants and configuration
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
INTERVAL = 300  # Time interval in seconds (e.g., 300 seconds for 5 minutes)

def main():
    print("Starting the Weather Monitoring System...")

    try:
        while True:
            for city in CITIES:
                print(f"\nFetching weather data for {city}...")
                weather_data = get_weather_data(city)  # Fetch the weather data
                if weather_data:
                    process_weather_data(weather_data)  # Process and display summary

            print(f"Waiting for {INTERVAL} seconds before the next update...\n")
            time.sleep(INTERVAL)  # Wait for the defined interval (e.g., 5 minutes)

    except KeyboardInterrupt:
        print("\nProgram stopped by the user.")

if __name__ == "__main__":
    main()
