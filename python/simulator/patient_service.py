import random
from datetime import datetime, timedelta

import pandas as pd


FIRST_NAMES = [
    "John",
    "Mary",
    "David",
    "Sarah",
    "Michael",
    "Linda",
    "James",
    "Patricia",
    "Robert",
    "Jennifer",
]

LAST_NAMES = [
    "Smith",
    "Johnson",
    "Brown",
    "Davis",
    "Wilson",
    "Taylor",
    "Anderson",
    "Thomas",
    "Moore",
    "Martin",
]

STATES = [
    "TX",
    "CA",
    "NY",
    "FL",
    "IL",
    "AZ",
    "GA",
    "NC",
]


def random_date(
    start_year: int = 1950,
    end_year: int = 2010,
) -> str:
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)

    date_range = end_date - start_date
    selected_date = start_date + timedelta(
        days=random.randint(0, date_range.days)
    )

    return selected_date.strftime("%Y-%m-%d")


def generate_new_patients(
    metadata: dict,
) -> pd.DataFrame:
    new_patient_count = random.randint(0, 20)
    rows = []

    for _ in range(new_patient_count):
        metadata["last_patient_id"] += 1
        patient_number = metadata["last_patient_id"]

        rows.append(
            {
                "patient_id": f"P{patient_number:06d}",
                "first_name": random.choice(FIRST_NAMES),
                "last_name": random.choice(LAST_NAMES),
                "gender": random.choice(["Male", "Female"]),
                "date_of_birth": random_date(),
                "state": random.choice(STATES),
            }
        )

    columns = [
        "patient_id",
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
        "state",
    ]

    return pd.DataFrame(rows, columns=columns)