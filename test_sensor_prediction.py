import unittest
import numpy as np
from datetime import datetime, timedelta
from sensor_prediction import (
    predict_sensor_trend,
    max_consecutive,
    analyze_trend_origin,
    calculate_time_to_threshold
)

class TestSensorPrediction(unittest.TestCase):
    
    def test_max_consecutive(self):
        """Test the max_consecutive function"""
        self.assertEqual(max_consecutive([]), 0)
        self.assertEqual(max_consecutive([False, False, False]), 0)
        self.assertEqual(max_consecutive([True, True, False, True]), 2)
        self.assertEqual(max_consecutive([False, True, True, True, False, True]), 3)
        self.assertEqual(max_consecutive([True, True, True]), 3)
    
    def test_analyze_trend_origin(self):
        """Test the analyze_trend_origin function"""
        # Test with stable data
        stable_data = np.ones(20)
        result = analyze_trend_origin(stable_data)
        self.assertIn("potential_causes", result)
        self.assertIn("confidence", result)
        self.assertIn("recommended_actions", result)
        
        # Test with trending data
        trending_data = np.linspace(1, 10, 20)
        result = analyze_trend_origin(trending_data)
        self.assertIn("potential_causes", result)
        
        # Test with related sensors
        related_sensors = {
            "sensor1": np.linspace(1, 10, 20),  # Correlated
            "sensor2": np.random.rand(20)  # Not correlated
        }
        result = analyze_trend_origin(trending_data, related_sensors)
        self.assertIn("potential_causes", result)
        
        # Test with maintenance history
        maintenance_history = [
            {"date": datetime.now() - timedelta(days=10), "type": "calibration"},
            {"date": datetime.now() - timedelta(days=60), "type": "replacement"}
        ]
        result = analyze_trend_origin(trending_data, None, maintenance_history)
        self.assertIn("potential_causes", result)
    
    def test_calculate_time_to_threshold(self):
        """Test the calculate_time_to_threshold function"""
        # Test with increasing trend
        data = np.linspace(5, 9, 10)
        predictions = [10, 11, 12]
        result = calculate_time_to_threshold(data, predictions, 0, 15)
        self.assertEqual(result["trend_direction"], "increasing")
        self.assertIsNotNone(result["time_to_max_threshold"])
        
        # Test with decreasing trend
        data = np.linspace(15, 10, 10)
        predictions = [9, 8, 7]
        result = calculate_time_to_threshold(data, predictions, 5, 20)
        self.assertEqual(result["trend_direction"], "decreasing")
        self.assertIsNotNone(result["time_to_min_threshold"])
        
        # Test with stable trend
        data = np.ones(10) * 7
        predictions = [7, 7, 7]
        result = calculate_time_to_threshold(data, predictions, 5, 10)
        self.assertEqual(result["trend_direction"], "stable")
    
    def test_predict_sensor_trend_normal(self):
        """Test prediction with normal data (within thresholds)"""
        # Generate some stable sensor data
        sensor_data = [5.0, 5.1, 5.2, 5.0, 5.1, 5.2, 5.0, 5.1, 5.2, 5.0]
        
        # Run prediction
        result = predict_sensor_trend(
            sensor_data=sensor_data,
            min_tolerance_threshold=4.0,
            max_tolerance_threshold=6.0,
            prediction_window=3,
            alert_threshold=2
        )
        
        # Check results
        self.assertIn("predicted_values", result)
        self.assertEqual(len(result["predicted_values"]), 3)
        self.assertFalse(result["alert_triggered"])
        self.assertGreater(result["confidence_score"], 0)
    
    def test_predict_sensor_trend_alert(self):
        """Test prediction with data trending toward threshold"""
        # Generate increasing sensor data
        sensor_data = [5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6, 6.8]
        
        # Run prediction
        result = predict_sensor_trend(
            sensor_data=sensor_data,
            min_tolerance_threshold=4.0,
            max_tolerance_threshold=7.0,
            prediction_window=3,
            alert_threshold=2
        )
        
        # Check results
        self.assertIn("predicted_values", result)
        self.assertEqual(len(result["predicted_values"]), 3)
        # The trend should continue upward and cross the max threshold
        self.assertTrue(result["alert_triggered"])
        self.assertGreater(result["confidence_score"], 0)
        self.assertEqual(result["time_to_threshold"]["trend_direction"], "increasing")

if __name__ == "__main__":
    unittest.main()