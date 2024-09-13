import sqlite3


##### Connect to database (create new database if it doesn't exist) 

conn = sqlite3.connect("SensorCommandCenter/Database/internal_sensor_database.db")

cursor = conn.cursor()

with open('tables.sql') as sql_file: 
    cursor.executescript(sql_file.read()) #Create Tables
    conn.commit() #Commit creation


conn.close() #ALWAYS close your connections ;)
