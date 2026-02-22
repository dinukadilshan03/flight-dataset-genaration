import pandas as pd
import random
from datetime import datetime
from faker import Faker

fake = Faker()

levels = (
    ["Junior"] * 6 +
    ["Senior"] * 6 +
    ["Lead"] * 3
)

random.shuffle(levels)

engineer_rows = []

for i in range(1, 16):  # 15 engineers
    engineer_rows.append({
        "engineer_id": f"E{i:03}",
        "name": fake.name(),
        "certification_level": levels[i-1],
        "hire_date": datetime(
            random.randint(2012, 2023),
            random.randint(1,12),
            random.randint(1,28)
        )
    })

engineers_df = pd.DataFrame(engineer_rows)

engineers_df.to_csv("data/Maintenance/engineers.csv", index=False)

print("Engineers generated:", len(engineers_df))