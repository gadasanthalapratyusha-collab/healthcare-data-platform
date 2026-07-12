from pathlib import Path

import pandas as pd


RAW_DIR = Path("data/raw")
SAMPLE_DIR = Path("data/sample")
MASTER_PROVIDERS_FILE = SAMPLE_DIR / "master_providers.csv"


def find_latest_delivery() -> Path:
    """
    Find the latest dated folder inside data/raw.
    """
    delivery_folders = [
        folder
        for folder in RAW_DIR.iterdir()
        if folder.is_dir()
    ]

    if not delivery_folders:
        raise FileNotFoundError(
            "No daily delivery folders found in data/raw."
        )

    return max(delivery_folders, key=lambda folder: folder.name)


def extract_csv_files(
    delivery_folder: Path,
) -> dict[str, pd.DataFrame]:
    """
    Read all CSV files from the selected daily delivery.
    """
    extracted_data = {}

    for csv_file in delivery_folder.glob("*.csv"):
        table_name = csv_file.stem
        dataframe = pd.read_csv(csv_file)

        extracted_data[table_name] = dataframe

        print(
            f"Extracted {csv_file.name}: "
            f"{len(dataframe)} rows"
        )

    if not extracted_data:
        raise FileNotFoundError(
            f"No CSV files found in {delivery_folder}"
        )

    return extracted_data


def extract_reference_data() -> dict[str, pd.DataFrame]:
    """
    Read reference/master datasets that do not arrive daily.
    """
    if not MASTER_PROVIDERS_FILE.exists():
        raise FileNotFoundError(
            f"Master provider file not found: "
            f"{MASTER_PROVIDERS_FILE}"
        )

    providers = pd.read_csv(MASTER_PROVIDERS_FILE)

    print(
        f"Extracted reference data "
        f"{MASTER_PROVIDERS_FILE.name}: "
        f"{len(providers)} rows"
    )

    return {
        "providers": providers
    }


def extract_all_data() -> tuple[
    Path,
    dict[str, pd.DataFrame],
]:
    """
    Extract both daily transactional data and reference data.
    """
    latest_delivery = find_latest_delivery()

    print(f"Latest delivery: {latest_delivery}")

    extracted_data = extract_csv_files(latest_delivery)
    reference_data = extract_reference_data()

    extracted_data.update(reference_data)

    return latest_delivery, extracted_data


def main() -> None:
    delivery_folder, datasets = extract_all_data()

    print(f"\nProcessing delivery: {delivery_folder.name}")

    claims_df = datasets.get("claims")
    providers_df = datasets.get("providers")
    patients_df = datasets.get("patients")

    if claims_df is not None:
        print(f"Claims available: {len(claims_df)} rows")

    if providers_df is not None:
        print(f"Providers available: {len(providers_df)} rows")

    if patients_df is not None:
        print(f"New patients available: {len(patients_df)} rows")
    else:
        print("No new patients file in this delivery.")


if __name__ == "__main__":
    main()