from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column 
from SensorCommandCenter.Database.DatabaseStructures import Base


class Data_Points(Base):
    __tablename__ = "data_points"

    id: Mapped[int] = mapped_column(primary_key=True)

    