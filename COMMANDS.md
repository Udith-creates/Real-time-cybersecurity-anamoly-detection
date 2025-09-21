# Real-time Cybersecurity Anomaly Detection - Command Reference

## 🚀 Quick Start (Automated)
```bash
cd /home/imdad/Desktop/Real-time-cybersecurity-anamoly-detection
./start_system.sh
```

## 📋 Manual Startup (5 Terminals Required)

### Terminal 1: Login Data Simulator
```bash
cd /home/imdad/Desktop/Real-time-cybersecurity-anamoly-detection
source venv/bin/activate
python simulate_logs.py
```

### Terminal 2: Network Traffic Simulator
```bash
cd /home/imdad/Desktop/Real-time-cybersecurity-anamoly-detection
source venv/bin/activate
python simulate_network_traffic.py
```

### Terminal 3: File Transfer Simulator
```bash
cd /home/imdad/Desktop/Real-time-cybersecurity-anamoly-detection
source venv/bin/activate
python simulate_file_transfers.py
```

### Terminal 4: Anomaly Detection Pipeline
```bash
cd /home/imdad/Desktop/Real-time-cybersecurity-anamoly-detection
source venv/bin/activate
python pathway_pipeline.py
```

### Terminal 5: Dashboard
```bash
cd /home/imdad/Desktop/Real-time-cybersecurity-anamoly-detection
source venv/bin/activate
streamlit run app.py
```

## 🔍 Testing & Monitoring Commands

### Check if data is being generated:
```bash
cd /home/imdad/Desktop/Real-time-cybersecurity-anamoly-detection
tail -5 log.csv
tail -5 network_traffic.csv
tail -5 file_transfers.csv
```

### Check anomaly detection output:
```bash
cd /home/imdad/Desktop/Real-time-cybersecurity-anamoly-detection
ls -la login_anomalies.csv
tail -10 login_anomalies.csv
```

### Test API key:
```bash
cd /home/imdad/Desktop/Real-time-cybersecurity-anamoly-detection
source venv/bin/activate
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('API Key:', 'Loaded' if os.getenv('GOOGLE_API_KEY') else 'Missing')"
```

### Test AI explanation:
```bash
cd /home/imdad/Desktop/Real-time-cybersecurity-anamoly-detection
source venv/bin/activate
python llm_explain.py
```

## 🌐 Access Points
- **Local Dashboard**: http://localhost:8501
- **Network Dashboard**: http://192.168.0.111:8501
- **Anomaly Output**: login_anomalies.csv

## 🎯 Expected Detections
- **Login Anomalies**: Russia, London, New York logins
- **Network Anomalies**: Traffic spikes >1000 requests
- **File Anomalies**: Transfers >1000MB

## 🛠️ Troubleshooting

### If virtual environment doesn't activate:
```bash
cd /home/imdad/Desktop/Real-time-cybersecurity-anamoly-detection
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### If pipeline fails:
```bash
# Check Pathway version
pip show pathway

# Restart with clean slate
rm -f login_anomalies.csv
python pathway_pipeline.py
```

### If no anomalies detected:
```bash
# Check if data contains suspicious entries
grep -E "Russia|London|New York" log.csv | head -5
grep "5000\|10000" network_traffic.csv | head -5
grep "2000\|2100" file_transfers.csv | head -5
```

## 📦 Dependencies
- pathway
- google-generativeai
- python-dotenv
- streamlit
- pandas

## 🔐 Environment Variables Required
- GOOGLE_API_KEY=AIzaSyC91Gr-K5JXW_56yhgbfBdBRFdOT8gnYt8
