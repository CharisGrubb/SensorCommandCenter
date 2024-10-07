import uuid
import sqlite3 #Used for internal db connection
import sqlalchemy #used for external db connection
import traceback
import os


class InternalDBConnection():
    
    def __init__(self):
        self.conn=None

    def __convert_results_to_json(self, results,headers:list):
        results_json=[]
        for r in results:
            row_json={}
            for col in range(len(r)):
                row_json[headers[col]]=r[col]
            results_json.append(row_json)
            
        return results_json

    def connect(self):
        if os.path.exists("Database/internal_sensor_database.db"):
            self.conn = sqlite3.connect("Database/internal_sensor_database.db")
            print("CONNECTED! ", self.conn)
        else:
            print("NO DB", os.getcwd())

    def add_sensor(self, sensor_name, sensor_model, sensor_type, import_type, create_user_id):
         if self.conn is not None:

            new_sensor_id = uuid.uuid4()

            query = """INSERT INTO Sensors ( sensor_id, sensor_name, sensor_model, sensor_type, import_type 
                                            ,sensor_enabled, create_date, created_by
                                VALUES(?, ?, ?, ?, ?, 0, CURRENT_TIMESTAMP,?);"""  ##Sensor is disabled by default. Additiona step required to enable sensor
            
            params = [new_sensor_id, sensor_name, sensor_model, sensor_type, import_type, create_user_id]

            crs = self.conn.cursor()
            crs.execute(query, parameters = params) 
            rows_affected = crs.rowcount
            print(rows_affected)
            self.conn.commit()

            return rows_affected
         

    def add_user(self, username, user_f_name, user_l_name, pw):
        pass


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
         if self.conn is not None:
            crs = self.conn.cursor()
            crs.execute("""SELECT *
                        FROM Configs;""") ####CHANGE TO HEADER NAMES...testing
            resultsset = crs.fetchall()
            headers =[x[0] for x in crs.description]
            results = self.__convert_results_to_json(resultsset, headers)
            self.conn.commit()
            return results
         
    def set_sensor_enabled(sensor_id, enabled):
        pass

    def add_sensor_datapoint(self, sensor_id, value, datetime_collected):
        pass

    def store_log(self, log_name, log_source, log_message, log_datetime):
        pass

    def close_connection(self):
        if self.conn is not None:
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
