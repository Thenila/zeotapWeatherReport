import unittest
from weather_service import kelvin_to_celsius, get_weather_data

class TestWeatherService(unittest.TestCase):

    def test_kelvin_to_celsius(self):
        self.assertEqual(kelvin_to_celsius(273.15), 0)
        self.assertEqual(kelvin_to_celsius(300), 26.85)

    def test_get_weather_data(self):
        # You can use mock responses for unit testing here
        pass

if __name__ == '__main__':
    unittest.main()
