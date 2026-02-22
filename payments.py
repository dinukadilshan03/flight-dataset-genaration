import pandas as pd
import random
from datetime import timedelta

tickets = pd.read_csv("data/Ticketing/tickets.csv")

payment_methods = (
    ["Credit Card"] * 50 +
    ["Debit Card"] * 25 +
    ["PayPal"] * 15 +
    ["Bank Transfer"] * 10
)

payment_rows = []
payment_counter = 1

for _, ticket in tickets.iterrows():
    
    method = random.choice(payment_methods)
    
    booking_date = pd.to_datetime(ticket["booking_date"])
    payment_date = booking_date + timedelta(days=random.randint(0,2))
    
    payment_rows.append({
        "payment_id": f"PAY{payment_counter:07}",
        "ticket_id": ticket["ticket_id"],
        "payment_method": method,
        "payment_amount": ticket["ticket_price"],
        "payment_date": payment_date
    })
    
    payment_counter += 1

payments_df = pd.DataFrame(payment_rows)

payments_df.to_csv("data/Ticketing/payments.csv", index=False)

print("Payments generated:", len(payments_df))