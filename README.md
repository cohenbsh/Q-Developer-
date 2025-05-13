# Statistical Functions Module

This repository contains a Python module for statistical analysis of numerical data.

## Features

The main function `summarize_figures` provides comprehensive statistical analysis of numerical data including:

### Statistical Measures
- Mean
- Median
- Mode
- Range
- Standard deviation
- Quartiles (Q1, Q2, Q3)
- Min and max values

### Order Analysis
- Determines if the sequence is ascending, descending, or neither
- Identifies patterns in the data (arithmetic or geometric sequences)
- Calculates step size between values (if consistent)

### Summary Generation
- Provides a human-readable text summary of the findings

## Installation

No special installation is required. The module depends on:
- NumPy
- Python's built-in statistics module

## Usage

```python
from statistical_functions import summarize_figures

# Example with a simple sequence
data = [1, 3, 5, 7, 9]
result = summarize_figures(data)

# Access the results
print(result['summary'])  # Text summary
print(result['statistics'])  # Dictionary of statistical measures
print(result['order_analysis'])  # Dictionary of order analysis results

# Example with random data
import random
random_data = [random.randint(1, 100) for _ in range(20)]
random_result = summarize_figures(random_data)
print(random_result['summary'])
```

## Function Documentation

### summarize_figures(data)

Calculate key statistical measures and analyze the order of numerical data.

**Parameters:**
- `data`: A list or array of numerical values

**Returns:**
A dictionary containing:
- `statistics`: Statistical measures (mean, median, mode, range, std_dev, quartiles)
- `order_analysis`: Order analysis results (is_ascending, is_descending, pattern, step_size)
- `summary`: A brief text summary of the findings

**Raises:**
- `ValueError`: If the input is empty or contains non-numerical values

## Testing

Run the unit tests to verify the functionality:

```bash
python -m unittest test_statistical_functions.py
```

## Examples

See the examples at the end of the `statistical_functions.py` file for demonstration of different use cases:
1. Ascending sequence with consistent step
2. Random data
3. Geometric sequence