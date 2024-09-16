import sqlite3


##### Connect to database (create new database if it doesn't exist) 

conn = sqlite3.connect("SensorCommandCenter/Database/internal_sensor_database.db")

cursor = conn.cursor()

#GET CURRENT USER VERSION 
cursor.execute("PRAGMA user_version")
current_user_version = cursor.fetchall()[0][0] #Used to tell which update scripts need ran for the DB
print(current_user_version)
if current_user_version==0:
    #Run initiation and create scripts
    with open('SensorCommandCenter/Install Scripts/Database Files/SQLite (Internal)/tables.sql') as sql_file: 
        cursor.executescript(sql_file.read()) #Create Tables
        conn.commit() #Commit creation

print('start checking update scripts')


conn.close() #ALWAYS close your connections ;)
