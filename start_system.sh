#!/bin/bash

# Real-time Cybersecurity Anomaly Detection System Startup Script
echo "🛡️  Starting Real-time Cybersecurity Anomaly Detection System..."

PROJECT_DIR="/home/imdad/Desktop/Real-time-cybersecurity-anamoly-detection"
cd "$PROJECT_DIR"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please create venv first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

echo "📊 Starting data simulators..."

# Clean up old output files
echo "🧹 Cleaning up old output files..."
rm -f login_anomalies.csv anomalies.csv 2>/dev/null

# Start login simulator in background
gnome-terminal --tab --title="Login Simulator" -- bash -c "
cd '$PROJECT_DIR'
source venv/bin/activate
echo '🔐 Starting Login Data Simulator...'
echo 'Generating login events with anomalies from Russia, London, New York...'
python simulate_logs.py
echo 'Login simulator stopped. Press any key to close.'
read
"

# Start network traffic simulator in background
gnome-terminal --tab --title="Network Simulator" -- bash -c "
cd '$PROJECT_DIR'
source venv/bin/activate
echo '🌐 Starting Network Traffic Simulator...'
echo 'Generating network traffic with spikes (5000-10000 requests)...'
python simulate_network_traffic.py
echo 'Network simulator stopped. Press any key to close.'
read
"

# Start file transfer simulator in background
gnome-terminal --tab --title="File Transfer Simulator" -- bash -c "
cd '$PROJECT_DIR'
source venv/bin/activate
echo '📁 Starting File Transfer Simulator...'
echo 'Generating file transfers with large volumes (2000MB+)...'
python simulate_file_transfers.py
echo 'File transfer simulator stopped. Press any key to close.'
read
"

# Wait a moment for data generation
echo "⏳ Waiting for data generation to start..."
sleep 8

# Start the detection pipeline
gnome-terminal --tab --title="Detection Pipeline" -- bash -c "
cd '$PROJECT_DIR'
source venv/bin/activate
echo '🔍 Starting Anomaly Detection Pipeline...'
echo 'Processing login anomalies from suspicious locations...'
echo 'Output will be saved to: login_anomalies.csv'
python pathway_pipeline.py
echo 'Detection pipeline stopped. Press any key to close.'
read
"

# Wait for pipeline to initialize and process some data
echo "⏳ Waiting for pipeline to initialize..."
sleep 15

# Check if anomalies file was created
if [ -f "login_anomalies.csv" ]; then
    echo "✅ Anomaly detection working! Found $(wc -l < login_anomalies.csv) entries."
else
    echo "⚠️  Anomaly file not found yet. Pipeline may need more time."
fi

# Start the dashboard
gnome-terminal --tab --title="Dashboard" -- bash -c "
cd '$PROJECT_DIR'
source venv/bin/activate
echo '📊 Starting Real-time Dashboard...'
echo 'Dashboard will show login anomalies in real-time'
echo 'Access at: http://localhost:8501'
streamlit run app.py
echo 'Dashboard stopped. Press any key to close.'
read
"

echo "✅ All components started successfully!"
echo ""
echo "� System Overview:"
echo "   📊 Dashboard: http://localhost:8501"
echo "   📊 Network Dashboard: http://$(hostname -I | awk '{print $1}'):8501"
echo "   📁 Anomaly Output: login_anomalies.csv"
echo ""
echo "🔍 Monitoring:"
echo "   • Login anomalies from Russia, London, New York"
echo "   • Network traffic spikes >1000 requests"
echo "   • File transfers >1000MB"
echo ""
echo "� Monitor the terminal tabs for real-time logs"
echo "🔄 Data refreshes every 2-3 seconds"
echo ""
echo "ℹ️  To stop all processes: Close all terminal tabs or use Ctrl+C in each"
