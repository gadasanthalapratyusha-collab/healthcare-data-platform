import random

import pandas as pd


APPOINTMENT_TYPES = [
    "Routine",
    "Follow-up",
    "Emergency",
    "Specialist",
]

APPOINTMENT_STATUSES = [
    "Completed",
    "Cancelled",
    "Scheduled",
]


def generate_appointments(
    patients: pd.DataFrame,
    providers: pd.DataFrame,
    metadata: dict,
    run_date: str,
    count: int,
) -> pd.DataFrame:
    """
    Generate daily appointments using valid patient and provider IDs.
    """
    rows = []

    patient_ids = patients["patient_id"].tolist()
    provider_ids = providers["provider_id"].tolist()

    for _ in range(count):
        metadata["last_appointment_id"] += 1

        rows.append(
            {
                "appointment_id": (
                    f"A{metadata['last_appointment_id']:08d}"
                ),
                "patient_id": random.choice(patient_ids),
                "provider_id": random.choice(provider_ids),
                "appointment_date": run_date,
                "appointment_type": random.choice(
                    APPOINTMENT_TYPES
                ),
                "status": random.choice(
                    APPOINTMENT_STATUSES
                ),
            }
        )

    return pd.DataFrame(rows)