import psycopg2


def create_table():
    conn = psycopg2.connect("dbname = 'tutorial' user ='postgres' password= 'P1usUltr@!' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(database_name, item, quantity, price):
    conn = psycopg2.connect(database_name)
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item, quantity, price))
    conn.commit()
    conn.close()

def view(database_name):
    conn = psycopg2.connect(database_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()

    return rows

def delete(database_name, item):
    conn = psycopg2.connect(database_name)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update(database_name, item, quantity, price):
    conn = psycopg2.connect(database_name)
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity =%s, price =%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


database_creds = "dbname = 'tutorial' user ='postgres' password= 'P1usUltr@!' host = 'localhost' port = '5432'"
table_name = "store"

insert(database_creds, "Beer", 10, 15.50)
#delete(database_creds, "Chili")
print(view(database_creds))

#update("lite.db", "Beer",1,20)
#print(view("lite.db", "store"))