
import pathway as pw

print("Starting Pathway anomaly detection...")

# --- Logins & File Access ---
print("Setting up login anomaly detection...")
login_schema = pw.schema_from_csv("log.csv")
logs = pw.io.csv.read("log.csv", schema=login_schema, mode="streaming")

# Filter for suspicious locations and actions
login_anomalies = logs.filter(
    (pw.this.location != 'Delhi') & 
    (pw.this.location != 'Mumbai') & 
    ((pw.this.action == 'login') | (pw.this.action == 'file_access'))
)

# Add simple alert message
login_anomalies = login_anomalies.with_columns(
    alert=pw.this.location + " " + pw.this.action + " - Suspicious location detected"
)

print("Login detection configured.")

# Output login anomalies using correct API
pw.io.csv.write(login_anomalies, "login_anomalies.csv")

print("Pipeline configured. Starting execution...")
pw.run()
