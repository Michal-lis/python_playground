import sqlite3
import time
import datetime
import random

from pprint import pprint


# time.time() provides time in seconds since the epoch(begging of the era) as fpn
# time.gmtime(0) to check what epoch is the sstem using
# time.sleep(x) - waits for SECONDS
# "%.3f"


def create_table(c):
    c.execute('CREATE TABLE IF NOT EXISTS dataToPlot(unix REAL, datastamp TEXT, keyword TEXT, value REAL)')


def simple_data_entry(c):
    c.execute("INSERT INTO dataToPlot VALUES (1234556,'2018-01-01','Python',5)")


def data_entry(data):
    c.execute('INSERT INTO dataToPlot VALUES (%s)' % data)


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


conn = sqlite3.connect('example2.db', timeout=10)
c = conn.cursor()
create_table(c)
# simple_data_entry(c)
for i in range(10):
    dynamic_data_entry(c)
    time.sleep(1)
read_from_db(c)
conn.commit()
c.close()
conn.close()
