from psycopg2.extras import execute_values

from etl.loaders.db import get_connection


def load_providers(
    providers_df,
) -> None:
    """
    Load provider reference data into PostgreSQL.
    """

    if providers_df is None or providers_df.empty:
        print("No providers to load.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    insert_sql = """
        INSERT INTO providers (
            provider_id,
            provider_name,
            specialty,
            hospital_name,
            state
        )
        VALUES %s
        ON CONFLICT (provider_id)
        DO NOTHING;
    """

    values = [
        (
            row.provider_id,
            row.provider_name,
            row.specialty,
            row.hospital_name,
            row.state,
        )
        for row in providers_df.itertuples()
    ]

    execute_values(
        cursor,
        insert_sql,
        values,
    )

    connection.commit()

    print(
        f"Loaded {len(values)} providers into PostgreSQL."
    )

    cursor.close()
    connection.close()