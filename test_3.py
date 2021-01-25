from sqlalchemy.engine.url import URL
from sqlalchemy import (create_engine, MetaData, Table, Column, String, Integer, inspect)

def get_tables(engine):
    inspector = inspect(engine)
    print(inspector.get_table_names())

def get_columns(engine, tbname):
    inspector = inspect(engine)
    print(inspector.get_columns(tbname))


if __name__ == "__main__":
    pg_db = {
        'drivername': 'postgres',
        'username': 'odoo',
        'password': 'odoo@123',
        'database': 'sqlalchemy',
        'host': '127.0.0.1',
        'port': 5432
    }
    pg_engine = create_engine(URL(**pg_db))
    # get_tables(pg_engine)
    get_columns(pg_engine, 'student')