import pathway as pw
from llm_explain import explain_anomaly
import pandas as pd

print("Starting anomaly detection pipeline...")

# Test with just login anomalies first
def is_login_anomaly(log):
    print(f"Checking log: {log}")
    result = (log['location'] not in ['Delhi', 'Mumbai']) and (log['action'] in ['login', 'file_access'])
    print(f"Is anomaly: {result}")
    return result

try:
    print("Loading login schema...")
    login_schema = pw.schema_from_csv("log.csv")
    print("Schema loaded successfully")
    
    print("Reading logs...")
    logs = pw.io.csv.read("log.csv", schema=login_schema, mode="streaming")
    print("Logs loaded successfully")
    
    print("Filtering anomalies...")
    login_anomalies = logs.filter(is_login_anomaly)
    print("Anomalies filtered")
    
    print("Adding AI explanations...")
    login_anomalies = login_anomalies.with_columns(alert=pw.apply(explain_anomaly, login_anomalies))
    print("AI explanations added")
    
    print("Writing to CSV...")
    login_anomalies.to_csv("test_anomalies.csv", mode="overwrite")
    print("CSV output configured")
    
    print("Running pipeline...")
    pw.run()
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
