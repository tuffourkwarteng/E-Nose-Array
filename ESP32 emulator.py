import requests
import random
import time
from datetime import datetime

# Your Firebase Database URL
FIREBASE_URL = "https://e-nose-array-default-rtdb.europe-west1.firebasedatabase.app/sensor_data.json"

while True:
    # Generate random sensor readings
    data = {
        "timestamp": datetime.now().isoformat(),
        "Ethanol": round(random.uniform(0, 150), 2),  # ppm
        "Methanol": round(random.uniform(0, 100), 2),  # ppm
        "CO2": round(random.uniform(400, 12000), 2),  # ppm
        "Temperature": round(random.uniform(18, 25), 2),  # °C
        "Humidity": round(random.uniform(50, 80), 2),  # %
    }

    # Send data to Firebase
    response = requests.post(FIREBASE_URL, json=data)

    print(f"Sent Data: {data} | Response: {response.text}")

    # Wait before sending next data
    time.sleep(60)  # Sends data every 5 seconds
