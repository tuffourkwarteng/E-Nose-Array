import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
import pandas as pd
import json

# Load Firebase credentials from Streamlit Secrets
firebase_config = json.loads(st.secrets["FIREBASE_CREDENTIALS"])

# Initialize Firebase
cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred, {"databaseURL": "https://e-nose-array-default-rtdb.europe-west1.firebasedatabase.app/"})

# Fetch data from Firebase
def get_firebase_data():
    ref = db.reference("/sensor_data")
    data = ref.get()
    if data:
        df = pd.DataFrame.from_dict(data, orient="index")
        df = df.sort_values("timestamp", ascending=False)
        return df
    else:
        return pd.DataFrame()

# Streamlit Dashboard
st.title("📊 E-Nose Sensor Data Dashboard")
st.write("🔹 **Live sensor data from Firebase**")

df = get_firebase_data()

if not df.empty:
    st.dataframe(df)
else:
    st.warning("No sensor data available yet. Please wait for updates.")

st.button("🔄 Refresh Data", on_click=lambda: st.experimental_rerun())
