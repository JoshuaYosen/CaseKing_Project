import sqlite3
from sqlite3 import Error


#function creates a connection to sqlite database
def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


#function creates SQL tables into database
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


#function defines table structures in database and inserts them into database
def main():
    database = r"/home/rhulain/Python Projects/CaseKing_Prjct/Scripts/db_file.db"

    sql_create_units_table = """CREATE TABLE IF NOT EXISTS Units (
        order_id          integer PRIMARY KEY,
        accuracy          name,
        age               name,
        armor             name,
        armor_bonus       name,
        attack            float,
        attack_bonus      name,
        attack_delay      float,
        blast_radius      float,
        build_time        float,
        cost              name,
        created_in        name,
        description       name,
        expansion         name,
        hit_points        integer,
        id                integer,
        line_of_sight     integer,
        movement_rate     float,
        name              integer,
        range             integer,
        reload_time       float,
        search_radius     float,
        Upgraded          name);"""

    sql_create_structures_table = """CREATE TABLE IF NOT EXISTS Structures (
        order_id         integer PRIMARY KEY,
        age              name,
        armor            name,
        attack           float,
        build_time       integer,
        cost             name,
        expansion        name,
        hit_points       integer,
        id               integer,
        line_of_sight    float,
        name             name,
        range            name,
        reload_time      float,
        special          name
        );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_units_table)

        create_table(conn, sql_create_structures_table)

    else:
        print("Error! Cannot Create Database Connection")


#executes main() function
if __name__ == '__main__':
    main()
