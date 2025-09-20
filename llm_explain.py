

from transformers import pipeline
import csv

# Use open-access GPT-2 model
generator = pipeline("text-generation", model="gpt2")

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
              f"Details: {rag_explanation}\n")

    output = generator(prompt, max_length=50, do_sample=True, temperature=0.7)
    return rag_explanation + "\n" + output[0]["generated_text"]
