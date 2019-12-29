import sqlite3


def connect():
    connection = sqlite3.connect('book.db')
    cursor = connection.cursor()
    create_query = 'CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY ,title text, author text, year INTEGER, isbn INTEGER)'
    cursor.execute(create_query)
    connection.commit()
    connection.close()

def insert(title,author,year,isbn):
    connection = sqlite3.connect('book.db')
    cursor = connection.cursor()
    insert_query = "INSERT INTO book VALUES (NULL,?,?,?,?)"
    cursor.execute(insert_query, (title,author,year,isbn))
    connection.commit()
    connection.close()

def view():
    connection =sqlite3.connect('book.db')
    cursor=connection.cursor()
    select_query="SELECT * FROM book"
    cursor.execute(select_query)
    row=cursor.fetchall()
    connection.commit()
    connection.close()
    return row


def search(title="",author="",year="",isbn=""):
    connection = sqlite3.connect('book.db')
    cursor = connection.cursor()
    search_query = "SELECT * FROM book where title=? OR author= ? OR year=? OR isbn=?"
    cursor.execute(search_query, (title,author,year,isbn))
    row = cursor.fetchall()
    connection.commit()
    connection.close()
    return row




connect()