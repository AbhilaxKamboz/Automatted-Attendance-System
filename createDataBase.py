import sqlite3
import playsound
from tkinter import messagebox
conn = sqlite3.connect('AttendanceDB.db')
c = conn.cursor()
sql = """
DROP TABLE IF EXISTS users1;
CREATE TABLE users1 (
           id integer unique primary key autoincrement,
           name text
);
"""
c.executescript(sql)
print("User Table created successfully in database")
playsound.playsound('voice/databaseCreated.mp3')
conn.commit()
conn.close()
messagebox.showinfo("","DataBase Created Sucess...")