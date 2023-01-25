from sqlalchemy import text
from db.core.initializer import create_connection


def run_db_select_statement():
    """Creates a self closing connection to the database after outputting 'Hello World'"""
    with create_connection() as conn:
        result = conn.execute(text("select 'Hello World'"))
        print(result.all())


def create_table():
    """Creates a new table with persons"""
    with create_connection() as conn:
        conn.execute(
            text(
                '''
                CREATE TABLE person (
                    person_id              SERIAL PRIMARY KEY,
                    gender          VARCHAR(200) NOT NULL,
                    name            VARCHAR(250) NOT NULL,
                    surname         VARCHAR(200)
                )
                '''
            )
        )


def drop_item_table():
    """Method that can drop the table"""
    with create_connection() as conn:
        conn.execute(text("DROP TABLE Item"))
        conn.commit()


def show_all_tables():
    """Method that can show all tables from db"""
    with create_connection() as conn:
        results = conn.execute(
            text(
                '''
                SELECT * FROM pg_catalog.pg_tables
                WHERE schemaname != 'pg_catalog' 
                AND schemaname != 'information_schema'
                '''
            )
        )
        for data in results:
            print(f"{data[1]} Table".title())


def retrieve_all_item():
    """Retrieves all records from Item table"""
    with create_connection() as conn:
        results = conn.execute(
            text("SELECT * FROM person")
        )
        for result in results:
            print(result)
