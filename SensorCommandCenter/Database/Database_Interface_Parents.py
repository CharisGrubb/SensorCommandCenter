
import sqlite3 #Used for internal db connection
import sqlalchemy #used for external db connection
import traceback
import os


#parent Internal 
class InternalDB():
    def __init__(self):
       self.conn = None

    def __connect(self):
        if os.path.exists(os.path.dirname(__file__) + "/internal_sensor_database.db"):
            self.conn = sqlite3.connect(os.path.dirname(__file__) + "/internal_sensor_database.db")
        else:
            print(os.curdir)
            raise Exception("NO INTERNAL DB", os.getcwd())
        
    def __close_connection(self):
        self.conn.close()
        self.conn = None


#PARENT-SQLAlchemy
class ExternalDBConnection():

    def __init__(self, server_name, server_port, local_driver, protocol, db_name, trusted_source = True, db_username = None, db_password = None):
        
        if not trusted_source and (db_username in ['', None, ' '] or db_password in ['', None, ' ']):
            raise Exception("Cannot connect to database without valid username/password or trusted source enabled.")
        
        self.server_name = None #Set to proper columns 
        self.port = None
        self.driver = None
        self.protocol = protocol
        self.db_name = None
        self.db_username = None
        self.db_password = None


    def get_engine(self):
        pass #Define generic or standard type connection

    def test_connection(self):

        query = "SELECT 1"

    def close_connection(self):
        pass
        