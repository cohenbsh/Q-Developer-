# Sensor Prediction System

A robust system for predicting sensor trends and alerting when values are expected to exceed tolerance thresholds.

## Features

- Time series forecasting using Exponential Smoothing
- Confidence scoring for predictions
- Automatic alerting when predictions indicate out-of-tolerance conditions
- Trend origin analysis to identify potential causes
- Time-to-threshold calculations
- Email alerting system
- Comprehensive logging

## Requirements

- Python 3.6+
- Required packages:
  - numpy
  - pandas
  - statsmodels
  - scikit-learn

## Installation

```bash
pip install numpy pandas statsmodels scikit-learn
```

## Usage

### Basic Usage

```python
from sensor_prediction import predict_sensor_trend

# Historical sensor data
sensor_data = [5.0, 5.1, 5.2, 5.0, 5.1, 5.2, 5.0, 5.1, 5.2, 5.0]

# Run prediction
result = predict_sensor_trend(
    sensor_data=sensor_data,
    min_tolerance_threshold=4.0,
    max_tolerance_threshold=6.0,
    prediction_window=3,
    alert_threshold=2,
    machine_id="MACHINE001"
)

# Access results
print(f"Predicted values: {result['predicted_values']}")
print(f"Alert triggered: {result['alert_triggered']}")
print(f"Confidence score: {result['confidence_score']}%")
```

### Advanced Usage

```python
from datetime import datetime, timedelta
from sensor_prediction import predict_sensor_trend

# Historical sensor data
sensor_data = [5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6, 6.8]

# Related sensors data
related_sensors = {
    "temperature": [20.1, 20.3, 20.5, 20.7, 20.9, 21.1, 21.3, 21.5, 21.7, 21.9],
    "pressure": [101.1, 101.2, 101.0, 101.3, 101.1, 101.2, 101.0, 101.3, 101.1, 101.2]
}

# Maintenance history
maintenance_history = [
    {"date": datetime.now() - timedelta(days=15), "type": "calibration", "technician": "John Doe"},
    {"date": datetime.now() - timedelta(days=90), "type": "replacement", "technician": "Jane Smith"}
]

# Run prediction with additional context
result = predict_sensor_trend(
    sensor_data=sensor_data,
    min_tolerance_threshold=4.0,
    max_tolerance_threshold=7.0,
    prediction_window=3,
    alert_threshold=2,
    qa_manager_email="qa_manager@company.com",
    machine_id="MACHINE002",
    related_sensors=related_sensors,
    maintenance_history=maintenance_history
)
```

## Function Reference

### predict_sensor_trend

```python
def predict_sensor_trend(
    sensor_data,
    min_tolerance_threshold,
    max_tolerance_threshold,
    prediction_window=3,
    alert_threshold=2,
    qa_manager_email="qa_manager@company.com",
    machine_id="UNKNOWN",
    related_sensors=None,
    maintenance_history=None
)
```

**Parameters:**

- `sensor_data` (list): Historical sensor readings
- `min_tolerance_threshold` (float): Minimum acceptable value
- `max_tolerance_threshold` (float): Maximum acceptable value
- `prediction_window` (int): Number of future points to predict
- `alert_threshold` (int): Number of consecutive out-of-tolerance predictions to trigger alert
- `qa_manager_email` (str): Email address for alerts
- `machine_id` (str): ID of the machine with the sensor
- `related_sensors` (dict): Data from related sensors
- `maintenance_history` (list): Maintenance history records

**Returns:**

A dictionary containing:
- `predicted_values`: List of predicted future values
- `alert_triggered`: Boolean indicating if an alert was triggered
- `confidence_score`: Confidence score of the prediction (0-100)
- `time_to_threshold`: Information about when values may cross thresholds
- `trend_origin`: Analysis of potential causes of the trend
- `alert_sent`: Boolean indicating if an alert email was sent
- `log_file`: Path to the log file
- `machine_id`: ID of the machine
- `timestamp`: ISO format timestamp of the prediction

## Examples

See `example_sensor_prediction.py` for complete usage examples.

## Testing

Run the test suite:

```bash
python -m unittest test_sensor_prediction.py
```

## Logging

Prediction results are automatically logged to the `sensor_logs` directory in JSON format.

## Email Alerts

The system is configured to send email alerts when sensor values are predicted to exceed tolerance thresholds. By default, it will print alert information to the console. To enable actual email sending, modify the `send_alert_email` function in `sensor_prediction.py`.