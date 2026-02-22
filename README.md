# Flight Data Generation

Synthetic airline dataset generator for academic OLTP/SQL projects.

This project creates relational CSV data for:
- Flight Operations
- Ticketing
- Maintenance

The generated data is suitable for database schema design, joins, constraints, ETL practice, and BI/reporting exercises.

## Features

- Generates linked entities with realistic IDs and relationships
- Creates data for flights, aircraft, airports, crew, passengers, tickets, payments, engineers, and maintenance records
- Writes outputs as CSV files under domain-specific folders
- Supports medium-size datasets suitable for student SQL Server projects

## Project Structure

```
.
├── aircraft.py
├── airports.py
├── crew.py
├── engineers.py
├── flight_crew.py
├── flights.py
├── maintanance.py
├── passengers.py
├── payments.py
├── tickets.py
├── main.py
├── pyproject.toml
└── data/
		├── Flight_Operations/
		├── Maintenance/
		└── Ticketing/
```

## Data Model Overview

Core relationships:
- `airports` 1-to-many `flights` (departure and arrival)
- `aircraft` 1-to-many `flights`
- `crew` many-to-many `flights` through `flight_crew`
- `passengers` 1-to-many `tickets`
- `flights` 1-to-many `tickets`
- `tickets` 1-to-1 `payments`
- `aircraft` 1-to-many `maintenance_records`
- `engineers` 1-to-many `maintenance_records`

## Requirements

- Python 3.12+
- Dependencies from `pyproject.toml`:
	- `pandas`
	- `faker`
	- `numpy`
	- `openpyxl`

## Setup

Using `uv` (recommended):

```bash
uv sync
```

Or with `pip`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install pandas faker numpy openpyxl
```

## Generate Data

Run scripts in this order:

```bash
python3 airports.py
python3 aircraft.py
python3 crew.py
python3 flights.py
python3 flight_crew.py

python3 passengers.py
python3 tickets.py
python3 payments.py

python3 engineers.py
python3 maintanance.py
```

## Current Expected Volumes

Based on current settings:
- Flights: ~5,117
- Tickets: ~76k (balanced mode)
- Payments: same as tickets
- Maintenance records: ~100-200 (depends on random intervals)

## Notes

- Data is randomly generated, so exact values vary each run.
- IDs are deterministic in format (e.g., `F000001`, `T0000001`, `PAY0000001`) but row content is randomized.
- Generated CSV files under `data/` are ignored in Git to keep repository size small.

## License

This project is intended for educational use.
