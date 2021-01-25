from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine as pg_engine


# create table
def create_student_table(engine):
    query = "CREATE TABLE student (id INTEGER NOT NULL, name VARCHAR NOT NULL, age INTEGER NOT NULL, std INTEGER NOT NULL, PRIMARY KEY (id));"
    try:
        engine.execute(query)
    except Exception as e:
        print(e)

def insert_student_table(engine):
    query_l = ["INSERT INTO student (id,name,age,std) VALUES (2,'AjayKumar',23,12);", 
               "INSERT INTO student (id,name,age,std) VALUES (3,'Arulkumar',23,12);",
               "INSERT INTO student (id,name,age,std) VALUES (4,'Nerupkumar',24,8);",
               "INSERT INTO student (id,name,age,std) VALUES (5,'Deepan Kumar',25,9);"]
    try:
        for query in query_l:
            engine.execute(query)
    except Exception as e:
        print(e)

def update_student_table(engine=None, whr_id=None, upda_res=None, upda_q=None):
    query = "UPDATE student SET {upda_q} = {upda_res} WHERE id = {ids};".format(upda_q=upda_q, upda_res=upda_res, ids=whr_id)
    try:
        engine.execute(query)
    except Exception as e:
        print(e)

def delete_student_record(engine, whr_id=None):
    query = "DELETE FROM student where id = {ids}".format(ids=whr_id)
    try:
        engine.execute(query)
    except Exception as e:
        print(e)




if __name__ == "__main__":
    postgres_db = {
    'drivername': 'postgres',
    'username': 'odoo',
    'database': 'sqlalchemy',
    'password': 'odoo@123',
    'host': '127.0.0.1',
    'port': 5432
    }
    db_engine = pg_engine(URL(**postgres_db))
    # create_student_table(db_engine)
    # insert_student_table(db_engine)
    # update_student_table(engine=db_engine, whr_id=1, upda_res=74, upda_q='age')
    delete_student_record(engine=db_engine, whr_id=4)
    
