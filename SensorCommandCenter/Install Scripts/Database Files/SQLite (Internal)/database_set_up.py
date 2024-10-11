import os
import sqlite3
import tkinter
import tkinter.simpledialog 

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


update_file_paths = os.listdir('SensorCommandCenter/Install Scripts/Database Files/SQLite (Internal)/Update_Scripts')
for file in update_file_paths:
    print(file)

    #Check file update number, if it is greater than users current version...execute.





#Prompt user for the default Username/password internal account:
username = None
pw = None
while username is None:
    username = tkinter.simpledialog.askstring("Internal Admin Username","What username would you like for the built in administrative account:")
    #Call username validation..

while pw is None:    
    pw = tkinter.simpledialog.askstring(f"Internal Admin Password","What password would you like for {username}:")
    #call password validation

#hash pw


#store pw in database, creating user



conn.close() #ALWAYS close your connections ;)
