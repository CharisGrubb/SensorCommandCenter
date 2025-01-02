from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey 
from SensorCommandCenter.Database.DatabaseStructures import Base


class Sensor(Base):

    __tablename__='sensors'

    sensor_id = Column(String, primary_key = True)
    sensor_name = Column(String)
    sensor_model = Column(String)
    sensor_type = Column(String)
    import_type = Column(Integer)
    sensor_enabled = Column(Integer)
    create_date = Column(Date)
    created_by = Column(String, ForeignKey("users.user_id"))
    modify_date = Column(Date)
    modified_by = Column(String, ForeignKey("users.user_id"))