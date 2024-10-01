import cx_Oracle

# Path to the wallet directory
wallet_dir = "/path/to/wallet"

# Update the TNS_ADMIN environment variable
import os
os.environ['TNS_ADMIN'] = wallet_dir

# Connection details
username = "your_adw_username"
password = "your_adw_password"
dsn = "your_adw_dsn"  # This can be found in the tnsnames.ora file in the wallet directory

# Establish the connection
connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)