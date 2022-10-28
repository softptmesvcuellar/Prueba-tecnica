import mysql.connector
from dump_db import dump_db
from upload_db import upload_db
import os

default_schemas = ('information_schema', 'preformance_schema', 'mysql')

BUCKET = os.environ.get("BUCKET")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")

def get_db_list(connector: mysql.connector):
    cur = connector.cursor()
    databases = ("show databases")
    cur.execute(databases)
    return databases


conn = mysql.connector.connect(user=USER, password=PASSWORD,
                               host=HOST, buffered=True)
db_list = get_db_list(conn)


for db in get_db_list():
    if db[0] in default_schemas:
        pass
    else:
        backup_name = dump_db(host=HOST,port=PORT,user=USER,passwd=PASSWORD,db=db[0])
        upload_result = upload_db(backup_name, BUCKET)
        print(upload_result)

