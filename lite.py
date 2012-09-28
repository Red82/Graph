__author__ = 'red'
import sqlite3
mydatabase = "/home/red/red/PycharmProjects/mydatabase.db"
connection = sqlite3.connect(mydatabase)
cursor = connection.cursor()
cursor.execute('CREATE TABLE mytable (Id INTEGER PRIMARY KEY,'
               ' Date TEXT, Entry TEXT, Adr TEXT)')
connection.commit()


import time
today=time.strftime("%A, %B %d, %Y")
today
cursor.execute('INSERT INTO mytable Values(null, ?, ?, ?)',
    (today, "This entry could be the first item on a To-Do "
    "List, or it could be a journal entry, or whatever you want.", "!!!!"))
connection.commit()
cursor.execute('INSERT INTO mytable VALUES(null, ?, ?, ?)',
    (today, "To-Do: Write an SQLite3 tutorial!", "22222"))
connection.commit()

cursor.execute('SELECT * FROM mytable')



cursor.close()
quit()