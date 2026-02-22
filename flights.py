import pandas as pd
import random
from datetime import datetime, timedelta

# Load reference data
airports = pd.read_csv("data/Flight_Operations/airports.csv")
aircraft = pd.read_csv("data/Flight_Operations/aircraft.csv")

START_DATE = datetime(2023,1,1)
END_DATE = datetime(2024,12,31)
FLIGHTS_PER_DAY = 7

flight_rows = []
flight_counter = 1
current_date = START_DATE

while current_date <= END_DATE:
    
    for _ in range(FLIGHTS_PER_DAY):
        
        departure = random.choice(airports["airport_id"].tolist())
        arrival = random.choice(airports["airport_id"].tolist())
        
        while arrival == departure:
            arrival = random.choice(airports["airport_id"].tolist())
        
        aircraft_id = random.choice(aircraft["aircraft_id"].tolist())
        
        departure_time = datetime(
            current_date.year,
            current_date.month,
            current_date.day,
            random.randint(0,23),
            random.randint(0,59)
        )
        
        flight_duration = timedelta(hours=random.randint(2,12))
        arrival_time = departure_time + flight_duration
        
        # Delay logic
        delay_minutes = 0
        if random.random() < 0.20:
            delay_minutes = random.randint(10,60)
        
        actual_departure = departure_time + timedelta(minutes=delay_minutes)
        actual_arrival = arrival_time + timedelta(minutes=delay_minutes)
        
        flight_rows.append({
            "flight_id": f"F{flight_counter:06}",
            "flight_number": f"SKY{random.randint(100,999)}",
            "aircraft_id": aircraft_id,
            "departure_airport_id": departure,
            "arrival_airport_id": arrival,
            "scheduled_departure": departure_time,
            "scheduled_arrival": arrival_time,
            "actual_departure": actual_departure,
            "actual_arrival": actual_arrival,
            "delay_minutes": delay_minutes,
            "flight_status": "Delayed" if delay_minutes > 0 else "On-Time"
        })
        
        flight_counter += 1
    
    current_date += timedelta(days=1)

flights_df = pd.DataFrame(flight_rows)

flights_df.to_csv("data/Flight_Operations/flights.csv", index=False)

print("Flights generated:", len(flights_df))