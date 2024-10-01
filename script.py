#rough idea of script

import oci
import cx_Oracle
import pandas as pd
import json
import requests

def handler(ctx, data: io.BytesIO = None):
    # Configuration for OCI and ADW
    
    # Details for ADW, will be in config.py
    dsn = "your_adw_dsn"
    username = "your_username"
    password = "your_password"
    
    #Connect to ADW in connection.py
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()

    
    # Trigger the execution of the notebook, deploy to front end w notebook and post results in public instance
    execution_response = requests.post('129.213.149.204', json={'notebook': notebook_content})
    
    return {
        "statusCode": execution_response.status_code,
        "body": execution_response.text
    }