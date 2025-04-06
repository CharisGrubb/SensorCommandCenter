
from SensorCommandCenter.Database.DatabaseStructures.Relational_DB import Base
import sqlalchemy #used for external db connection
import traceback



#parent Internal 
class InternalDB():
    def __init__(self):
       
        self.engine = sqlalchemy.create_engine("sqlite.:///internal_sensor_database.db")
        Base.metadata.create_all(self.engine)
        self.Session = sqlalchemy.orm.sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()



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
        