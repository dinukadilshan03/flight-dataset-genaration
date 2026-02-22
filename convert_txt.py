import pandas as pd

engineers = pd.read_csv("data/Maintenance/engineers.csv")
maintenance = pd.read_csv("data/Maintenance/maintenance_records.csv")

engineers.to_csv(
    "data/Maintenance/engineers.txt",
    sep="|",
    index=False
)

maintenance.to_csv(
    "data/Maintenance/maintenance_records.txt",
    sep="|",
    index=False
)

print("Maintenance system converted to TXT.")