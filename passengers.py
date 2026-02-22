import pandas as pd
import random
from datetime import datetime
from faker import Faker

fake = Faker()

NUM_PASSENGERS = 1500

# Create loyalty distribution
loyalty_distribution = (
    ["Silver"] * int(NUM_PASSENGERS * 0.70) +
    ["Gold"] * int(NUM_PASSENGERS * 0.25) +
    ["Platinum"] * int(NUM_PASSENGERS * 0.05)
)

random.shuffle(loyalty_distribution)

passenger_rows = []

for i in range(1, NUM_PASSENGERS + 1):
    passenger_rows.append({
        "passenger_id": f"P{i:05}",
        "name": fake.name(),
        "country": fake.country(),
        "loyalty_tier": loyalty_distribution[i-1],
        "registration_date": datetime(
            random.randint(2018, 2024),
            random.randint(1,12),
            random.randint(1,28)
        )
    })

passengers_df = pd.DataFrame(passenger_rows)

passengers_df.to_csv("data/Ticketing/passengers.csv", index=False)

print("Passengers generated:", len(passengers_df))