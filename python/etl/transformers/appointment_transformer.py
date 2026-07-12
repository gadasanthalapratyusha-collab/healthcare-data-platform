import pandas as pd

from etl.transformers.validation import (
    convert_date_columns,
    remove_duplicate_rows,
    strip_text_columns,
    validate_required_columns,
)


EXPECTED_COLUMNS = [
    "appointment_id",
    "patient_id",
    "provider_id",
    "appointment_date",
    "appointment_type",
    "status",
]


def transform_appointments(
    appointments_df: pd.DataFrame | None,
) -> pd.DataFrame | None:
    """
    Clean and validate appointment records.
    """

    if appointments_df is None:
        print("No appointment data received.")
        return None

    cleaned_df = appointments_df.copy()

    validate_required_columns(
        cleaned_df,
        EXPECTED_COLUMNS,
        "appointments",
    )

    original_count = len(cleaned_df)

    cleaned_df = remove_duplicate_rows(cleaned_df)

    cleaned_df = cleaned_df.drop_duplicates(
        subset=["appointment_id"],
        keep="last",
    )

    cleaned_df = strip_text_columns(
        cleaned_df,
        [
            "appointment_id",
            "patient_id",
            "provider_id",
            "appointment_type",
            "status",
        ],
    )

    cleaned_df = convert_date_columns(
        cleaned_df,
        ["appointment_date"],
    )

    cleaned_df = cleaned_df.dropna(
        subset=[
            "appointment_id",
            "patient_id",
            "provider_id",
            "appointment_date",
        ]
    )

    cleaned_df = cleaned_df[
        cleaned_df["appointment_id"].str.match(
            r"^A\d{8}$",
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

    cleaned_df["appointment_type"] = (
        cleaned_df["appointment_type"].str.title()
    )

    cleaned_df["status"] = cleaned_df["status"].str.title()

    valid_types = [
        "Routine",
        "Follow-Up",
        "Emergency",
        "Specialist",
    ]

    valid_statuses = [
        "Completed",
        "Cancelled",
        "Scheduled",
    ]

    cleaned_df = cleaned_df[
        cleaned_df["appointment_type"].isin(valid_types)
    ]

    cleaned_df = cleaned_df[
        cleaned_df["status"].isin(valid_statuses)
    ]

    cleaned_df = cleaned_df.reset_index(drop=True)

    removed_count = original_count - len(cleaned_df)

    print(
        f"Appointments transformed: {len(cleaned_df)} valid rows, "
        f"{removed_count} rows removed"
    )

    return cleaned_df