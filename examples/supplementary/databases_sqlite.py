import os
import random
import sqlite3

from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('data/todos.db')
        return con
    except Error:
        print(Error)


def create_table(connection):
    cursor = connection.cursor()
    # Check if table already exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='todos'")
    rows = cursor.fetchall()

    # If not, create table
    if len(rows) == 0:
        cursor.execute("CREATE TABLE todos(task TEXT, done INTEGER)")
    connection.commit()


def create_task(connection, task, complete=False):
    done = 1 if complete else 0
    connection.cursor().execute("INSERT INTO todos (task, done) VALUES(?, ?)", (task, done))
    connection.commit()


def fetch_tasks(connection, complete=None):
    cursor = connection.cursor()
    if complete is None:
        cursor.execute('SELECT task FROM todos')
    else:
        values = (1,) if complete else (0,)
        cursor.execute('SELECT task FROM todos WHERE done=?', values)
    rows = cursor.fetchall()
    return [row[0] for row in rows]


def load_data(connection):
    with open('data/todos.csv') as file:
        file.readline()
        for line in file.readlines():
            items = line.split(',')
            task = items[0]
            done = bool(int(items[1]))
            create_task(connection, task, done)


if __name__ == '__main__':
    con = sql_connection()
    create_table(con)
    if len(fetch_tasks(con)) == 0:
        load_data(con)

    print('Todo:')
    print(fetch_tasks(con, complete=False))
    print('Done:')
    print(fetch_tasks(con, complete=True))
    con.close()
