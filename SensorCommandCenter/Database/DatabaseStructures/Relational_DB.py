from sqlalchemy import MetaData, Integer, String, DateTime, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column 

class Base(DeclarativeBase):
    metadata = MetaData(schema="SensorCommandCenter")


class Sensor(Base):

    __tablename__='sensors'

    sensor_id: Mapped[str] = mapped_column(String(50), primary_key = True)
    sensor_name: Mapped[str] = mapped_column(String(100))
    sensor_model: Mapped[str] = mapped_column(String(50))
    sensor_type: Mapped[str] = mapped_column(String(50))
    import_type: Mapped[int] = mapped_column(Integer)
    sensor_enabled = mapped_column(Integer)
    create_date = mapped_column(DateTime)
    created_by = mapped_column(String, ForeignKey("users.user_id"))
    modify_date = mapped_column(DateTime)
    modified_by = mapped_column(String, ForeignKey("users.user_id"))

class Data_Points(Base):
    __tablename__ = "data_points"

    id: Mapped[int] = mapped_column(primary_key=True)

    
class User(Base):

    __tablename__='Users'
    user_id: Mapped[int] = mapped_column(primary_key = True)

class Configs(Base):
    __tablename__ = "logs"
    config_id: Mapped[int] = mapped_column(primary_key = True)


class Logs(Base):
    __tablename__ = "logs"
    log_id: Mapped[int] = mapped_column(primary_key = True)