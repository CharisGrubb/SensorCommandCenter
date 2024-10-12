import uuid
import sqlite3 #Used for internal db connection
import sqlalchemy #used for external db connection
import traceback
import os

from SensorCommandCenter.Database import IOValidation
from SensorCommandCenter.Logging import Logger


class InternalDBConnection():
    
    def __init__(self):
       self.conn = None
       self.log = Logger.Log("Internal_DB_Interface", "Database Interfaces")


    def __convert_results_to_json(self, results,headers:list):
        results_json=[]
        for r in results:
            row_json={}
            for col in range(len(r)):
                row_json[headers[col]]=r[col]
            results_json.append(row_json)
        return results_json

    def __connect(self):
        if os.path.exists("Database/internal_sensor_database.db"):
            self.conn = sqlite3.connect("Database/internal_sensor_database.db")
            self.log.log_to_database("System Connections","Connected to internal database successfuly",None)
        else:
            raise Exception("NO INTERNAL DB", os.getcwd())

    def add_sensor(self, sensor_name, sensor_model, sensor_type, import_type, create_user_id):
         
        self.__connect()
        try:
            new_sensor_id = uuid.uuid4()

            query = """INSERT INTO Sensors ( sensor_id, sensor_name, sensor_model, sensor_type, import_type 
                                            ,sensor_enabled, create_date, created_by)
                                VALUES(?, ?, ?, ?, ?, 0, CURRENT_TIMESTAMP,?);"""  ##Sensor is disabled by default. Additiona step required to enable sensor
            
            params = [new_sensor_id, sensor_name, sensor_model, sensor_type, import_type, create_user_id]

            crs = self.conn.cursor()
            crs.execute(query, parameters = params) 
            rows_affected = crs.rowcount
            self.conn.commit()
            self.__close_connection()
            return rows_affected
        except:
            #Pipe opperator (|) used in alerting. Alerts for certain logs will split at the pipe and only show the text6 before the pipe. This allows security around stack trace
            self.log.log_to_database("Database Query","Error inserting new sensor " +sensor_name + " | " + traceback.format_exc(),'ERROR', create_user_id )
            return -1
    
         

    def add_user(self, username:str, user_f_name:str, user_l_name:str, pw:str):
        #validate parameters
        IOValidation.InputOutputValidation.validate_user_name(username) #If it fails, error will be raised
        IOValidation.InputOutputValidation.validate_user_first_last_name(user_f_name, user_l_name)
        #encrypt pw, parameter should already be hashed


        #insert into the db 
        self.__connect()
        new_user_id = uuid.uuid4()

        self.__close_connection()

    def get_password_hash(self, username:str):

        #validate username for any unsafe characters
        IOValidation.InputOutputValidation.validate_user_name(username) #If it fails, error will be raised
        if  self.conn is not None:
            query = """ """

            #pull hash from database based on username

            #decrypt has before returning
        else:
            raise Exception("Not connected to database, cannot pull data!") #Raise error, do not return None or setinal value, it could be used to bypass controls
    
    def get_user_account_type(self, username:str):
        
        IOValidation.InputOutputValidation.validate_user_name(username) #If it fails, error will be raised
        
        query = """SELECT Acount_type FROM Users WHERE username = ?"""
        self.__connect()
        
        crs = self.conn.cursor()
        crs.execute(query, [username])
        resultsset = crs.fetchall()
        
        self.__close_connection()
        
        if len(resultsset):
            return resultsset[0][0]
        else:
            return None
        
        

    def get_sensor(self, sensor_id):
        pass

    def get_all_sensors(self):
        if self.conn is not None:
            crs = self.conn.cursor()
            crs.execute("""SELECT sensor_id,sensor_name,sensor_model,sensor_type ,import_type, sensor_enabled int, create_date ,created_by, modify_date ,modified_by
                        FROM Sensors;""") 
            resultsset = crs.fetchall()
            headers =[x[0] for x in crs.description]
            results = self.__convert_results_to_json(resultsset, headers)
            self.conn.commit()
            return results

    def get_all_model_sensors(self, model):
        pass

    def get_all_type_sensors(self, type):
        pass

    def get_configurations(self, config_name, category, sub_category): 
        self.conn.__connect()
        crs = self.conn.cursor()
        crs.execute("""SELECT *
                    FROM Configs;""") ####CHANGE TO HEADER NAMES...testing
        resultsset = crs.fetchall()
        headers =[x[0] for x in crs.description]
        results = self.__convert_results_to_json(resultsset, headers)
        self.conn.commit()
        self.__close_connection()
        return results
         
    def set_sensor_enabled(self,sensor_id, enabled):
        self.conn.__connect()
        crs = self.conn.cursor()
        crs.execute("UPDATE Sensors set enabled = ? where sensor_id = ?",[enabled, sensor_id])
        self.conn.commit()
        self.__close_connection()
        

    def add_sensor_datapoint(self, sensor_id, value, datetime_collected):
        pass

    

    def __close_connection(self):
        self.conn.close()
        self.conn = None
        

    
    def __update_encryptions(self):
        pass 

        #pull all pws with their username/ids 
        
        #loop through and decrypt each one

        #call load_encryption_key to rotate

        #loop through and encrypt each one again

        #update db with updated encryption

#PARENT-SQLAlchemy
class ExternalDBConnection():

    def __init__(self):
        self.internal_db_connection=InternalDBConnection()
        self.db_configurations = self.internal_db_connection.get_configurations()
        self.server_name = None #Set to proper columns 
        self.port = None
        self.driver = None
        self.db_name = None
        self.db_username = None
        self.db_password = None


    def get_engine(self):
        pass #Define generic or standard type connection

    def test_connection(self):

        query = "SELECT 1"

    def close_connection(self):
        pass

#Child
class ExternalDB_MSSQL(ExternalDBConnection):
     def get_engine(self):
        pass #Override engine with connection syntax specific to MSSQL 


#Child
class ExternalDB_MySQL(ExternalDBConnection):
    pass
