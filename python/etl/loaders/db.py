import psycopg2


DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "healthcare_db",
    "user": "healthcare_user",
    "password": "healthcare_password",
}


def get_connection():
    """
    Create and return a PostgreSQL database connection.
    """

    connection = psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
    )

    return connection


def test_connection() -> None:
    """
    Verify database connectivity.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT version();")

    version = cursor.fetchone()[0]

    print("\nConnected successfully!")
    print(version)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    test_connection()