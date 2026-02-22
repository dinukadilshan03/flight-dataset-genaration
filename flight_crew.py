import pandas as pd
import random

# Load data
flights = pd.read_csv("data/Flight_Operations/flights.csv")
crew = pd.read_csv("data/Flight_Operations/crew.csv")

flight_crew_rows = []

# Separate crew by role
captains = crew[crew["role"] == "Captain"]["crew_id"].tolist()
first_officers = crew[crew["role"] == "First Officer"]["crew_id"].tolist()
cabin_crew = crew[crew["role"] == "Cabin Crew"]["crew_id"].tolist()

for _, flight in flights.iterrows():
    
    # Select crew
    captain = random.choice(captains)
    first_officer = random.choice(first_officers)
    cabin_team = random.sample(cabin_crew, 3)
    
    # Add assignments
    flight_crew_rows.append({
        "flight_id": flight["flight_id"],
        "crew_id": captain,
        "assignment_role": "Captain"
    })
    
    flight_crew_rows.append({
        "flight_id": flight["flight_id"],
        "crew_id": first_officer,
        "assignment_role": "First Officer"
    })
    
    for cc in cabin_team:
        flight_crew_rows.append({
            "flight_id": flight["flight_id"],
            "crew_id": cc,
            "assignment_role": "Cabin Crew"
        })

flight_crew_df = pd.DataFrame(flight_crew_rows)

flight_crew_df.to_csv("data/Flight_Operations/flight_crew.csv", index=False)

print("Flight crew assignments generated:", len(flight_crew_df))