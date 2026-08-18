import psycopg2


def get_db_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="sevaconnect_ngo",
        user="postgres",
        password="12345",
        port="5432"
    )

    return connection