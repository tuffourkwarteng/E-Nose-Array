import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
import pandas as pd

# Load Firebase credentials
cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://e-nose-array-default-rtdb.europe-west1.firebasedatabase.app/"})

# Fetch data from Firebase
def get_firebase_data():
    ref = db.reference("/sensor_data")  # Path to your sensor data
    data = ref.get()
    if data:
        df = pd.DataFrame.from_dict(data, orient="index")  # Convert to DataFrame
        df = df.sort_values("timestamp", ascending=False)  # Sort by latest
        return df
    else:
        return pd.DataFrame()  # Return empty if no data

# Streamlit Dashboard
st.title("📊 E-Nose Sensor Data Dashboard")
st.write("🔹 **Live sensor data from Firebase**")

df = get_firebase_data()  # Load data

if not df.empty:
    st.dataframe(df)  # Display data in table
else:
    st.warning("No sensor data available yet. Please wait for updates.")

st.button("🔄 Refresh Data", on_click=lambda: st.experimental_rerun())  # Refresh button
