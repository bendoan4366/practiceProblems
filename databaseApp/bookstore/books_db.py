import psycopg2

class booksDatabase:

    def __init__(self):
        self.conn = psycopg2.connect("dbname = 'tutorial' user ='postgres' password= 'P1usUltr@!' host = 'localhost' port = '5432'")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (id SERIAL PRIMARY KEY, title TEXT, author TEXT, year TEXT, isbn TEXT)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO books VALUES(DEFAULT, %s,%s,%s,%s)",(title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    def search(self, id= 0, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM books WHERE id = %s OR title=%s OR author=%s OR year=%s OR isbn=%s",(id, title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM books WHERE id=%s", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE books SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()