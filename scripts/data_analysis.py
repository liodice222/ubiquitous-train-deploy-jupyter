from config import connection

# Create a cursor to execute sql and fetch data from ADW
cursor = connection.cursor()

# Execute a query
query = "SELECT * FROM table"
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()