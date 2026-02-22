import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from faker import Faker
import os


airports_data = [
    ("LHR", "Heathrow Airport", "London", "UK", "Europe"),
    ("JFK", "John F Kennedy Intl", "New York", "USA", "North America"),
    ("DXB", "Dubai International", "Dubai", "UAE", "Middle East"),
    ("SIN", "Changi Airport", "Singapore", "Singapore", "Asia"),
    ("FRA", "Frankfurt Airport", "Frankfurt", "Germany", "Europe"),
    ("HND", "Tokyo Haneda", "Tokyo", "Japan", "Asia"),
    ("SYD", "Sydney Kingsford Smith", "Sydney", "Australia", "Oceania"),
    ("CDG", "Charles de Gaulle", "Paris", "France", "Europe"),
    ("LAX", "Los Angeles Intl", "Los Angeles", "USA", "North America"),
    ("DOH", "Hamad International", "Doha", "Qatar", "Middle East"),
    ("AMS", "Amsterdam Schiphol", "Amsterdam", "Netherlands", "Europe"),
    ("YYZ", "Toronto Pearson", "Toronto", "Canada", "North America"),
    ("ICN", "Incheon International", "Seoul", "South Korea", "Asia"),
    ("MAD", "Adolfo Suárez Madrid–Barajas", "Madrid", "Spain", "Europe"),
    ("BOM", "Chhatrapati Shivaji Maharaj Intl", "Mumbai", "India", "Asia")
]

import pandas as pd

airports = pd.DataFrame(airports_data, columns=[
    "iata_code","airport_name","city","country","region"
])

# Create PK
airports.insert(0, "airport_id",
                ["AID" + str(i).zfill(3) for i in range(1, len(airports)+1)])

airports.to_csv("data/Flight_Operations/airports.csv", index=False)

print("Airports generated:", len(airports))