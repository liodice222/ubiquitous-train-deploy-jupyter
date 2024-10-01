from config import connection

# Create a cursor
cursor = connection.cursor()

# Execute a query
query = "SELECT * FROM your_table_name"
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()