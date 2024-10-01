import cx_Oracle

# Path to the wallet directory, from cloud shell
wallet_dir = "/home/liodice/dep"

# Update the TNS_ADMIN environment variable
import os
os.environ['TNS_ADMIN'] = wallet_dir

# Connection details
username = "your_adw_username"
password = "your_adw_password"
dsn = "your_adw_dsn"  # tnsname in db connection

# Establish the connection
connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)