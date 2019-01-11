import sqlite3
import time
import datetime
import random

from matplotlib import style
from pprint import pprint


# Do automatic backups!

def create_table(c):
    c.execute('CREATE TABLE IF NOT EXISTS dataToPlot(unix REAL, datastamp TEXT, keyword TEXT, value REAL)')


def simple_data_entry(c):
    c.execute("INSERT INTO dataToPlot VALUES (1234556,'2018-01-01','Python',5)")


def data_entry(c, data):
    columns = ', '.join(data.keys())
    placeholders = ', '.join('?' * len(data))
    sql = 'INSERT INTO dataToPlot ({}) VALUES ({})'.format(columns, placeholders)
    for d in data.values():
        print(type(d))
    c.execute(sql, data.values())


def dynamic_data_entry(c):
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime(('%Y-%m-%d %H:%M:%S')))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO dataToPlot VALUES (?,?,?,?)", (unix, date, keyword, value))
    # %s for MySQL
    # ? for SQLite


def read_from_db(c):
    c.execute("SELECT * FROM dataToPlot")
    lis = c.fetchall()
    pprint(lis)


def del_and_update(conn, c):
    c.execute("SELECT * FROM dataToPlot")
    [print(row) for row in c.fetchall()]

    c.execute("UPDATE dataToPlot SET value=99 WHERE value=(%s)" % 3)
    conn.commit()

    c.execute("SELECT * FROM dataToPlot")
    [print(row) for row in c.fetchall()]


conn = sqlite3.connect('cinema.db', timeout=10)
c = conn.cursor()
create_table(c)
unix = int(time.time())
dictdata = {'unix': int(time.time()),
            'datastamp': str(datetime.datetime.fromtimestamp(unix).strftime(('%Y-%m-%d %H:%M:%S'))),
            'keyword': 'Python', 'value': 2}
data_entry(c, dictdata)
conn.commit()
c.close()
conn.close()
