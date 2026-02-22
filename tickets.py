import pandas as pd
import random
from datetime import timedelta

# Load reference data
flights = pd.read_csv("data/Flight_Operations/flights.csv")
aircraft = pd.read_csv("data/Flight_Operations/aircraft.csv")
passengers = pd.read_csv("data/Ticketing/passengers.csv")

passenger_ids = passengers["passenger_id"].tolist()

ticket_rows = []
ticket_counter = 1

for _, flight in flights.iterrows():
    # Academic scope: fixed passenger band per flight
    num_passengers = random.randint(10, 20)
    
    selected_passengers = random.sample(passenger_ids, num_passengers)
    
    for passenger_id in selected_passengers:
        
        # Seat class distribution
        r = random.random()
        if r < 0.75:
            seat_class = "Economy"
            price = random.randint(200, 600)
        elif r < 0.95:
            seat_class = "Business"
            price = random.randint(800, 1500)
        else:
            seat_class = "First"
            price = random.randint(2500, 4000)
        
        # Booking date before flight
        flight_date = pd.to_datetime(flight["scheduled_departure"])
        booking_date = flight_date - timedelta(days=random.randint(1, 60))
        
        ticket_rows.append({
            "ticket_id": f"T{ticket_counter:07}",
            "flight_id": flight["flight_id"],
            "passenger_id": passenger_id,
            "seat_class": seat_class,
            "ticket_price": price,
            "booking_date": booking_date
        })
        
        ticket_counter += 1

tickets_df = pd.DataFrame(ticket_rows)

tickets_df.to_csv("data/Ticketing/tickets.csv", index=False)

print("Tickets generated:", len(tickets_df))