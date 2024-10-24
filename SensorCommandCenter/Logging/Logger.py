import traceback

from datetime import datetime
from Database.Database_Interface_Parents import InternalDB



class Log:
    def __init__(self, log_name, log_source):
        self.name = log_name
        self.source = log_source 
        self.db = Logger_DB()

    def log_to_database(self, log_type, message, log_level, user_id = None):
        try:
            self.db.store_log(self.name, log_type, self.source, message, log_level,str(datetime.now()) , user_id)
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


class Logger_DB(InternalDB):
     #Inheritance, child of InternalDB conn
    def store_log(self, log_name, log_type, log_source, log_message, log_level,log_datetime, user_id:str=None):
        self.__connect()


        query = """INSERT INTO logs ( user_id, log_note, log_level ,log_type ,log_source ,log_name ,create_date)
                            VALUES(?, ?, ?, ?, ?, ?, ?);"""  ##Sensor is disabled by default. Additiona step required to enable sensor
        
        params = [user_id, log_message, log_level, log_type, log_source, log_name, log_datetime]

        crs = self.conn.cursor()
        crs.execute(query,  params) 
        rows_affected = crs.rowcount
        print(rows_affected)
        self.conn.commit()

        self.__close_connection()

        return rows_affected

  

         

