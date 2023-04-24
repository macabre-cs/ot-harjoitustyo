from database_connection import get_database_connection


def destroy_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists pets;
    """)

    connection.commit()


def make_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        create table pets (
            name text primary key,
            password text
        );
    """)

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    destroy_tables(connection)
    make_tables(connection)


if __name__ == "__main__":
    initialize_database()
