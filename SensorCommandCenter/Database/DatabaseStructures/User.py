from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey 
from SensorCommandCenter.Database.DatabaseStructures import Base


class User(Base):

    __tablename__='users'

    user_id = Column(String, primary_key = True)