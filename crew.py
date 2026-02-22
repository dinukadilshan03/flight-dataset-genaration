import pandas as pd
import random
from datetime import datetime
from faker import Faker

fake = Faker()

# Load airports to reference base_airport_id
airports = pd.read_csv("data/Flight_Operations/airports.csv")

roles = (
    ["Captain"] * 20 +
    ["First Officer"] * 20 +
    ["Cabin Crew"] * 40
)
random.shuffle(roles)

crew_rows = []

for i in range(1, 81):  # 80 crew
    crew_rows.append({
        "crew_id": f"C{i:03}",
        "name": fake.name(),
        "role": roles[i-1],
        "hire_date": datetime(
            random.randint(2010, 2022),
            random.randint(1,12),
            random.randint(1,28)
        ),
        "base_airport_id": random.choice(airports["airport_id"].tolist())
    })

crew_df = pd.DataFrame(crew_rows)

crew_df.to_csv("data/Flight_Operations/crew.csv", index=False)

print("Crew generated:", len(crew_df))