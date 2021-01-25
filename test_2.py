from sqlalchemy import (create_engine, MetaData, Column, Table, String, Integer)
from sqlalchemy.engine.url import URL


#Generating the Database Schema
def create_metdata_instance(engine):
    metdata_schema = MetaData(engine)
    return metdata_schema

def create_tbale(metadata):
    table = Table('Course', metadata, Column('id', Integer,primary_key=True, autoincrement=True), Column('crs_name', String))
    metadata.create_all()
    for _t in metadata.tables:
        print(_t)


if __name__ == "__main__":
    postgres_db = {
        'drivername': 'postgres',
        'username': 'odoo',
        'database': 'sqlalchemy',
        'password': 'odoo@123',
        'host': '127.0.0.1',
        'port': 5432
    }
    db_driver_url = URL(**postgres_db)
    pg_engine = create_engine(db_driver_url)
    create_tbale(create_metdata_instance(pg_engine))



    