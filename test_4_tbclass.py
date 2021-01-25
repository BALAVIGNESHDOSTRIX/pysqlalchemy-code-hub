from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

pgconfig = {
    'drivername': 'postgres',
    'username': 'odoo',
    'password': 'odoo@123',
    'host': '127.0.0.1',
    'port': 5432,
    'database': 'sqlalchemy'
}

pgengine = create_engine(URL(**pgconfig))
Base = declarative_base()

class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)

Session = sessionmaker(pgengine)
session = Session()

def tablecr():
    Base.metadata.create_all(pgengine)

def create_records():
    value_l = ([2,'God of War', 1982], [3,'Ethens', 1984], 
              [4,'MIB', 1990], [5, 'Godzilla', 1987])
    for x in value_l:
        flm_obj = Film(id=x[0], title=x[1], year=x[2])
        session.add(flm_obj)
        session.commit()

def read_records(filter_year=None):
    for x in session.query(Film).filter(Film.year == int(filter_year)):
        print(x.id, x.title, x.year)

def update_records(sear_y, result):
    for x in session.query(Film).filter(Film.year == sear_y):
        x.title = result
        session.commit()

def delete_records(sear_y):
    for x in session.query(Film).filter(Film.year == sear_y):
        session.delete(x)
        session.commit()


    

if __name__ == '__main__':
    # create_records()
    # read_records(1984)
    # update_records(1987, "Armagedon")
    delete_records(1987)
    


