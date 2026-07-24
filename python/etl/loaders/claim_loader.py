from psycopg2.extras import execute_values

from etl.loaders.db import get_connection


def load_claims(
    claims_df,
) -> None:
    """
    Load cleaned claim records into PostgreSQL.
    """

    if claims_df is None or claims_df.empty:
        print("No claims to load.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    insert_sql = """
        INSERT INTO claims (
            claim_id,
            patient_id,
            provider_id,
            diagnosis_code,
            procedure_code,
            claim_amount,
            claim_date,
            claim_status
        )
        VALUES %s
        ON CONFLICT (claim_id)
        DO NOTHING;
    """

    values = [
        (
            row.claim_id,
            row.patient_id,
            row.provider_id,
            row.diagnosis_code,
            row.procedure_code,
            row.claim_amount,
            row.claim_date,
            row.claim_status,
        )
        for row in claims_df.itertuples()
    ]

    try:
        execute_values(
            cursor,
            insert_sql,
            values,
        )

        connection.commit()

        print(
            f"Loaded {len(values)} claims into PostgreSQL."
        )

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()