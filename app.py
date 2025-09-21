import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Cybersecurity Anomaly Dashboard")
st.title("Real-Time Cyber Anomaly Detection")

placeholder = st.empty()

while True:
    try:
        df = pd.read_csv("login_anomalies.csv")
        with placeholder.container():
            st.subheader("Latest Login Anomalies")
            st.dataframe(df.tail(10), height=300)
            for _, row in df.tail(5).iterrows():
                st.warning(f"🚨 {row['alert']} - User: {row['username']} at {row['timestamp']}")
    except Exception as e:
        st.info("Waiting for new anomaly data...")
        st.write(f"Error: {e}")
    time.sleep(2)
