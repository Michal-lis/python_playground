import sqlite3


def create_table(c):
    c.execute('CREATE TABLE IF NOT EXISTS dataToPlot(unix REAL, datastamp TEXT, keyword TEXT, value REAL)')


def simple_data_entry(c):
    c.execute("INSERT INTO dataToPlot VALUES (123456,'2018-01-01','Python',5)")


def data_entry(data):
    c.execute('INSERT INTO dataToPlot VALUES (%s)' % data)


conn = sqlite3.connect('example2.db')
c = conn.cursor()
create_table(c)
simple_data_entry(c)
