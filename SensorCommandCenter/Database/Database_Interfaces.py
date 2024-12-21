import uuid
import sqlite3 #Used for internal db connection
import sqlalchemy #used for external db connection
import traceback
import os

from SensorCommandCenter.Database import IOValidation, Database_Interface_Parents
from SensorCommandCenter.Logging.Logger import Log

       

#Child Internal
class InternalDBConnection(Database_Interface_Parents.InternalDB):
    
    def __init__(self):
        super().__init__()
        self.log = Log("Internal_DB_Interface", "Database Interfaces")


    def __convert_results_to_json(self, results,headers:list):
        results_json=[]
        for r in results:
            row_json={}
            for col in range(len(r)):
                row_json[headers[col]]=r[col]
            results_json.append(row_json)
        return results_json

   

    def add_sensor(self, sensor_name, sensor_model, sensor_type, import_type, create_user_id):
         
        self._InternalDB__connect()
        try:
            new_sensor_id = str(uuid.uuid4())

            query = """INSERT INTO Sensors ( sensor_id, sensor_name, sensor_model, sensor_type, import_type 
                                            ,sensor_enabled, create_date, created_by)
                                VALUES(?, ?, ?, ?, ?, 0, CURRENT_TIMESTAMP,?);"""  ##Sensor is disabled by default. Additiona step required to enable sensor
            
            params = [new_sensor_id, sensor_name, sensor_model, sensor_type, import_type, create_user_id]

            crs = self.conn.cursor()
            crs.execute(query, params) 
            rows_affected = crs.rowcount
            self.conn.commit()
            self._InternalDB__close_connection()
            return rows_affected
        except:
            #Pipe opperator (|) used in alerting. Alerts for certain logs will split at the pipe and only show the text6 before the pipe. This allows security around stack trace
            self.log.log_to_database("Database Query","Error inserting new sensor " +sensor_name + " | " + traceback.format_exc(),'ERROR', create_user_id )
            return -1
    
         

    def add_user(self, username:str, user_f_name:str, user_l_name:str, pw:str, access:str='R', access_until = None, account_type:str = 'Internal', user_m_initial:str = None):
        #validate parameters
        IOValidation.InputOutputValidation.validate_user_name(username) #If it fails, error will be raised
        IOValidation.InputOutputValidation.validate_user_first_last_name(user_f_name, user_l_name)

        #encrypt pw, parameter should already be hashed
        pw = IOValidation.Ryptor.encrypt(pw)

        #Convert Access string to integer for storage
      
        #insert into the db 
        self._InternalDB__connect()
        crs = self.conn.cursor()

        new_user_id = uuid.uuid4()
        query = """INSERT INTO dbo.Users (user_id, username, user_pw, user_f_name, user_l_name, user_middle_initial, access_level, access_until, account_type)
                               VALUES(?,?,?,?,?,?,?,?,?) """
        
        # crs.execute(query, [new_user_id, username, pw, user_f_name, user_l_name, user_m_initial])

        self._InternalDB__close_connection()


    def check_for_enabled_admin(self):
        self._InternalDB__connect()
        query = """SELECT Count(1) FROM Users WHERE Account_type = 'Global Admin' and coalesce(access_until, CURRENT_TIMESTAMP +1) > CURRENT_TIMESTAMP"""
        crs = self.conn.cursor()
        crs.execute(query)
        results = crs.fetchall()
        self._InternalDB__close_connection()

        if results is not None and len(results):
            return results[0][0]
        else:
            return False

    #returns the unencrypted hashed password for INTERNAL users only. 
    def get_password_hash(self, username:str):

        #validate username for any unsafe characters
        IOValidation.InputOutputValidation.validate_user_name(username) #If it fails, error will be raised
        self._InternalDB__connect()
        if  self.conn is not None:
            query = """SELECT user_pw FROM dbo.Users WHERE username = ? AND Account_type = 'Internal'"""
            crs = self.conn.cursor()

            #pull hash from database based on username
            crs.execute(query, [username])
            result = crs.fetchall()

            crs.close()
            self._InternalDB__close_connection()

            #decrypt has before returning
            if len(result):
                pw = IOValidation.Ryptor.decrypt(result[0][0])
                return pw
            else:
                self.log.log_to_database("Authentication", f"No internal user {username} found.","ALERT")
                raise Exception("No such internal user!")

        else:
            raise Exception("Not connected to database, cannot pull data!") #Raise error, do not return None or setinal value, it could be used to bypass controls
        
       
    
    def get_all_users(self):
        self._InternalDB__connect()
        if self.conn is not None: 
            query = """SELECT Username FROM Users"""
            crs = self.conn.cursor()

            crs.execute(query)
            result = crs.fetchall()
            
            if result is not None and len(result):
                headers = [x[0] for x in crs.description]
                return self.__convert_results_to_json(result)
            else:
                return None


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
        self._InternalDB__connect()
        if self.conn is not None:
            crs = self.conn.cursor()
            crs.execute("""SELECT sensor_id,sensor_name,sensor_model,sensor_type ,import_type, sensor_enabled int, create_date ,created_by, modify_date ,modified_by
                        FROM Sensors;""") 
            resultsset = crs.fetchall()
            headers =[x[0] for x in crs.description]
            results = self.__convert_results_to_json(resultsset, headers)
            self.conn.commit()
            self._InternalDB__close_connection()
            return results

    def get_all_model_sensors(self, model):
        pass

    def get_all_type_sensors(self, sensor_type):
        self._InternalDB__connect()
        crs = self.conn.cursor()
        crs.execute("""SELECT  sensor_id, sensor_name, sensor_model, import_type ,sensor_enabled
                    FROM Sensors
                    WHERE Sensor_type = ?;""",[sensor_type])
        resultsset = crs.fetchall()
        headers =[x[0] for x in crs.description]
        results = self.__convert_results_to_json(resultsset, headers)
        self.conn.commit()
        self._InternalDB__close_connection()
        return results

    def get_configurations(self, config_name, category = None, sub_category = None): 
        self._InternalDB__connect()
        crs = self.conn.cursor()
        crs.execute("""SELECT *
                    FROM Configs;""") ####CHANGE TO HEADER NAMES...testing
        resultsset = crs.fetchall()
        headers =[x[0] for x in crs.description]
        results = self.__convert_results_to_json(resultsset, headers)
        self.conn.commit()
        self._InternalDB__close_connection()
        return results
         
    def set_sensor_enabled(self,sensor_id, enabled):
        self.conn.__connect()
        crs = self.conn.cursor()
        crs.execute("UPDATE Sensors set enabled = ? where sensor_id = ?",[enabled, sensor_id])
        self.conn.commit()
        self.__close_connection()


    def add_sensor_datapoint(self, sensor_id, value, datetime_collected):

        self._InternalDB__connect()
        crs = self.conn.cursor()

        query = """INSERT INTO Sensor_data_points (Sensor_ID, Val, Create_Date)
                                                VALUES (? , ?, ?)"""
        crs.execute(query, [sensor_id, value, datetime_collected])

        rows_affected = crs.rowcount
        self.conn.commit()
        self._InternalDB__close_connection()

        return rows_affected

    


    
    def _update_encryptions(self):
         
        #check if key has already been loaded (on inital instalation, it will be false)
        if IOValidation.Ryptor.check_for_encryption_key():
            #update global variable to pause all data flows affecting encryption/decrytpion
            pass
            #pull all pws with their username/ids 
            
            #loop through and decrypt each one

            #call load_encryption_key to rotate

            #loop through and encrypt each one again

            #update db with updated encryption

            #update global variable to pause all data flows affecting encryption/decrytpion
        else:
            if not IOValidation.Ryptor.load_encryption_key():
                raise Exception("Issue loading encryption key!")
            


#Child
class ExternalDB_MSSQL(Database_Interface_Parents.ExternalDBConnection):
     def get_engine(self):
        pass #Override engine with connection syntax specific to MSSQL 


#Child
class ExternalDB_MySQL(Database_Interface_Parents.ExternalDBConnection):
    def get_engine(self):
        pass #Override engine with connection syntax specific to MySQL 


#Child 
class ExternalDB_SQLite(Database_Interface_Parents.ExternalDBConnection):

    ###!!!! Test SQLite connection hosted on another server/system
    def get_engine(self):
        pass #Override engine with connection syntax specific to SQLite  



#Child 
class ExternalDB_PosgreSQL(Database_Interface_Parents.ExternalDBConnection):
    def get_engine(self):
        pass #Override engine with connection syntax specific to Posgres 