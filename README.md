# 🛡️ Real-Time Cybersecurity Anomaly Detection

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Pathway](https://img.shields.io/badge/Pathway-Streaming-green.svg)](https://pathway.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 🚀 **Real-time AI-powered cybersecurity monitoring system** that detects anomalies instantly and provides intelligent explanations using RAG (Retrieval-Augmented Generation).

## 🎯 Overview

This project implements a real-time cybersecurity anomaly detection system that:
- 📊 **Ingests live security data streams** (login attempts, network traffic, file transfers)
- 🔍 **Detects suspicious patterns** using intelligent rules
- 🤖 **Explains anomalies** with AI-generated insights using RAG
- 📈 **Displays real-time alerts** on an interactive dashboard

## ✨ Features

### 🔐 Multi-Type Anomaly Detection
- **Suspicious Logins**: Detects logins from unusual locations
- **Network Traffic Spikes**: Identifies potential DDoS attacks
- **Data Exfiltration**: Monitors large file transfers

### 🧠 AI-Powered Explanations
- **RAG Integration**: Retrieves relevant context from knowledge base
- **Natural Language**: Human-friendly explanations for each alert
- **Real-time Processing**: Instant AI responses as anomalies occur

### 📊 Live Dashboard
- **Real-time Updates**: Live streaming of detected anomalies
- **Interactive Interface**: Clean, intuitive Streamlit dashboard
- **Alert History**: Track and review past incidents

## 🏗️ Architecture

```
📁 Data Sources → 🔄 Pathway Pipeline → 🤖 AI Explanation → 📊 Dashboard
     ↓                    ↓                    ↓              ↓
  CSV Files         Anomaly Detection      RAG + LLM      Streamlit UI
```

### Core Components:
1. **Data Simulators**: Generate realistic cybersecurity logs
2. **Pathway Pipeline**: Stream processing and anomaly detection
3. **RAG System**: Knowledge retrieval + AI explanation
4. **Dashboard**: Real-time visualization

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Udith-creates/Real-time-cybersecurity-anamoly-detection.git
   cd Real-time-cybersecurity-anamoly-detection
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### 🎮 Running the System

1. **Start Data Simulators** (in separate terminals):
   ```bash
   python simulate_logs.py          # Login/access logs
   python simulate_network_traffic.py  # Network traffic
   python simulate_file_transfers.py   # File transfer data
   ```

2. **Run Pathway Pipeline**:
   ```bash
   python pathway_pipeline.py
   ```

3. **Launch Dashboard**:
   ```bash
   streamlit run app.py
   ```

4. **Open Browser**: Navigate to `http://localhost:8501`

## 📁 Project Structure

```
📦 Real-time-cybersecurity-anamoly-detection/
├── 🔧 pathway_pipeline.py      # Main streaming pipeline
├── 🤖 llm_explain.py          # AI explanation system
├── 📊 app.py                  # Streamlit dashboard
├── 🎲 simulate_logs.py        # Login data simulator
├── 🌐 simulate_network_traffic.py  # Network data simulator
├── 📁 simulate_file_transfers.py   # File transfer simulator
├── 📚 knowledge_base.csv      # RAG knowledge source
├── 📋 requirements.txt        # Dependencies
├── ⚙️ .env                   # Environment variables
└── 📖 README.md              # This file
```

## 🔍 How It Works

### 1. Data Ingestion
```python
# Pathway streams data from CSV files
logs = pw.io.csv.read("log.csv", schema=schema, mode="streaming")
```

### 2. Anomaly Detection
```python
def is_login_anomaly(log):
    return (log['location'] not in ['Delhi', 'Mumbai']) and \
           (log['action'] in ['login', 'file_access'])
```

### 3. RAG-Enhanced Explanations
```python
def explain_anomaly(log):
    rag_explanation = retrieve_explanation(log)  # Retrieve context
    llm_response = generate_explanation(log, rag_explanation)  # AI generation
    return combined_explanation
```

## 🎯 Detected Anomaly Types

| 🚨 Type | 📝 Description | 🔔 Example Alert |
|---------|---------------|------------------|
| 🔐 **Login** | Unusual location access | "Login from Russia detected - outside normal hours" |
| 🌐 **Network** | Traffic spikes | "Traffic 100× higher than baseline - potential DDoS" |
| 📁 **File Transfer** | Large data movement | "2GB transfer detected - possible data exfiltration" |

## 🤖 AI Integration

This system uses **RAG (Retrieval-Augmented Generation)** to provide context-aware explanations:

1. **Retrieval**: Searches knowledge base for relevant patterns
2. **Augmentation**: Combines retrieved context with real-time data
3. **Generation**: Creates human-friendly explanations using AI

## 🛠️ Customization

### Adding New Anomaly Types
1. Create detection function in `pathway_pipeline.py`
2. Add explanation logic in `llm_explain.py`
3. Update knowledge base in `knowledge_base.csv`

### Configuring AI Model
- **Local**: Use Transformers (default)
- **API**: Switch to OpenAI/Anthropic for better quality

## 📊 Demo Features

- ✅ **Real-time streaming** with Pathway
- ✅ **Multi-source data ingestion**
- ✅ **Intelligent anomaly detection**
- ✅ **RAG-powered explanations**
- ✅ **Live dashboard updates**
- ✅ **Scalable architecture**

## 🏆 Hackathon Requirements Met

- ✅ **Pathway-Powered Streaming ETL**
- ✅ **Live Indexing (No Rebuilds)**
- ✅ **Real-time Retrieval/Generation**
- ✅ **Interactive Dashboard**
- ✅ **RAG Integration**



## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Pathway](https://pathway.com) for real-time streaming capabilities
- [Streamlit](https://streamlit.io) for the dashboard framework
- [Hugging Face](https://huggingface.co) for AI model integration

---

<div align="center">



[🌟 Star this repo](https://github.com/Udith-creates/Real-time-cybersecurity-anamoly-detection) | [🐛 Report Bug](https://github.com/Udith-creates/Real-time-cybersecurity-anamoly-detection/issues) | [💡 Request Feature](https://github.com/Udith-creates/Real-time-cybersecurity-anamoly-detection/issues)

</div>