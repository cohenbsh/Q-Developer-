import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import os
from datetime import datetime

def max_consecutive(bool_list):
    """
    Find the maximum number of consecutive True values in a list.
    
    Args:
        bool_list (list): List of boolean values
        
    Returns:
        int: Maximum number of consecutive True values
    """
    if not bool_list:
        return 0
        
    max_count = 0
    current_count = 0
    
    for value in bool_list:
        if value:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
            
    return max_count

def analyze_trend_origin(data, related_sensors=None, maintenance_history=None):
    """
    Analyze the potential origin of a trend in sensor data.
    
    Args:
        data (pd.Series): Historical sensor data
        related_sensors (dict, optional): Data from related sensors
        maintenance_history (list, optional): Maintenance history records
        
    Returns:
        dict: Analysis of trend origin with potential causes and confidence levels
    """
    result = {
        "potential_causes": [],
        "confidence": 0,
        "recommended_actions": []
    }
    
    # Check for sudden changes in the data
    if len(data) > 5:
        recent_mean = data[-5:].mean()
        overall_mean = data.mean()
        std_dev = data.std()
        
        if abs(recent_mean - overall_mean) > 2 * std_dev:
            result["potential_causes"].append("Sudden change detected")
            result["confidence"] = 70
            result["recommended_actions"].append("Inspect sensor for physical damage")
    
    # Check related sensors if available
    if related_sensors:
        correlated_sensors = []
        for sensor_id, sensor_data in related_sensors.items():
            if len(sensor_data) == len(data):
                correlation = np.corrcoef(data, sensor_data)[0, 1]
                if abs(correlation) > 0.7:
                    correlated_sensors.append(sensor_id)
        
        if correlated_sensors:
            result["potential_causes"].append(f"Correlated with sensors: {', '.join(correlated_sensors)}")
            result["confidence"] = max(result["confidence"], 80)
            result["recommended_actions"].append("Check related systems")
    
    # Check maintenance history if available
    if maintenance_history:
        recent_maintenance = [m for m in maintenance_history 
                             if (datetime.now() - m["date"]).days < 30]
        if recent_maintenance:
            result["potential_causes"].append("Recent maintenance may be related")
            result["confidence"] = max(result["confidence"], 60)
            result["recommended_actions"].append("Review recent maintenance records")
    
    # If no specific cause found
    if not result["potential_causes"]:
        result["potential_causes"].append("Normal operational variation")
        result["confidence"] = 30
        result["recommended_actions"].append("Continue monitoring")
    
    return result

def calculate_time_to_threshold(data, predictions, min_threshold, max_threshold):
    """
    Calculate estimated time until sensor values cross thresholds.
    
    Args:
        data (pd.Series): Historical sensor data
        predictions (list): Predicted future values
        min_threshold (float): Minimum tolerance threshold
        max_threshold (float): Maximum tolerance threshold
        
    Returns:
        dict: Time to threshold information
    """
    # Get the last actual value
    last_value = data.iloc[-1] if len(data) > 0 else None
    
    # Initialize result
    result = {
        "time_to_min_threshold": None,
        "time_to_max_threshold": None,
        "trend_direction": "stable"
    }
    
    # If no predictions or last value, return early
    if not predictions or last_value is None:
        return result
    
    # Calculate average rate of change from predictions
    changes = [predictions[i] - predictions[i-1] for i in range(1, len(predictions))]
    avg_change = sum(changes) / len(changes) if changes else 0
    
    # Determine trend direction
    if avg_change > 0.01:
        result["trend_direction"] = "increasing"
    elif avg_change < -0.01:
        result["trend_direction"] = "decreasing"
    
    # Calculate time to thresholds if trend is not stable
    if result["trend_direction"] != "stable" and avg_change != 0:
        if result["trend_direction"] == "increasing" and last_value < max_threshold:
            time_to_max = (max_threshold - last_value) / abs(avg_change)
            result["time_to_max_threshold"] = round(time_to_max, 1)
        
        if result["trend_direction"] == "decreasing" and last_value > min_threshold:
            time_to_min = (last_value - min_threshold) / abs(avg_change)
            result["time_to_min_threshold"] = round(time_to_min, 1)
    
    return result

def send_alert_email(recipient_email, machine_id, predictions, confidence_score, 
                    time_to_threshold, trend_origin, min_threshold, max_threshold):
    """
    Send an alert email when sensor predictions indicate out-of-tolerance conditions.
    
    Args:
        recipient_email (str): Email address of the recipient
        machine_id (str): ID of the machine with the sensor
        predictions (list): Predicted future values
        confidence_score (float): Confidence score of the prediction
        time_to_threshold (dict): Time to threshold information
        trend_origin (dict): Analysis of trend origin
        min_threshold (float): Minimum tolerance threshold
        max_threshold (float): Maximum tolerance threshold
        
    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = 'sensor-alerts@company.com'
        msg['To'] = recipient_email
        msg['Subject'] = f'ALERT: Sensor Prediction Warning for Machine {machine_id}'
        
        # Build email body
        body = f"""
        <html>
        <body>
            <h2>Sensor Alert: Machine {machine_id}</h2>
            <p><strong>Alert Type:</strong> Predicted Out-of-Tolerance Condition</p>
            <p><strong>Confidence Score:</strong> {confidence_score}%</p>
            <p><strong>Predicted Values:</strong> {', '.join([str(round(p, 2)) for p in predictions])}</p>
            <p><strong>Tolerance Range:</strong> {min_threshold} to {max_threshold}</p>
            
            <h3>Trend Analysis:</h3>
            <p><strong>Direction:</strong> {time_to_threshold['trend_direction']}</p>
            
            <h3>Potential Causes:</h3>
            <ul>
        """
        
        for cause in trend_origin['potential_causes']:
            body += f"<li>{cause}</li>"
        
        body += """
            </ul>
            
            <h3>Recommended Actions:</h3>
            <ul>
        """
        
        for action in trend_origin['recommended_actions']:
            body += f"<li>{action}</li>"
        
        body += """
            </ul>
            
            <p>Please investigate this issue promptly.</p>
        </body>
        </html>
        """
        
        msg.attach(MIMEText(body, 'html'))
        
        # For demonstration purposes, we'll just log that we would send an email
        # In a real implementation, you would use SMTP to send the email
        print(f"[ALERT EMAIL] Would send alert email to {recipient_email} about Machine {machine_id}")
        
        # Uncomment the following code to actually send emails
        """
        with smtplib.SMTP('smtp.company.com', 587) as server:
            server.starttls()
            server.login('sensor-alerts@company.com', 'password')
            server.send_message(msg)
        """
        
        return True
    
    except Exception as e:
        print(f"Error sending alert email: {str(e)}")
        return False

def save_to_log(machine_id, sensor_data, predictions, alert_triggered, confidence_score, trend_origin):
    """
    Save prediction results to a log file.
    
    Args:
        machine_id (str): ID of the machine with the sensor
        sensor_data (list): Historical sensor data
        predictions (list): Predicted future values
        alert_triggered (bool): Whether an alert was triggered
        confidence_score (float): Confidence score of the prediction
        trend_origin (dict): Analysis of trend origin
        
    Returns:
        str: Path to the log file
    """
    try:
        # Create logs directory if it doesn't exist
        log_dir = "sensor_logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # Create log filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(log_dir, f"{machine_id}_{timestamp}.json")
        
        # Prepare log data
        log_data = {
            "machine_id": machine_id,
            "timestamp": datetime.now().isoformat(),
            "sensor_data": [float(x) for x in sensor_data[-10:]],  # Last 10 readings
            "predictions": [float(x) for x in predictions],
            "alert_triggered": alert_triggered,
            "confidence_score": confidence_score,
            "trend_analysis": trend_origin
        }
        
        # Write to file
        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        print(f"Log saved to {log_file}")
        return log_file
    
    except Exception as e:
        print(f"Error saving to log: {str(e)}")
        return None

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
):
    """
    Predicts future sensor values and alerts if trends indicate out-of-tolerance conditions.
    
    Args:
        sensor_data (list): Historical sensor readings
        min_tolerance_threshold (float): Minimum acceptable value
        max_tolerance_threshold (float): Maximum acceptable value
        prediction_window (int): Number of future points to predict
        alert_threshold (int): Number of consecutive out-of-tolerance predictions to trigger alert
        qa_manager_email (str): Email address for alerts
        machine_id (str): ID of the machine with the sensor
        related_sensors (dict): Data from related sensors
        maintenance_history (list): Maintenance history records
        
    Returns:
        dict: Prediction results and analysis
    """
    # Convert data to pandas Series for time series analysis
    data = pd.Series(sensor_data)
    
    # Create and fit time series model
    model = ExponentialSmoothing(
        data, 
        trend='add',
        seasonal=None,
        damped=True
    ).fit()
    
    # Generate predictions
    predictions = model.forecast(prediction_window).tolist()
    
    # Calculate confidence score based on model fit
    rmse = np.sqrt(mean_squared_error(data[1:], model.fittedvalues[:-1]))
    max_error = max(abs(data.max() - data.min()), 1)  # Avoid division by zero
    confidence_score = max(0, min(100, 100 * (1 - rmse / max_error)))
    
    # Check if predictions cross tolerance thresholds
    below_min = [p < min_tolerance_threshold for p in predictions]
    above_max = [p > max_tolerance_threshold for p in predictions]
    
    # Count consecutive out-of-tolerance predictions
    consecutive_below = max_consecutive(below_min)
    consecutive_above = max_consecutive(above_max)
    
    # Determine if alert should be triggered
    alert_triggered = (consecutive_below >= alert_threshold or 
                       consecutive_above >= alert_threshold)
    
    # Analyze trend origin
    trend_origin = analyze_trend_origin(data, related_sensors, maintenance_history)
    
    # Calculate time to threshold
    time_to_threshold = calculate_time_to_threshold(data, predictions, 
                                                   min_tolerance_threshold, 
                                                   max_tolerance_threshold)
    
    # Send alert if needed
    alert_sent = False
    if alert_triggered:
        alert_sent = send_alert_email(
            qa_manager_email,
            machine_id,
            predictions,
            confidence_score,
            time_to_threshold,
            trend_origin,
            min_tolerance_threshold,
            max_tolerance_threshold
        )
    
    # Save results to log file
    log_file = save_to_log(
        machine_id, 
        sensor_data, 
        predictions, 
        alert_triggered,
        confidence_score,
        trend_origin
    )
    
    # Return results
    return {
        "predicted_values": predictions,
        "alert_triggered": alert_triggered,
        "confidence_score": round(confidence_score, 1),
        "time_to_threshold": time_to_threshold,
        "trend_origin": trend_origin,
        "alert_sent": alert_sent,
        "log_file": log_file,
        "machine_id": machine_id,
        "timestamp": datetime.now().isoformat()
    }