import pandas as pd

from etl.transformers.validation import (
    convert_date_columns,
    remove_duplicate_rows,
    strip_text_columns,
    validate_required_columns,
)


EXPECTED_COLUMNS = [
    "prescription_id",
    "patient_id",
    "provider_id",
    "medication_name",
    "dosage",
    "prescription_date",
]


def transform_prescriptions(
    prescriptions_df: pd.DataFrame | None,
) -> pd.DataFrame | None:
    """
    Clean and validate prescription records.
    """

    if prescriptions_df is None:
        print("No prescription data received.")
        return None

    cleaned_df = prescriptions_df.copy()

    validate_required_columns(
        cleaned_df,
        EXPECTED_COLUMNS,
        "prescriptions",
    )

    original_count = len(cleaned_df)

    cleaned_df = remove_duplicate_rows(cleaned_df)

    cleaned_df = cleaned_df.drop_duplicates(
        subset=["prescription_id"],
        keep="last",
    )

    cleaned_df = strip_text_columns(
        cleaned_df,
        [
            "prescription_id",
            "patient_id",
            "provider_id",
            "medication_name",
            "dosage",
        ],
    )

    cleaned_df = convert_date_columns(
        cleaned_df,
        ["prescription_date"],
    )

    cleaned_df = cleaned_df.dropna(
        subset=[
            "prescription_id",
            "patient_id",
            "provider_id",
            "medication_name",
            "dosage",
            "prescription_date",
        ]
    )

    cleaned_df = cleaned_df[
        cleaned_df["prescription_id"].str.match(
            r"^RX\d{8}$",
            na=False,
        )
    ]

    cleaned_df = cleaned_df[
        cleaned_df["patient_id"].str.match(
            r"^P\d{6}$",
            na=False,
        )
    ]

    cleaned_df = cleaned_df[
        cleaned_df["provider_id"].str.match(
            r"^PR\d{5}$",
            na=False,
        )
    ]

    cleaned_df["medication_name"] = (
        cleaned_df["medication_name"].str.title()
    )

    cleaned_df["dosage"] = cleaned_df["dosage"].str.lower()

    cleaned_df = cleaned_df.reset_index(drop=True)

    removed_count = original_count - len(cleaned_df)

    print(
        f"Prescriptions transformed: {len(cleaned_df)} valid rows, "
        f"{removed_count} rows removed"
    )

    return cleaned_df