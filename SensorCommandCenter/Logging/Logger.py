import os
import traceback

from datetime import datetime
from SensorCommandCenter.Database.Database_Interface_Parents import InternalDB



class Log:
    def __init__(self, log_name, log_source):
        self.name = log_name
        self.source = log_source 
        self.db = Logger_DB()

    def log_to_database(self, log_type, message, log_level, user_id = None):
        try:
            log_time = str(datetime.now())
            self.db.store_log(self.name, log_type, self.source, message, log_level, log_time , user_id)
            self.__push_from_queue_to_db()
            self.db.close_connection()
        except:
            print(traceback.format_exc())
            self.__store_in_queue(message, log_level, log_time,user_id)

    #Private acting method to store log into txt file if internal database is unavailable for some reason
    def __store_in_queue(self, message, level, log_time, log_type, user_id):

        with open(os.path.dirname(__file__)+'Log_Queue.txt','a') as f: #!!!!TEST the OS package working in docker and other OS systems 
            f.write(str(log_time) + '---' +message + '---' + level + '---' + log_type + '---' + self.source + '---' + self.name + '---' + str(user_id))
            f.close()

    #Read from txt file and push to internal db
    def __push_from_queue_to_db(self): ###!!!!!Investigate upgrading to a json file of stored logs....
        
        lines_to_rewrite = []
        f = open(os.path.dirname(__file__)+'Log_Queue.txt','r')
        for line in f:
            try:
                line_split = line.string().split('---')
                Logger_DB.store_log(log_name = line_split[5]
                                    , log_type = line_split[3]
                                    , log_source = line_split[4]
                                    , log_message = line_split[1]
                                    , log_level = line_split[2]
                                    ,log_datetime = line_split[0]
                                    , user_id = line_split[6])
            except: #If any lines fail to push to the database, add them to a list to rewrite to file
                lines_to_rewrite.append(line)
        f.close()

        if len(lines_to_rewrite): #If there are any lines to rewrite back, write them to the file. 'w' will overwrite what was there.
            f = open(os.path.dirname(__file__)+"/Log_Queue.txt",'w') ####!!!! TEST CONCUNRRENCY....ways to mitigate a loss of things going in and out at the same time
            for line in lines_to_rewrite:
                f.write(line)
            
            f.close() #Always close your files and streams ;)



class Logger_DB(InternalDB):
     #Inheritance, child of InternalDB conn
    def store_log(self, log_name, log_type, log_source, log_message, log_level,log_datetime, user_id:str=None):
        self._InternalDB__connect()


        query = """INSERT INTO logs ( user_id, log_note, log_level ,log_type ,log_source ,log_name ,create_date)
                            VALUES(?, ?, ?, ?, ?, ?, ?);"""  ##Sensor is disabled by default. Additiona step required to enable sensor
        
        params = [user_id, log_message, log_level, log_type, log_source, log_name, log_datetime]

        crs = self.conn.cursor()
        
        crs.execute(query,  params) 
        rows_affected = crs.rowcount

        self.conn.commit()
        self._InternalDB__close_connection()

        return rows_affected

  

         

