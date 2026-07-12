import random

import pandas as pd


DIAGNOSIS_CODES = [
    "E11",
    "I10",
    "J45",
    "M54",
    "R51",
]

PROCEDURE_CODES = [
    "99213",
    "99214",
    "93000",
    "80053",
    "36415",
]

CLAIM_STATUSES = [
    "Approved",
    "Denied",
    "Pending",
]


def generate_claims(
    patients: pd.DataFrame,
    providers: pd.DataFrame,
    metadata: dict,
    run_date: str,
    count: int,
) -> pd.DataFrame:
    """
    Generate healthcare claims using valid patient and provider IDs.
    """
    rows = []

    patient_ids = patients["patient_id"].tolist()
    provider_ids = providers["provider_id"].tolist()

    for _ in range(count):
        metadata["last_claim_id"] += 1

        rows.append(
            {
                "claim_id": f"C{metadata['last_claim_id']:08d}",
                "patient_id": random.choice(patient_ids),
                "provider_id": random.choice(provider_ids),
                "diagnosis_code": random.choice(DIAGNOSIS_CODES),
                "procedure_code": random.choice(PROCEDURE_CODES),
                "claim_amount": round(
                    random.uniform(100, 5000),
                    2,
                ),
                "claim_date": run_date,
                "claim_status": random.choice(CLAIM_STATUSES),
            }
        )

    return pd.DataFrame(rows)