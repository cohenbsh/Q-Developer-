"""
Statistical Functions Module

This module provides functions for statistical analysis of numerical data.
"""

import numpy as np
from statistics import mode, StatisticsError
from typing import List, Dict, Union, Tuple, Any


def summarize_figures(data: List[Union[int, float]]) -> Dict[str, Any]:
    """
    Calculate key statistical measures and analyze the order of numerical data.
    
    Args:
        data: A list or array of numerical values
        
    Returns:
        A dictionary containing:
        - Statistical measures (mean, median, mode, range, std_dev, quartiles)
        - Order analysis results (is_ascending, is_descending, pattern, step_size)
        - A brief text summary of the findings
        
    Raises:
        ValueError: If the input is empty or contains non-numerical values
        
    Example:
        >>> data = [1, 2, 3, 4, 5]
        >>> result = summarize_figures(data)
        >>> print(result['summary'])
        'The data is an ascending sequence with 5 values ranging from 1 to 5. 
        The mean is 3.0 and the median is 3. The data has a consistent step size of 1.0.'
    """
    # Input validation
    if not data:
        raise ValueError("Input data cannot be empty")
    
    try:
        # Convert to numpy array for calculations
        np_data = np.array(data, dtype=float)
    except (ValueError, TypeError):
        raise ValueError("Input data must contain only numerical values")
    
    # Calculate statistical measures
    stats = {}
    
    # Basic statistics
    stats['mean'] = float(np.mean(np_data))
    stats['median'] = float(np.median(np_data))
    
    # Mode calculation with error handling
    try:
        stats['mode'] = mode(np_data)
    except StatisticsError:
        stats['mode'] = "No unique mode found"
    
    stats['range'] = float(np.max(np_data) - np.min(np_data))
    stats['min'] = float(np.min(np_data))
    stats['max'] = float(np.max(np_data))
    stats['std_dev'] = float(np.std(np_data))
    
    # Quartiles
    stats['quartiles'] = {
        'Q1': float(np.percentile(np_data, 25)),
        'Q2': float(np.percentile(np_data, 50)),  # Same as median
        'Q3': float(np.percentile(np_data, 75))
    }
    
    # Order analysis
    order_analysis = analyze_order(np_data)
    
    # Combine results
    result = {
        'statistics': stats,
        'order_analysis': order_analysis,
        'summary': generate_summary(stats, order_analysis, len(np_data))
    }
    
    return result


def analyze_order(data: np.ndarray) -> Dict[str, Any]:
    """
    Analyze the order and pattern of the data.
    
    Args:
        data: NumPy array of numerical values
        
    Returns:
        Dictionary containing order analysis results
    """
    n = len(data)
    
    # Check if data is sorted
    is_ascending = all(data[i] <= data[i+1] for i in range(n-1))
    is_descending = all(data[i] >= data[i+1] for i in range(n-1))
    
    # Calculate differences between consecutive elements
    if n > 1:
        diffs = [data[i+1] - data[i] for i in range(n-1)]
        
        # Check if step size is consistent
        consistent_step = all(abs(diffs[0] - diff) < 1e-10 for diff in diffs)
        step_size = diffs[0] if consistent_step else None
    else:
        consistent_step = False
        step_size = None
    
    # Detect patterns (simple patterns only)
    pattern = None
    if n > 2:
        # Check for arithmetic sequence
        if consistent_step:
            pattern = "arithmetic sequence"
        
        # Check for geometric sequence
        if all(data[i] != 0 for i in range(n)):
            ratios = [data[i+1] / data[i] for i in range(n-1) if data[i] != 0]
            if all(abs(ratios[0] - ratio) < 1e-10 for ratio in ratios):
                pattern = "geometric sequence"
    
    return {
        'is_ascending': is_ascending,
        'is_descending': is_descending,
        'is_ordered': is_ascending or is_descending,
        'consistent_step': consistent_step,
        'step_size': step_size,
        'pattern': pattern
    }


def generate_summary(stats: Dict[str, Any], order_analysis: Dict[str, Any], n: int) -> str:
    """
    Generate a text summary of the statistical analysis.
    
    Args:
        stats: Dictionary of statistical measures
        order_analysis: Dictionary of order analysis results
        n: Number of data points
        
    Returns:
        A text summary of the findings
    """
    summary_parts = []
    
    # Data size and range
    summary_parts.append(f"The data contains {n} values ranging from {stats['min']} to {stats['max']}.")
    
    # Order description
    if order_analysis['is_ascending']:
        order_desc = "ascending"
    elif order_analysis['is_descending']:
        order_desc = "descending"
    else:
        order_desc = "neither ascending nor descending"
    
    summary_parts.append(f"The sequence is {order_desc}.")
    
    # Pattern description
    if order_analysis['pattern']:
        summary_parts.append(f"The data follows a {order_analysis['pattern']}.")
    
    if order_analysis['consistent_step']:
        summary_parts.append(f"The data has a consistent step size of {order_analysis['step_size']}.")
    
    # Statistical measures
    summary_parts.append(f"The mean is {stats['mean']:.2f} and the median is {stats['quartiles']['Q2']:.2f}.")
    
    if isinstance(stats['mode'], (int, float)):
        summary_parts.append(f"The mode is {stats['mode']}.")
    else:
        summary_parts.append(f"{stats['mode']}.")
    
    summary_parts.append(f"The standard deviation is {stats['std_dev']:.2f}.")
    
    return " ".join(summary_parts)


# Example usage
if __name__ == "__main__":
    # Example 1: Ascending sequence with consistent step
    data1 = [1, 3, 5, 7, 9]
    result1 = summarize_figures(data1)
    print("Example 1:")
    print(f"Data: {data1}")
    print(f"Summary: {result1['summary']}")
    print(f"Statistics: {result1['statistics']}")
    print(f"Order Analysis: {result1['order_analysis']}")
    print()
    
    # Example 2: Random data
    data2 = [42, 15, 7, 23, 56, 15, 8, 19]
    result2 = summarize_figures(data2)
    print("Example 2:")
    print(f"Data: {data2}")
    print(f"Summary: {result2['summary']}")
    print()
    
    # Example 3: Geometric sequence
    data3 = [2, 4, 8, 16, 32, 64]
    result3 = summarize_figures(data3)
    print("Example 3:")
    print(f"Data: {data3}")
    print(f"Summary: {result3['summary']}")