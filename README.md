# HealthTracker: An AI-Enabled Body Area Network for Enhanced Health Monitoring

## Overview

**HealthTracker** is an AI-powered health monitoring system that simulates and analyzes patient health data without requiring physical wearable sensors. The system generates realistic health parameters such as heart rate, blood pressure, respiratory rate, oxygen levels, and ECG signals, creating a virtual environment for testing, training, and prediction by healthcare professionals.

---

## Project Architecture

The system consists of five primary layers:

1. **Data Simulation Layer** – Generates simulated physiological parameters  
2. **Data Transmission Layer** – Transfers data from simulation to processing modules  
3. **Data Processing Layer** – Applies machine learning algorithms to identify anomalies  
4. **Notification Layer** – Alerts healthcare providers about detected anomalies  
5. **User Interface Layer** – Provides access to health insights, trends, and alerts  



---

## Key Features

### ✅ Continuous Data Collection
- Simulates heart rate, blood pressure, respiratory rate, oxygen saturation, and ECG signals  
- Generates realistic temporal trends and variations for reliable analysis

### ✅ Anomaly Detection and Predictive Analytics
- **Hybrid CNN**: Analyzes ECG data to identify cardiovascular risks  
- **Isolation Forest**: Detects outliers in vital signs  
- **LSTM**: Predicts future health risks based on historical data

### ✅ Real-Time Alert System
- Notifies healthcare professionals about anomalies in real time  
- Categorizes alerts by severity and affected health parameters  
- Includes simulated patient location data

### ✅ Data Storage and Management
- Scalable storage system for health data  
- Efficient search, backup, and retrieval functionalities

### ✅ User Interface
- **Patient Dashboard**: View health metrics and receive alerts  
- **Provider Dashboard**: Access detailed reports, set thresholds, and monitor patients  
- Role-based access control for data security

### ✅ Report Generation and Visualization
- Graphs of vital signs over time  
- Trend analysis for proactive health management

### ✅ Emergency Response Integration
- Sends automatic alerts to emergency services during critical health events

---

## 📁 Project Structure

```
healthTracker/
├── app.py                  # Main application file
├── audio_play.py           # Audio alert functionality
├── chat.py                 # Chat interface
├── email_sender.py         # Email notification system
├── model_predict.py        # ML model prediction functions
├── smartai_text.pkl        # Text processing model
├── chatbot_model.h5        # Chatbot neural network model
├── tokenizer.pickle        # Tokenization data for chatbot
├── intents.json            # Chatbot intents and responses
├── data/
│   ├── chat_history.csv    # Stored user chat interactions
│   ├── database.csv        # Core health data
│   └── health_data.csv     # Processed physiological metrics
├── models/
│   ├── cnn_model.ipynb     # CNN for ECG analysis
│   ├── LSTM_model.ipynb    # LSTM for trend prediction
│   ├── rnn_model.ipynb     # RNN for sequential data analysis
│   ├── index_to_tag.pickle # Index-to-tag mapping for models
│   └── tag_to_index.pickle # Tag-to-index mapping
```



---

## Technical Requirements

### Functional Requirements
- Continuous physiological data simulation  
- Seamless data transmission  
- AI-based anomaly detection and forecasting  
- Real-time alerts and notifications  
- Efficient data storage and querying  
- Multi-role access via user interface  
- Dynamic report generation  
- Integration with emergency services

### Non-Functional Requirements
- **Reliability**: 99.9% uptime  
- **Scalability**: Handles large volumes of health data  
- **Performance**: Response time under 2 seconds  
- **Security**: Robust privacy and encryption protocols  
- **Usability**: Intuitive and user-friendly interface  
- **Maintainability**: Modular and easy to update  
- **Interoperability**: Compatibility with other healthcare systems

---

## Installation and Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-username/healthTracker.git
cd healthTracker
```
2. **Install required dependencies**
```bash
pip install -r requirements.txt
```
3. **Run the application**
```bash
python app.py
```

## Usage

### For Healthcare Providers
- Access real-time and historical health reports
- Monitor simulated patient data
- Receive alerts for abnormalities
- Configure thresholds and response settings

### For Patients
- View personal simulated health records
- Receive alerts and recommendations
- Adjust personal monitoring preferences

## Machine Learning Models
- CNN (Convolutional Neural Network): For analyzing ECG signals and identifying cardiac anomalies
- LSTM (Long Short-Term Memory): For predicting future health risks based on time-series data
- RNN (Recurrent Neural Network): For analyzing sequential physiological data
- Isolation Forest: For detecting anomalies and outliers in health metrics


