import urllib
import psycopg2
from psycopg2.pool import SimpleConnectionPool
import pandas as pd
from sqlalchemy.pool import NullPool
from sqlalchemy import create_engine

pghost = "localhost"
pgdatabase = "postgres"
pguser = "postgres"
pgpassword = "123123123"
pgport = "5432"

conn_string = "postgres://"+pguser+":"+urllib.parse.quote(pgpassword)+"@"+pghost+":"+pgport+"/"+pgdatabase
conn_postgres = psycopg2.connect(conn_string)

conn = SimpleConnectionPool(0, 25,conn_string)

def Querying(query):
    conn_postgres = conn.getconn()
    df = pd.read_sql(query, conn_postgres)
    conn.putconn(conn_postgres)
    return(df)