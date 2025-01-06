from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column 
from SensorCommandCenter.Database.DatabaseStructures import Base


class Sensor(Base):

    __tablename__='sensors'

    sensor_id: Mapped[str] = mapped_column(String(50), primary_key = True)
    sensor_name: Mapped[str] = mapped_column(String(100))
    sensor_model: Mapped[str] = mapped_column(String(50))
    sensor_type: Mapped[str] = mapped_column(String(50))
    import_type: Mapped[int] = mapped_column(Integer)
    sensor_enabled = mapped_column(Integer)
    create_date = mapped_column(Date)
    created_by = mapped_column(String, ForeignKey("users.user_id"))
    modify_date = mapped_column(Date)
    modified_by = mapped_column(String, ForeignKey("users.user_id"))