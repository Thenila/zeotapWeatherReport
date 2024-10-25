import unittest
from alert_system import check_thresholds

class TestAlertSystem(unittest.TestCase):

    def test_check_thresholds(self):
        weather_data = [{'city': 'Delhi', 'temp': 37}]
        check_thresholds(weather_data, temp_threshold=35)
        # Ensure this triggers an alert, can be done using mock objects

if __name__ == '__main__':
    unittest.main()
