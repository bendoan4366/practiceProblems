import psycopg2

def create_table():
    conn = psycopg2.connect("dbname = 'tutorial' user ='postgres' password= 'P1usUltr@!' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id SERIAL PRIMARY KEY, title TEXT, author TEXT, year TEXT, isbn TEXT)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = psycopg2.connect("dbname = 'tutorial' user ='postgres' password= 'P1usUltr@!' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES(DEFAULT, %s,%s,%s,%s)",(title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname = 'tutorial' user ='postgres' password= 'P1usUltr@!' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()

    return rows

def search(id= 0, title="", author="", year="", isbn=""):
    conn = psycopg2.connect("dbname = 'tutorial' user ='postgres' password= 'P1usUltr@!' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE id = %s OR title=%s OR author=%s OR year=%s OR isbn=%s",(id, title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()

    return rows

#check
def delete(id):
    conn = psycopg2.connect("dbname = 'tutorial' user ='postgres' password= 'P1usUltr@!' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=%s", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = psycopg2.connect("dbname = 'tutorial' user ='postgres' password= 'P1usUltr@!' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


#delete(4)  
create_table()