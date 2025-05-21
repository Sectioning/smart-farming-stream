import pandas as pd
import random

def generate_data(rows=100):
    data = []
    for _ in range(rows):
        temp = random.uniform(20, 40)
        humidity = random.uniform(30, 90)
        soil_moisture = random.uniform(10, 70)
        rainfall = random.uniform(0, 10)
        irrigation_needed = 1 if soil_moisture < 35 and rainfall < 2 else 0
        data.append([temp, humidity, soil_moisture, rainfall, irrigation_needed])

    df = pd.DataFrame(data, columns=["Temperature", "Humidity", "Soil_Moisture", "Rainfall", "Irrigation_Needed"])
    df.to_csv("simulated_data.csv", index=False)

generate_data()
