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
def select():
    cur.execute("SELECT * from user_db.user_detail")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def insert():
    cur.execute("insert into user_db.user_detail(name)values('test from python3')")
    conn.commit()

def update():
    cur.execute("update  user_db.user_detail set name='new name added' where id = '1'")
    conn.commit()
    
def delete():
    cur.execute("delete from user_db.user_detail where id = '2'")
    conn.commit()
# to commit the operation in database
     



insert()
update()
delete()
select()

cur.close()
conn.close()