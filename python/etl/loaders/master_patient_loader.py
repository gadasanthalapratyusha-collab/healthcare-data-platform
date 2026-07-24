from pathlib import Path

import pandas as pd
from psycopg2.extras import execute_values

from etl.loaders.db import get_connection


MASTER_PATIENTS_FILE = Path(
    "data/sample/master_patients.csv"
)


def load_master_patients() -> None:
    """
    Load the complete master patient registry into PostgreSQL.
    """

    if not MASTER_PATIENTS_FILE.exists():
        raise FileNotFoundError(
            f"Master patient file not found: "
            f"{MASTER_PATIENTS_FILE}"
        )

    patients_df = pd.read_csv(MASTER_PATIENTS_FILE)

    if patients_df.empty:
        print("No master patients to load.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    insert_sql = """
        INSERT INTO patients (
            patient_id,
            first_name,
            last_name,
            gender,
            date_of_birth,
            state
        )
        VALUES %s
        ON CONFLICT (patient_id)
        DO NOTHING;
    """

    values = [
        (
            row.patient_id,
            row.first_name,
            row.last_name,
            row.gender,
            row.date_of_birth,
            row.state,
        )
        for row in patients_df.itertuples()
    ]

    try:
        execute_values(
            cursor,
            insert_sql,
            values,
        )

        connection.commit()

        print(
            f"Loaded {len(values)} master patients "
            f"into PostgreSQL."
        )

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()