import unittest
from weather_rollup import calculate_daily_summary

class TestWeatherRollup(unittest.TestCase):

    def test_calculate_daily_summary(self):
        sample_data = [
            {'temp': 30, 'main': 'Clear'},
            {'temp': 35, 'main': 'Clouds'},
            {'temp': 32, 'main': 'Clear'}
        ]
        summary = calculate_daily_summary('Delhi', sample_data)
        self.assertEqual(summary['avg_temp'], 32.33)
        self.assertEqual(summary['dominant_condition'], 'Clear')

if __name__ == '__main__':
    unittest.main()
