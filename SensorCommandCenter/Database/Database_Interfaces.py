import sqlite3 #Used for internal db connection
import sqlalchemy #used for external db connection
import traceback


class InternalDBConnection():
    
    def __init__(self):
        self.conn=None

    def connect(self):
        self.conn = sqlite3.connect("SensorCommandCenter/Database/internal_sensor_database.db")

    def get_configurations(self, config_name, category, sub_category): 
        pass

    def close_connection(self):
        self.conn.close()
        self.conn=None

#PARENT-SQLAlchemy
class ExternalDBConnection():

    def __init__(self):
        self.internal_db_connection=InternalDBConnection()
        self.db_configurations = self.internal_db_connection.get_configurations()


    def get_engine(self):
        pass #Define generic or standard type connection

    def close_connection(self):
        pass

#Child
class ExternalDB_MSSQL(ExternalDBConnection):
     def get_engine(self):
        pass #Override engine with connection syntax specific to MSSQL 


#Child
class ExternalDB_MySQL(ExternalDBConnection):
    pass
