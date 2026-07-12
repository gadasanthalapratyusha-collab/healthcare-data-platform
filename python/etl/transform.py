from etl.extract import extract_all_data
from etl.transformers.appointment_transformer import (
    transform_appointments,
)
from etl.transformers.claim_transformer import (
    transform_claims,
)
from etl.transformers.patient_transformer import (
    transform_patients,
)
from etl.transformers.prescription_transformer import (
    transform_prescriptions,
)


def transform_all_data() -> tuple:
    """
    Extract and transform all datasets for the latest delivery.
    """
    delivery_folder, datasets = extract_all_data()

    transformed_data = {
        "patients": transform_patients(
            datasets.get("patients")
        ),
        "claims": transform_claims(
            datasets.get("claims")
        ),
        "appointments": transform_appointments(
            datasets.get("appointments")
        ),
        "prescriptions": transform_prescriptions(
            datasets.get("prescriptions")
        ),
        "providers": datasets.get("providers"),
    }

    return delivery_folder, transformed_data


def main() -> None:
    delivery_folder, transformed_data = transform_all_data()

    print(f"\nProcessed delivery: {delivery_folder.name}")

    for dataset_name, dataframe in transformed_data.items():
        if dataframe is None:
            print(f"{dataset_name}: no data received")
        else:
            print(
                f"Clean {dataset_name} rows: "
                f"{len(dataframe)}"
            )


if __name__ == "__main__":
    main()