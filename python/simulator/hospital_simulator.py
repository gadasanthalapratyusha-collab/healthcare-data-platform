import random
from pathlib import Path

import pandas as pd

from simulator.appointment_service import generate_appointments
from simulator.claim_service import generate_claims
from simulator.metadata_manager import (
    get_next_date,
    load_metadata,
    save_metadata,
)
from simulator.patient_service import generate_new_patients
from simulator.prescription_service import generate_prescriptions


RAW_DIR = Path("data/raw")
SAMPLE_DIR = Path("data/sample")

MASTER_PATIENTS_FILE = SAMPLE_DIR / "master_patients.csv"
MASTER_PROVIDERS_FILE = SAMPLE_DIR / "master_providers.csv"


def create_daily_folder(run_date: str) -> Path:
    """
    Create a folder for one daily hospital delivery.
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
            f"Master patient file not found: {MASTER_PATIENTS_FILE}"
        )

    if not MASTER_PROVIDERS_FILE.exists():
        raise FileNotFoundError(
            f"Master provider file not found: {MASTER_PROVIDERS_FILE}"
        )

    patients = pd.read_csv(MASTER_PATIENTS_FILE)
    providers = pd.read_csv(MASTER_PROVIDERS_FILE)

    return patients, providers


def initialize_metadata_defaults(metadata: dict) -> None:
    """
    Add missing metadata fields without replacing existing values.
    """
    metadata.setdefault("last_patient_id", 1000)
    metadata.setdefault("last_provider_id", 200)
    metadata.setdefault("last_claim_id", 100)
    metadata.setdefault("last_appointment_id", 60)
    metadata.setdefault("last_prescription_id", 40)
    metadata.setdefault("days_generated", 1)


def main() -> None:
    """
    Generate one new day of hospital operational data.
    """
    metadata = load_metadata()
    initialize_metadata_defaults(metadata)

    run_date = get_next_date(metadata)
    daily_folder = create_daily_folder(run_date)

    master_patients, master_providers = load_master_data()

    new_patients = generate_new_patients(metadata)

    if not new_patients.empty:
        new_patients.to_csv(
            daily_folder / "patients.csv",
            index=False,
        )

        master_patients = pd.concat(
            [master_patients, new_patients],
            ignore_index=True,
        )

        master_patients.to_csv(
            MASTER_PATIENTS_FILE,
            index=False,
        )

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