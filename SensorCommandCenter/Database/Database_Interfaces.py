import sqlite3 #Used for internal db connection
import sqlalchemy #used for external db connection


class InternalDBConnection():
    
    def __init__(self):
        self.conn=None

    def connect(self):
        self.conn = sqlite3.connect("SensorCommandCenter/Database/internal_sensor_database.db")

    def close_connection(self):
        self.conn.close()
        self.conn=None

#PARENT
class ExternalDBConnection():

    def __init__(self):
        pass

    def connect(self):
        pass 

    def close_connection(self):
        pass

#Child
class ExternalDB_MSSQL(ExternalDBConnection):
    pass


#Child
class ExternalDB_MySQL(ExternalDBConnection):
    pass
