from etl.loaders.claim_loader import load_claims
from etl.loaders.master_patient_loader import (
    load_master_patients,
)
from etl.loaders.provider_loader import load_providers
from etl.transform import transform_all_data
from etl.loaders.appointment_loader import load_appointments
from etl.loaders.prescription_loader import load_prescriptions


def main() -> None:
    """
    Run the complete load stage for the latest delivery.
    """

    delivery_folder, transformed_data = transform_all_data()

    print(f"\nLoading delivery: {delivery_folder.name}")

    # Parent and reference tables must load first.
    load_providers(
        transformed_data["providers"]
    )

    load_master_patients()

    # Transactional tables load afterward.
    load_claims(
        transformed_data["claims"]
    )

    load_appointments(
        transformed_data["appointments"]
    )

    load_prescriptions(
        transformed_data["prescriptions"]
    )

    print("\nLoad completed successfully.")


if __name__ == "__main__":
    main()