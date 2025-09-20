
import os
import csv
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google AI with API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

def retrieve_explanation(log):
    kb_file = "knowledge_base.csv"
    explanations = []
    with open(kb_file, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["type"] == "login" and log.get("location") == "Russia":
                explanations.append(row["explanation"])
            elif row["type"] == "network" and int(log.get("requests", 0)) > 1000:
                explanations.append(row["explanation"])
            elif row["type"] == "file_transfer" and int(log.get("volume_mb", 0)) > 1000:
                explanations.append(row["explanation"])
    return " ".join(explanations)

def explain_anomaly(log):
    rag_explanation = retrieve_explanation(log)
    prompt = (f"Explain why this cybersecurity event is suspicious:\n"
              f"User: {log.get('username', '')}\n"
              f"Location: {log.get('location', '')}\n"
              f"Action: {log.get('action', '')}\n"
              f"Timestamp: {log.get('timestamp', '')}\n"
              f"Context: {rag_explanation}\n"
              f"Provide a concise security analysis in 1-2 sentences.")

    try:
        response = model.generate_content(prompt)
        ai_explanation = response.text
        return f"{rag_explanation}\nAI Analysis: {ai_explanation}"
    except Exception as e:
        return f"{rag_explanation}\nAI Analysis: Error generating explanation: {str(e)}"
