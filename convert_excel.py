import pandas as pd

# Load CSV files
passengers = pd.read_csv("data/Ticketing/passengers.csv")
tickets = pd.read_csv("data/Ticketing/tickets.csv")
payments = pd.read_csv("data/Ticketing/payments.csv")

# Save as Excel
passengers.to_excel("data/Ticketing/passengers.xlsx", index=False)
tickets.to_excel("data/Ticketing/tickets.xlsx", index=False)
payments.to_excel("data/Ticketing/payments.xlsx", index=False)

print("Ticketing system converted to Excel.")