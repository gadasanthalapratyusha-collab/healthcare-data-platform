from etl.extract import extract_all_data
from etl.transformers.patient_transformer import (
    transform_patients,
)

from etl.transformers.claim_transformer import (
    transform_claims,
)


def main() -> None:
    delivery_folder, datasets = extract_all_data()

    transformed_patients = transform_patients(
        datasets.get("patients")
    )

    transformed_claims = transform_claims(
    datasets.get("claims")
    )

    print(f"\nProcessed delivery: {delivery_folder.name}")

    if transformed_patients is not None:
     print(
        f"Clean patient rows: "
        f"{len(transformed_patients)}"
        )

    if transformed_claims is not None:
     print(
        f"Clean claim rows: "
        f"{len(transformed_claims)}"
        )


if __name__ == "__main__":
    main()