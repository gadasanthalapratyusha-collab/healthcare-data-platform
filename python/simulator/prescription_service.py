import random

import pandas as pd


MEDICATIONS = [
    "Metformin",
    "Lisinopril",
    "Atorvastatin",
    "Amoxicillin",
    "Albuterol",
]

DOSAGES = [
    "5mg",
    "10mg",
    "20mg",
    "500mg",
]


def generate_prescriptions(
    patients: pd.DataFrame,
    providers: pd.DataFrame,
    metadata: dict,
    run_date: str,
    count: int,
) -> pd.DataFrame:
    """
    Generate daily prescriptions.
    """

    rows = []

    patient_ids = patients["patient_id"].tolist()
    provider_ids = providers["provider_id"].tolist()

    for _ in range(count):

        metadata["last_prescription_id"] += 1

        rows.append(
            {
                "prescription_id":
                    f"RX{metadata['last_prescription_id']:08d}",

                "patient_id":
                    random.choice(patient_ids),

                "provider_id":
                    random.choice(provider_ids),

                "medication_name":
                    random.choice(MEDICATIONS),

                "dosage":
                    random.choice(DOSAGES),

                "prescription_date":
                    run_date,
            }
        )

    return pd.DataFrame(rows)