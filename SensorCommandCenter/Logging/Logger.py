from SensorCommandCenter.Database.Database_Interfaces import InternalDBConnection



class Log:
    def __init__(self, log_name, log_source):
        self.name = log_name
        self.source = log_source 

    def log_to_database(self):
        db = Logger_DB()
        db.insert_log('Test',None)

    #Private acting method to store log into txt file if internal database is unavailable for some reason
    def __store_in_queue(self):
        pass 

    #Read from txt file and push to internal db
    def __push_from_queue_to_db(self):
        pass


class Logger_DB(InternalDBConnection):
    

    def insert_log(self, message, log_datetime):
        print('Insert Log called')
        if self.conn is None:
            self.connect()
        
        self.conn.commit()
        self.close_connection()
        

