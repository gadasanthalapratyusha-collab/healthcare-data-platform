from psycopg2.extras import execute_values

from etl.loaders.db import get_connection


def load_patients(
    patients_df,
) -> None:
    """
    Load cleaned patient records into PostgreSQL.
    """

    if patients_df is None or patients_df.empty:
        print("No patients to load.")
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

    execute_values(
        cursor,
        insert_sql,
        values,
    )

    connection.commit()

    print(
        f"Loaded {len(values)} patients."
    )

    cursor.close()
    connection.close()