import pandas as pd
import random
from datetime import datetime, timedelta

aircraft = pd.read_csv("data/Flight_Operations/aircraft.csv")
engineers = pd.read_csv("data/Maintenance/engineers.csv")

START_DATE = datetime(2023,1,1)
END_DATE = datetime(2024,12,31)

maintenance_rows = []
maintenance_counter = 1

for _, plane in aircraft.iterrows():
    
    current_date = START_DATE + timedelta(days=random.randint(0,30))
    
    while current_date <= END_DATE:
        
        engineer_id = random.choice(engineers["engineer_id"].tolist())
        
        r = random.random()
        
        if r < 0.60:
            maintenance_type = "Routine"
            cost = random.randint(5000,15000)
            downtime = random.randint(6,12)
        elif r < 0.90:
            maintenance_type = "Engine Check"
            cost = random.randint(20000,50000)
            downtime = random.randint(24,72)
        else:
            maintenance_type = "Heavy Maintenance"
            cost = random.randint(80000,150000)
            downtime = random.randint(100,300)
        
        maintenance_rows.append({
            "maintenance_id": f"M{maintenance_counter:06}",
            "aircraft_id": plane["aircraft_id"],
            "engineer_id": engineer_id,
            "maintenance_type": maintenance_type,
            "maintenance_date": current_date,
            "cost": cost,
            "downtime_hours": downtime
        })
        
        maintenance_counter += 1
        
        # Next maintenance 90–120 days later
        current_date += timedelta(days=random.randint(90,120))

maintenance_df = pd.DataFrame(maintenance_rows)

maintenance_df.to_csv("data/Maintenance/maintenance_records.csv", index=False)

print("Maintenance records generated:", len(maintenance_df))