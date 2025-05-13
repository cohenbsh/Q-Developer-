"""
Unit tests for the statistical_functions module.
"""

import unittest
import numpy as np
from statistical_functions import summarize_figures


class TestSummarizeFigures(unittest.TestCase):
    """Test cases for the summarize_figures function."""
    
    def test_basic_statistics(self):
        """Test basic statistical calculations."""
        data = [1, 2, 3, 4, 5]
        result = summarize_figures(data)
        stats = result['statistics']
        
        self.assertEqual(stats['mean'], 3.0)
        self.assertEqual(stats['median'], 3.0)
        self.assertEqual(stats['mode'], 1)  # First value when all occur once
        self.assertEqual(stats['range'], 4.0)
        self.assertEqual(stats['min'], 1.0)
        self.assertEqual(stats['max'], 5.0)
        self.assertAlmostEqual(stats['std_dev'], 1.4142135623730951)
        
        # Test quartiles
        self.assertEqual(stats['quartiles']['Q1'], 2.0)
        self.assertEqual(stats['quartiles']['Q2'], 3.0)
        self.assertEqual(stats['quartiles']['Q3'], 4.0)
    
    def test_order_analysis(self):
        """Test order analysis functionality."""
        # Ascending data
        asc_data = [1, 2, 3, 4, 5]
        asc_result = summarize_figures(asc_data)
        self.assertTrue(asc_result['order_analysis']['is_ascending'])
        self.assertFalse(asc_result['order_analysis']['is_descending'])
        self.assertTrue(asc_result['order_analysis']['consistent_step'])
        self.assertEqual(asc_result['order_analysis']['step_size'], 1.0)
        
        # Descending data
        desc_data = [5, 4, 3, 2, 1]
        desc_result = summarize_figures(desc_data)
        self.assertFalse(desc_result['order_analysis']['is_ascending'])
        self.assertTrue(desc_result['order_analysis']['is_descending'])
        self.assertTrue(desc_result['order_analysis']['consistent_step'])
        self.assertEqual(desc_result['order_analysis']['step_size'], -1.0)
        
        # Unordered data
        unord_data = [3, 1, 4, 2, 5]
        unord_result = summarize_figures(unord_data)
        self.assertFalse(unord_result['order_analysis']['is_ascending'])
        self.assertFalse(unord_result['order_analysis']['is_descending'])
        self.assertFalse(unord_result['order_analysis']['consistent_step'])
    
    def test_pattern_detection(self):
        """Test pattern detection functionality."""
        # Arithmetic sequence
        arith_data = [2, 4, 6, 8, 10]
        arith_result = summarize_figures(arith_data)
        self.assertEqual(arith_result['order_analysis']['pattern'], 'arithmetic sequence')
        
        # Geometric sequence
        geom_data = [2, 4, 8, 16, 32]
        geom_result = summarize_figures(geom_data)
        self.assertEqual(geom_result['order_analysis']['pattern'], 'geometric sequence')
    
    def test_summary_generation(self):
        """Test that a summary is generated."""
        data = [1, 2, 3, 4, 5]
        result = summarize_figures(data)
        self.assertIsInstance(result['summary'], str)
        self.assertGreater(len(result['summary']), 0)
    
    def test_error_handling(self):
        """Test error handling for invalid inputs."""
        # Empty list
        with self.assertRaises(ValueError):
            summarize_figures([])
        
        # Non-numeric data
        with self.assertRaises(ValueError):
            summarize_figures([1, 2, 'a', 4, 5])
    
    def test_mode_handling(self):
        """Test mode calculation with multiple modes."""
        # Data with a clear mode
        mode_data = [1, 2, 2, 3, 4]
        mode_result = summarize_figures(mode_data)
        self.assertEqual(mode_result['statistics']['mode'], 2)
    
    def test_large_dataset(self):
        """Test with a larger dataset."""
        # Generate a large random dataset
        np.random.seed(42)  # For reproducibility
        large_data = list(np.random.normal(50, 10, 1000))
        
        # Should not raise any exceptions
        result = summarize_figures(large_data)
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    unittest.main()