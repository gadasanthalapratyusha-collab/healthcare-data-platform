from psycopg2.extras import execute_values

from etl.loaders.db import get_connection


def load_prescriptions(prescriptions_df) -> None:
    """
    Load prescriptions into PostgreSQL.
    """

    if prescriptions_df.empty:
        print("No prescriptions to load.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    insert_sql = """
        INSERT INTO prescriptions (
            prescription_id,
            patient_id,
            provider_id,
            medication_name,
            dosage,
            prescription_date
        )
        VALUES %s
        ON CONFLICT (prescription_id)
        DO NOTHING;
    """

    values = [
        (
            row.prescription_id,
            row.patient_id,
            row.provider_id,
            row.medication_name,
            row.dosage,
            row.prescription_date,
        )
        for row in prescriptions_df.itertuples()
    ]

    try:
        execute_values(cursor, insert_sql, values)
        connection.commit()

        print(
            f"Loaded {len(values)} prescriptions into PostgreSQL."
        )

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()