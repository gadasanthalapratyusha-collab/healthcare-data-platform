import random
from pathlib import Path

import pandas as pd

from simulator.metadata_manager import (
    get_next_date,
    load_metadata,
    save_metadata,
)
from simulator.patient_service import generate_new_patients

RAW_DIR = Path("data/raw")
SAMPLE_DIR = Path("data/sample")

MASTER_PATIENTS_FILE = SAMPLE_DIR / "master_patients.csv"
MASTER_PROVIDERS_FILE = SAMPLE_DIR / "master_providers.csv"


def create_daily_folder(run_date: str) -> Path:
    """
    Create a folder for the next hospital delivery date.

    Example:
        data/raw/2026-07-02/
    """
    daily_folder = RAW_DIR / run_date

    if daily_folder.exists():
        raise FileExistsError(
            f"Daily folder already exists: {daily_folder}"
        )

    daily_folder.mkdir(parents=True)
    return daily_folder


def load_master_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load the permanent patient and provider registries.
    """
    if not MASTER_PATIENTS_FILE.exists():
        raise FileNotFoundError(
            f"Master patient file not found: "
            f"{MASTER_PATIENTS_FILE}"
        )

    if not MASTER_PROVIDERS_FILE.exists():
        raise FileNotFoundError(
            f"Master provider file not found: "
            f"{MASTER_PROVIDERS_FILE}"
        )

    patients = pd.read_csv(MASTER_PATIENTS_FILE)
    providers = pd.read_csv(MASTER_PROVIDERS_FILE)

    return patients, providers


def generate_claims(
    patients: pd.DataFrame,
    providers: pd.DataFrame,
    metadata: dict,
    run_date: str,
    count: int,
) -> pd.DataFrame:
    """
    Generate claims using valid patient and provider IDs.
    """
    rows = []

    patient_ids = patients["patient_id"].tolist()
    provider_ids = providers["provider_id"].tolist()

    diagnosis_codes = [
        "E11",
        "I10",
        "J45",
        "M54",
        "R51",
    ]

    procedure_codes = [
        "99213",
        "99214",
        "93000",
        "80053",
        "36415",
    ]

    for _ in range(count):
        metadata["last_claim_id"] += 1

        rows.append(
            {
                "claim_id": (
                    f"C{metadata['last_claim_id']:08d}"
                ),
                "patient_id": random.choice(patient_ids),
                "provider_id": random.choice(provider_ids),
                "diagnosis_code": random.choice(
                    diagnosis_codes
                ),
                "procedure_code": random.choice(
                    procedure_codes
                ),
                "claim_amount": round(
                    random.uniform(100, 5000),
                    2,
                ),
                "claim_date": run_date,
                "claim_status": random.choice(
                    ["Approved", "Denied", "Pending"]
                ),
            }
        )

    return pd.DataFrame(rows)


def generate_appointments(
    patients: pd.DataFrame,
    providers: pd.DataFrame,
    metadata: dict,
    run_date: str,
    count: int,
) -> pd.DataFrame:
    """
    Generate daily patient appointments.
    """
    rows = []

    patient_ids = patients["patient_id"].tolist()
    provider_ids = providers["provider_id"].tolist()

    appointment_types = [
        "Routine",
        "Follow-up",
        "Emergency",
        "Specialist",
    ]

    appointment_statuses = [
        "Completed",
        "Cancelled",
        "Scheduled",
    ]

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
                    appointment_types
                ),
                "status": random.choice(
                    appointment_statuses
                ),
            }
        )

    return pd.DataFrame(rows)


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

    medications = [
        "Metformin",
        "Lisinopril",
        "Atorvastatin",
        "Amoxicillin",
        "Albuterol",
    ]

    dosages = [
        "5mg",
        "10mg",
        "20mg",
        "500mg",
    ]

    for _ in range(count):
        metadata["last_prescription_id"] += 1

        rows.append(
            {
                "prescription_id": (
                    f"RX{metadata['last_prescription_id']:08d}"
                ),
                "patient_id": random.choice(patient_ids),
                "provider_id": random.choice(provider_ids),
                "medication_name": random.choice(
                    medications
                ),
                "dosage": random.choice(dosages),
                "prescription_date": run_date,
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    """
    Generate one new day of hospital operational data.
    """
    metadata = load_metadata()
    metadata.setdefault("last_patient_id", 1000)
    metadata.setdefault("last_provider_id", 200)
    metadata.setdefault("last_claim_id", 100)
    metadata.setdefault("last_appointment_id", 60)
    metadata.setdefault("last_prescription_id", 40)
    metadata.setdefault("days_generated", 1)
    run_date = get_next_date(metadata)

    daily_folder = create_daily_folder(run_date)

    master_patients, master_providers = (
        load_master_data()
    )

    # Generate only today's newly registered patients.
    new_patients = generate_new_patients(metadata)

    if not new_patients.empty:
        new_patients.to_csv(
            daily_folder / "patients.csv",
            index=False,
        )

        # Add new patients to the permanent master registry.
        master_patients = pd.concat(
            [master_patients, new_patients],
            ignore_index=True,
        )

        master_patients.to_csv(
            MASTER_PATIENTS_FILE,
            index=False,
        )

    # Transaction files arrive every day.
    claim_count = random.randint(100, 150)
    appointment_count = random.randint(50, 80)
    prescription_count = random.randint(25, 50)

    claims = generate_claims(
        patients=master_patients,
        providers=master_providers,
        metadata=metadata,
        run_date=run_date,
        count=claim_count,
    )

    appointments = generate_appointments(
        patients=master_patients,
        providers=master_providers,
        metadata=metadata,
        run_date=run_date,
        count=appointment_count,
    )

    prescriptions = generate_prescriptions(
        patients=master_patients,
        providers=master_providers,
        metadata=metadata,
        run_date=run_date,
        count=prescription_count,
    )

    claims.to_csv(
        daily_folder / "claims.csv",
        index=False,
    )

    appointments.to_csv(
        daily_folder / "appointments.csv",
        index=False,
    )

    prescriptions.to_csv(
        daily_folder / "prescriptions.csv",
        index=False,
    )

    # Provider reference data is not resent every day.

    metadata["last_generated_date"] = run_date
    metadata["days_generated"] += 1

    save_metadata(metadata)

    print("=" * 50)
    print(f"Hospital delivery generated for {run_date}")
    print(f"Folder: {daily_folder}")
    print(f"New patients: {len(new_patients)}")
    print(f"Claims: {len(claims)}")
    print(f"Appointments: {len(appointments)}")
    print(f"Prescriptions: {len(prescriptions)}")
    print("=" * 50)


if __name__ == "__main__":
    main()