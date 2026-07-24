from psycopg2.extras import execute_values


from etl.loaders.db import get_connection


def load_appointments(appointments_df) -> None:
    """
    Load appointments into PostgreSQL.
    """

    if appointments_df.empty:
        print("No appointments to load.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    insert_sql = """
        INSERT INTO appointments (
            appointment_id,
            patient_id,
            provider_id,
            appointment_date,
            appointment_type,
            status
        )
        VALUES %s
        ON CONFLICT (appointment_id)
        DO NOTHING;
    """

    values = [
        (
            row.appointment_id,
            row.patient_id,
            row.provider_id,
            row.appointment_date,
            row.appointment_type,
            row.status,
        )
        for row in appointments_df.itertuples()
    ]

    try:
        execute_values(cursor, insert_sql, values)
        connection.commit()

        print(
            f"Loaded {len(values)} appointments into PostgreSQL."
        )

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()