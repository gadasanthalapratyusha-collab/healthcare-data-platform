import pandas as pd


def validate_required_columns(
    dataframe: pd.DataFrame,
    expected_columns: list[str],
    dataset_name: str,
) -> None:
    """
    Ensure all expected columns exist.
    """

    missing_columns = [
        column
        for column in expected_columns
        if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(
            f"{dataset_name} is missing columns: "
            f"{missing_columns}"
        )


def remove_duplicate_rows(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """
    Remove exact duplicate rows.
    """
    return dataframe.drop_duplicates()


def strip_text_columns(
    dataframe: pd.DataFrame,
    columns: list[str],
) -> pd.DataFrame:
    """
    Remove leading and trailing spaces.
    """

    dataframe = dataframe.copy()

    for column in columns:
        dataframe[column] = (
            dataframe[column]
            .astype("string")
            .str.strip()
        )

    return dataframe


def convert_date_columns(
    dataframe: pd.DataFrame,
    columns: list[str],
) -> pd.DataFrame:
    """
    Convert date columns to datetime.
    """

    dataframe = dataframe.copy()

    for column in columns:
        dataframe[column] = pd.to_datetime(
            dataframe[column],
            errors="coerce",
        )

    return dataframe