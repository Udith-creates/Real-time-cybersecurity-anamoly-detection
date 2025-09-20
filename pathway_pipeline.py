
import pathway as pw
from llm_explain import explain_anomaly

# --- Logins & File Access ---
def is_login_anomaly(log):
    return (log['location'] not in ['Delhi', 'Mumbai']) and (log['action'] in ['login', 'file_access'])

login_schema = pw.schema_from_csv("log.csv")
logs = pw.io.csv.read("log.csv", schema=login_schema, mode="streaming")
login_anomalies = logs.filter(is_login_anomaly)
login_anomalies = login_anomalies.with_columns(alert=pw.apply(explain_anomaly, login_anomalies))

# --- Network Traffic ---
def is_network_anomaly(row):
    return int(row['requests']) > 1000

network_schema = pw.schema_from_csv("network_traffic.csv")
network_logs = pw.io.csv.read("network_traffic.csv", schema=network_schema, mode="streaming")
network_anomalies = network_logs.filter(is_network_anomaly)
def network_explain(row):
    return f"Traffic {row['requests']}× higher than baseline — potential attack."
network_anomalies = network_anomalies.with_columns(alert=pw.apply(network_explain, network_anomalies))

# --- File Transfers ---
def is_file_anomaly(row):
    return int(row['volume_mb']) > 1000

file_schema = pw.schema_from_csv("file_transfers.csv")
file_logs = pw.io.csv.read("file_transfers.csv", schema=file_schema, mode="streaming")
file_anomalies = file_logs.filter(is_file_anomaly)
def file_explain(row):
    return f"File transfer volume {row['volume_mb']}MB — suspicious data exfiltration attempt."
file_anomalies = file_anomalies.with_columns(alert=pw.apply(file_explain, file_anomalies))

# --- Combine all anomalies ---
all_anomalies = login_anomalies.select(*login_anomalies.columns).concat(network_anomalies.select(*network_anomalies.columns)).concat(file_anomalies.select(*file_anomalies.columns))
all_anomalies.to_csv("anomalies.csv", mode="overwrite")

pw.run()
