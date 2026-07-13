from etl.loaders.patient_loader import load_patients
from etl.transform import transform_all_data


def main() -> None:
    """
    Execute the ETL load stage.
    """

    delivery_folder, transformed_data = transform_all_data()

    print(f"\nLoading delivery: {delivery_folder.name}")

    load_patients(
        transformed_data["patients"]
    )

    print("\nLoad completed successfully.")


if __name__ == "__main__":
    main()