import numpy as np
from datetime import datetime, timedelta
from sensor_prediction import predict_sensor_trend

def main():
    print("Sensor Prediction System Example")
    print("================================")
    
    # Example 1: Normal sensor data (within thresholds)
    print("\nExample 1: Normal sensor data")
    print("----------------------------")
    
    # Generate some stable sensor data
    normal_sensor_data = [5.0, 5.1, 5.2, 5.0, 5.1, 5.2, 5.0, 5.1, 5.2, 5.0]
    
    # Run prediction
    result = predict_sensor_trend(
        sensor_data=normal_sensor_data,
        min_tolerance_threshold=4.0,
        max_tolerance_threshold=6.0,
        prediction_window=3,
        alert_threshold=2,
        machine_id="MACHINE001"
    )
    
    # Display results
    print(f"Predicted values: {[round(v, 2) for v in result['predicted_values']]}")
    print(f"Alert triggered: {result['alert_triggered']}")
    print(f"Confidence score: {result['confidence_score']}%")
    print(f"Trend direction: {result['time_to_threshold']['trend_direction']}")
    
    # Example 2: Increasing sensor data (will cross threshold)
    print("\nExample 2: Increasing sensor data")
    print("-------------------------------")
    
    # Generate increasing sensor data
    increasing_sensor_data = [5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6, 6.8]
    
    # Create example related sensors data
    related_sensors = {
        "temperature": [20.1, 20.3, 20.5, 20.7, 20.9, 21.1, 21.3, 21.5, 21.7, 21.9],
        "pressure": [101.1, 101.2, 101.0, 101.3, 101.1, 101.2, 101.0, 101.3, 101.1, 101.2]
    }
    
    # Create example maintenance history
    maintenance_history = [
        {"date": datetime.now() - timedelta(days=15), "type": "calibration", "technician": "John Doe"},
        {"date": datetime.now() - timedelta(days=90), "type": "replacement", "technician": "Jane Smith"}
    ]
    
    # Run prediction
    result = predict_sensor_trend(
        sensor_data=increasing_sensor_data,
        min_tolerance_threshold=4.0,
        max_tolerance_threshold=7.0,
        prediction_window=3,
        alert_threshold=2,
        machine_id="MACHINE002",
        related_sensors=related_sensors,
        maintenance_history=maintenance_history
    )
    
    # Display results
    print(f"Predicted values: {[round(v, 2) for v in result['predicted_values']]}")
    print(f"Alert triggered: {result['alert_triggered']}")
    print(f"Confidence score: {result['confidence_score']}%")
    print(f"Trend direction: {result['time_to_threshold']['trend_direction']}")
    
    if result["time_to_threshold"]["time_to_max_threshold"]:
        print(f"Estimated time to max threshold: {result['time_to_threshold']['time_to_max_threshold']} units")
    
    print("\nPotential causes:")
    for cause in result["trend_origin"]["potential_causes"]:
        print(f"- {cause}")
    
    print("\nRecommended actions:")
    for action in result["trend_origin"]["recommended_actions"]:
        print(f"- {action}")
    
    # Example 3: Decreasing sensor data (will cross threshold)
    print("\nExample 3: Decreasing sensor data")
    print("-------------------------------")
    
    # Generate decreasing sensor data
    decreasing_sensor_data = [6.0, 5.8, 5.6, 5.4, 5.2, 5.0, 4.8, 4.6, 4.4, 4.2]
    
    # Run prediction
    result = predict_sensor_trend(
        sensor_data=decreasing_sensor_data,
        min_tolerance_threshold=4.0,
        max_tolerance_threshold=7.0,
        prediction_window=3,
        alert_threshold=2,
        machine_id="MACHINE003"
    )
    
    # Display results
    print(f"Predicted values: {[round(v, 2) for v in result['predicted_values']]}")
    print(f"Alert triggered: {result['alert_triggered']}")
    print(f"Confidence score: {result['confidence_score']}%")
    print(f"Trend direction: {result['time_to_threshold']['trend_direction']}")
    
    if result["time_to_threshold"]["time_to_min_threshold"]:
        print(f"Estimated time to min threshold: {result['time_to_threshold']['time_to_min_threshold']} units")

if __name__ == "__main__":
    main()