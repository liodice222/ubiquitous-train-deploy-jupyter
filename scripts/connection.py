import cx_Oracle
import os
from config import WALLET_DIR, DB_USERNAME, DB_PASSWORD, DB_DSN

os.environ['TNS_ADMIN'] = WALLET_DIR

def get_connection():
    return cx_Oracle.connect(user=DB_USERNAME, password=DB_PASSWORD, dsn=DB_DSN)

def fetch_data(query):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results