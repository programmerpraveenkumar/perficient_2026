import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    host="localhost",         # or IP address like "127.0.0.1"
    database="ecommerce",  # replace with your database name
    user="postgres",     # replace with your username
    password="roottoor", # replace with your password
    port="5432"               # default PostgreSQL port
)

# Create a cursor object
cur = conn.cursor()

# Example: execute a query
cur.execute("SELECT version();")

# Fetch result
db_version = cur.fetchone()
print("Connected to:", db_version)

# Close the connection
cur.close()
conn.close()
