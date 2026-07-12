import pandas as pd

from etl.transformers.validation import (
    convert_date_columns,
    remove_duplicate_rows,
    strip_text_columns,
    validate_required_columns,
)


EXPECTED_COLUMNS = [
    "patient_id",
    "first_name",
    "last_name",
    "gender",
    "date_of_birth",
    "state",
]


def transform_patients(
    patients_df: pd.DataFrame | None,
) -> pd.DataFrame | None:
    """
    Clean and validate newly received patient records.
    """

    # Some daily deliveries may not contain patients.csv.
    if patients_df is None:
        print("No patient data received for this delivery.")
        return None

    cleaned_df = patients_df.copy()

    validate_required_columns(
        cleaned_df,
        EXPECTED_COLUMNS,
        "patients",
    )

    original_count = len(cleaned_df)

    # Remove exact duplicate rows.
    cleaned_df = remove_duplicate_rows(cleaned_df)

    # Remove duplicate patient IDs, keeping the latest row.
    cleaned_df = cleaned_df.drop_duplicates(
        subset=["patient_id"],
        keep="last",
    )

    text_columns = [
        "patient_id",
        "first_name",
        "last_name",
        "gender",
        "state",
    ]

    cleaned_df = strip_text_columns(
        cleaned_df,
        text_columns,
    )

    # Standardize values.
    cleaned_df["gender"] = cleaned_df["gender"].str.title()
    cleaned_df["state"] = cleaned_df["state"].str.upper()

    # Convert date of birth to a datetime value.
    cleaned_df = convert_date_columns(
        cleaned_df,
        ["date_of_birth"],
    )

    # Remove records missing required fields.
    cleaned_df = cleaned_df.dropna(
        subset=[
            "patient_id",
            "first_name",
            "last_name",
            "date_of_birth",
        ]
    )

    # Validate patient ID format: P followed by six digits.
    valid_patient_ids = cleaned_df[
        "patient_id"
    ].str.match(r"^P\d{6}$", na=False)

    cleaned_df = cleaned_df[valid_patient_ids]

    # Keep only supported gender values.
    cleaned_df = cleaned_df[
        cleaned_df["gender"].isin(
            ["Male", "Female"]
        )
    ]

    cleaned_df = cleaned_df.reset_index(drop=True)

    removed_count = original_count - len(cleaned_df)

    print(
        f"Patients transformed: {len(cleaned_df)} valid rows, "
        f"{removed_count} rows removed"
    )

    return cleaned_df