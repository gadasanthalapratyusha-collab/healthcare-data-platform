import pandas as pd

from etl.transformers.validation import (
    convert_date_columns,
    remove_duplicate_rows,
    strip_text_columns,
    validate_required_columns,
)


EXPECTED_COLUMNS = [
    "claim_id",
    "patient_id",
    "provider_id",
    "diagnosis_code",
    "procedure_code",
    "claim_amount",
    "claim_date",
    "claim_status",
]


def transform_claims(
    claims_df: pd.DataFrame | None,
) -> pd.DataFrame | None:
    """
    Clean and validate claim records.
    """

    if claims_df is None:
        print("No claim data received.")
        return None

    cleaned_df = claims_df.copy()

    validate_required_columns(
        cleaned_df,
        EXPECTED_COLUMNS,
        "claims",
    )

    original_count = len(cleaned_df)

    # Remove duplicate rows
    cleaned_df = remove_duplicate_rows(cleaned_df)

    # Remove duplicate claim IDs
    cleaned_df = cleaned_df.drop_duplicates(
        subset=["claim_id"],
        keep="last",
    )

    # Clean text columns
    cleaned_df = strip_text_columns(
        cleaned_df,
        [
            "claim_id",
            "patient_id",
            "provider_id",
            "diagnosis_code",
            "procedure_code",
            "claim_status",
        ],
    )

    # Convert claim date
    cleaned_df = convert_date_columns(
        cleaned_df,
        ["claim_date"],
    )

    # Remove incomplete records
    cleaned_df = cleaned_df.dropna(
        subset=[
            "claim_id",
            "patient_id",
            "provider_id",
            "claim_date",
        ]
    )

    # Validate IDs
    cleaned_df = cleaned_df[
        cleaned_df["claim_id"].str.match(
            r"^C\d{8}$",
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

    # Ensure claim amount is numeric
    cleaned_df["claim_amount"] = pd.to_numeric(
        cleaned_df["claim_amount"],
        errors="coerce",
    )

    cleaned_df = cleaned_df.dropna(
        subset=["claim_amount"]
    )

    # Remove negative claims
    cleaned_df = cleaned_df[
        cleaned_df["claim_amount"] >= 0
    ]

    # Standardize claim status
    cleaned_df["claim_status"] = (
        cleaned_df["claim_status"]
        .str.title()
    )

    cleaned_df = cleaned_df.reset_index(drop=True)

    removed_count = original_count - len(cleaned_df)

    print(
        f"Claims transformed: {len(cleaned_df)} valid rows, "
        f"{removed_count} rows removed"
    )

    return cleaned_df