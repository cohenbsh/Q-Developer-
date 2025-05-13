"""
Example usage of the statistical_functions module.

This script demonstrates how to use the summarize_figures function
with different types of data and how to access the results.
"""

import numpy as np
import random
from statistical_functions import summarize_figures


def print_section(title):
    """Print a section title with decorative formatting."""
    print("\n" + "=" * 50)
    print(f" {title} ".center(50, "="))
    print("=" * 50 + "\n")


def print_result(data, result):
    """Print the results in a formatted way."""
    print(f"Data: {data}")
    print(f"\nSummary: {result['summary']}")
    
    print("\nStatistical Measures:")
    stats = result['statistics']
    print(f"  Mean: {stats['mean']}")
    print(f"  Median: {stats['median']}")
    print(f"  Mode: {stats['mode']}")
    print(f"  Range: {stats['range']} (Min: {stats['min']}, Max: {stats['max']})")
    print(f"  Standard Deviation: {stats['std_dev']}")
    print(f"  Quartiles: Q1={stats['quartiles']['Q1']}, Q2={stats['quartiles']['Q2']}, Q3={stats['quartiles']['Q3']}")
    
    print("\nOrder Analysis:")
    order = result['order_analysis']
    print(f"  Ascending: {order['is_ascending']}")
    print(f"  Descending: {order['is_descending']}")
    print(f"  Consistent Step: {order['consistent_step']}")
    if order['consistent_step']:
        print(f"  Step Size: {order['step_size']}")
    if order['pattern']:
        print(f"  Pattern: {order['pattern']}")


def main():
    """Run examples with different types of data."""
    # Example 1: Arithmetic sequence
    print_section("Example 1: Arithmetic Sequence")
    data1 = [5, 10, 15, 20, 25, 30]
    result1 = summarize_figures(data1)
    print_result(data1, result1)
    
    # Example 2: Geometric sequence
    print_section("Example 2: Geometric Sequence")
    data2 = [3, 6, 12, 24, 48, 96]
    result2 = summarize_figures(data2)
    print_result(data2, result2)
    
    # Example 3: Descending sequence
    print_section("Example 3: Descending Sequence")
    data3 = [100, 90, 80, 70, 60, 50]
    result3 = summarize_figures(data3)
    print_result(data3, result3)
    
    # Example 4: Random data
    print_section("Example 4: Random Data")
    random.seed(42)  # For reproducibility
    data4 = [random.randint(1, 100) for _ in range(10)]
    result4 = summarize_figures(data4)
    print_result(data4, result4)
    
    # Example 5: Normal distribution
    print_section("Example 5: Normal Distribution")
    np.random.seed(42)  # For reproducibility
    data5 = list(np.random.normal(50, 10, 15).round(2))
    result5 = summarize_figures(data5)
    print_result(data5, result5)
    
    # Example 6: Data with repeated values (multiple modes)
    print_section("Example 6: Data with Repeated Values")
    data6 = [5, 2, 7, 2, 9, 5, 2, 8]
    result6 = summarize_figures(data6)
    print_result(data6, result6)


if __name__ == "__main__":
    main()