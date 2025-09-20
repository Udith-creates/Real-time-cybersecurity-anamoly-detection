import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Cybersecurity Anomaly Dashboard")
st.title("Real-Time Cyber Anomaly Detection")

placeholder = st.empty()

while True:
    try:
        df = pd.read_csv("anomalies.csv")
        with placeholder.container():
            st.subheader("Latest Anomalies")
            st.dataframe(df.tail(10), height=300)
            for _, row in df.tail(5).iterrows():
                st.warning(row['alert'])
    except Exception:
        st.info("Waiting for new anomaly data...")
    time.sleep(2)
