import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from faker import Faker
import os

fake = Faker()

# PARAMETERS
START_DATE = datetime(2023,1,1)
END_DATE = datetime(2024,12,31)
FLIGHTS_PER_DAY = 7
NUM_AIRCRAFT = 15
NUM_PASSENGERS = 1500
NUM_CREW = 60
NUM_ENGINEERS = 15

# Create folder structure
os.makedirs("data/Flight_Operations", exist_ok=True)
os.makedirs("data/Ticketing", exist_ok=True)
os.makedirs("data/Maintenance", exist_ok=True)

