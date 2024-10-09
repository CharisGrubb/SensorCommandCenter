import traceback

from datetime import datetime
from SensorCommandCenter.Database.Database_Interfaces import InternalDBConnection



class Log:
    def __init__(self, log_name, log_source):
        self.name = log_name
        self.source = log_source 
        self.db = Logger_DB()

    def log_to_database(self, log_type, message, user_id = None):
        try:
            self.db.connect()
            self.db.store_log(self.name, log_type, self.source, message, str(datetime.now()) , user_id)
            self.__push_from_queue_to_db()
            self.db.close_connection()
        except:
            print(traceback.format_exc())
            self.__store_in_queue()

    #Private acting method to store log into txt file if internal database is unavailable for some reason
    def __store_in_queue(self):
        print('In store to queue')
        pass 

    #Read from txt file and push to internal db
    def __push_from_queue_to_db(self):
        pass


class Logger_DB(InternalDBConnection):
     #Inheritance, child of InternalDB conn
    def store_log(self, log_name, log_type, log_source, log_message, log_datetime, user_id:str=None):
         if self.conn is not None:


            query = """INSERT INTO logs ( user_id, log_note ,log_type ,log_source ,log_name ,create_date)
                                VALUES(?, ?, ?, ?, ?, ?);"""  ##Sensor is disabled by default. Additiona step required to enable sensor
            
            params = [user_id, log_message, log_type, log_source, log_name, log_datetime]

            crs = self.conn.cursor()
            crs.execute(query,  params) 
            rows_affected = crs.rowcount
            print(rows_affected)
            self.conn.commit()

            return rows_affected

    ###Testing this approach to avoid circular imports, have all logging go through this interface, and utilize code reuse

         

