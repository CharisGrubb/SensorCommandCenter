from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column 
from SensorCommandCenter.Database.DatabaseStructures import Base


class Logs(Base):
    __tablename__ = "logs"

    log_id: Mapped[int] = mapped_column(primary_key = True)