import random
from datetime import datetime
import pandas as pd

aircraft_models = [
    ("Boeing 737-800", "Boeing", 189),
    ("Airbus A320", "Airbus", 180),
    ("Boeing 787-9", "Boeing", 290),
    ("Airbus A350", "Airbus", 300),
    ("Embraer E190", "Embraer", 100)
]

aircraft_rows = []

for i in range(1, 20):  # 15 aircraft
    model = random.choice(aircraft_models)

    aircraft_rows.append({
        "aircraft_id": f"AC{i:03}",
        "model": model[0],
        "manufacturer": model[1],
        "capacity": model[2],
        "acquisition_date": datetime(2016, random.randint(1,12), random.randint(1,28)),
        "current_status": "Active"
    })

aircraft_df = pd.DataFrame(aircraft_rows)

aircraft_df.to_csv("data/Flight_Operations/aircraft.csv", index=False)

print("Aircraft generated:", len(aircraft_df))